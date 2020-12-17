import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import logging
import threading
import time
from api import API
from Algos import Simplino

from ui_widget_simplino import Ui_Form

MAKER_REFERAL_DISCOUNT = 0.6

class TopSimplino(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.calculate_button.clicked.connect(lambda: self.btn_calculate_simplino())
        self.ui.start_button.clicked.connect(lambda: self.btn_start())
        self.ui.stop_button.clicked.connect(lambda: self.btn_stop())

        self.api = API("binance")  # Create and instance that can communicate with an exchange
        self.simplino = None
        self.on_mount(self.api)

        self.thread_simplino = None
        self.thread_simplino_kill = False
        self.running = False
        self.show()
    def btn_calculate_simplino(self):

        start_price = float(self.ui.start_price_text_input.text())
        nb_buy = int(self.ui.nb_buy_text_input.text())
        drop_percent = float(self.ui.drop_poucent_text_input.text())
        pair = self.ui.pair_comboBox.currentText()
        more_percent = float(self.ui.percent_more_buy_label.text())

        self.simplino = Simplino(pair)

        info = self.api.exchange.fetch_balance()
        balances = info['info']['balances']

        for asset in balances:  # fetch the balance of the pairing asset. Selling side
            if asset['asset'] == self.simplino.sell_asset:
                balance = float(asset['free'])

        self.simplino.simplino_algo_create_buys(balance, start_price, drop_percent / 100, nb_buy, more_percent)

        self.create_table()
        self.set_pair_label()

    def btn_start(self):
        if self.simplino.ready:  # if buy and sell price ready
            if not self.running:

                success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                  "Buy",
                                                                                  self.simplino.buyPrices[0],
                                                                                  self.simplino.buy_qtys[0])

                if success:
                    print("Simplino start")
                    self.ui.start_time_label.setText(str(time.time()))
                    print("Starting thread for simplino")
                    self.running = True
                    self.thread_simplino = threading.Thread(target=self.main_simplino)
                    self.thread_simplino.start()

                    return True

                else:
                    logging.error("Could not start simplino")
                    return False

            else:
                logging.error("Simplino already running")
                return False

        else:
            logging.error("Simplino context not set")
            return False

    def btn_stop(self):
        if self.running:
            self.thread_simplino_kill = True
            self.thread_simplino.join()
            self.thread_simplino_kill = False
            self.running = False
            logging.debug("thread KILLED")
        else:
            logging.info("Simplino is not running")

    def main_simplino(self):
        while True:
            if self.thread_simplino_kill:
                return

            orderbook = self.api.exchange.fetch_order_book(self.simplino.pair)
            print(self.simplino.buy_order_id, self.simplino.sell_order_id)
            buy_filled, buy_order_info = self.api.order_isfilled(self.simplino.pair,
                                                                 self.simplino.buy_order_id)
            if self.simplino.sell_order_id is not 0:
                sell_filled, sell_order_info = self.api.order_isfilled(self.simplino.pair,
                                                                       self.simplino.sell_order_id)
            else:
                sell_filled = False
                sell_order_info = None

            if buy_filled:
                self.buy_order_filled(buy_order_info)
            elif sell_filled:
                self.sell_order_filled(sell_order_info)

            self.update_visual(orderbook, buy_filled, sell_filled, buy_order_info, sell_order_info)

            time.sleep(1)  # exchange polling rate

    def buy_order_filled(self, order_info):
        self.simplino.nb_buys += 1
        qty = float(order_info["info"]["executedQty"])
        price = float(order_info["info"]["price"])
        self.simplino.buy_qty += qty
        self.simplino.nb_possible_sell = self.simplino.nb_buys - self.simplino.nb_sells

        fee_rate = self.api.exchange.markets[self.simplino.pair]['maker']

        self.simplino.invested -= (1 + (fee_rate * MAKER_REFERAL_DISCOUNT)) * qty * price

        if self.simplino.nb_possible_sell > 1:  # a sell order is open?
            self.api.cancel_order(self.simplino.sell_order_id, self.simplino.pair)
        else:
            logging.info("no active sell order")

        if self.simplino.nb_possible_sell < self.simplino.nb_buy_depth:
            buy_price = self.simplino.buyPrices[self.simplino.nb_possible_sell]
            buy_qty = self.simplino.buy_qtys[self.simplino.nb_possible_sell]

            success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                              "Buy",
                                                                              buy_price,
                                                                              buy_qty)
        else:
            logging.info("Buy depth reached cant buy more!")

        # Always can sell after a buy order is filled
        sell_price = self.simplino.sell_prices[self.simplino.nb_possible_sell - 1]
        sell_qty = self.simplino.buy_qty / self.simplino.nb_possible_sell

        success, self.simplino.sell_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                           "Sell",
                                                                           sell_price,
                                                                           sell_qty)

    def sell_order_filled(self, order_info):
        self.simplino.nb_sells += 1
        qty = float(order_info["info"]["executedQty"])
        price = float(order_info["info"]["price"])
        self.simplino.buy_qty -= qty

        fee_rate = self.api.exchange.markets[self.simplino.pair]['maker']

        self.simplino.invested += (1 - (fee_rate * MAKER_REFERAL_DISCOUNT)) * qty * price

        if self.api.cancel_order(self.simplino.buy_order_id, self.simplino.pair):
            self.simplino.nb_possible_sell = self.simplino.nb_buys - self.simplino.nb_sells

            buy_price = self.simplino.buyPrices[self.simplino.nb_possible_sell]
            buy_qty = self.simplino.buy_qtys[self.simplino.nb_possible_sell]

            success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                              "Buy",
                                                                              buy_price,
                                                                              buy_qty)
            if self.simplino.nb_possible_sell > 0:
                sell_price = self.simplino.sell_prices[self.simplino.nb_possible_sell - 1]
                sell_qty = self.simplino.buy_qty / self.simplino.nb_possible_sell

                success, self.simplino.sell_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                   "Sell",
                                                                                   sell_price,
                                                                                   sell_qty)
            else:
                self.simplino.sell_order_id = 0  # NULL order ID so don't get fill checked

    def create_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(self.simplino.buyPrices) + 1)
        self.ui.tableWidget.setColumnCount(4)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Buy Price"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Buy Qty"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("Cumulate"))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem("Cumulative max"))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Sell Price"))
        cumulate = 0
        cumulate_max = 0

        for i in range(1, len(self.simplino.buyPrices) + 1):
            cumulate_max += i * self.simplino.buy_qtys[i - 1] * self.simplino.buyPrices[i - 1]
            cumulate += self.simplino.buy_qtys[i - 1] * self.simplino.buyPrices[i - 1]

            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem((str(round(self.simplino.buyPrices[i - 1], 5)))))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem((str(round(self.simplino.buy_qtys[i - 1], 5)))))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem((str(round(cumulate, 5)))))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem((str(round(cumulate_max, 5)))))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem((str(round(self.simplino.sell_prices[i - 1], 5)))))

    def set_pair_label(self):
        self.ui.price_pairing_label.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_2.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_3.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_4.setText(self.simplino.sell_asset)
        self.ui.Pairing_label.setText(self.simplino.pair)
        self.ui.sell_asset_label.setText(self.simplino.sell_asset)
        self.ui.sell_asset_label_2.setText(self.simplino.sell_asset)
        self.ui.Buy_asset_label.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_2.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_3.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_4.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_5.setText(self.simplino.buy_asset)

    def add_filled_order_in_tab(self, order_info):
        row = self.simplino.nb_buys + self.simplino.nb_sells
        self.ui.Order_filled_tab.setRowCount(row + 1)
        self.ui.Order_filled_tab.setItem(row, 0, QTableWidgetItem((str(order_info["info"]["orderId"]))))
        self.ui.Order_filled_tab.setItem(row, 1, QTableWidgetItem((order_info["info"]["side"])))
        self.ui.Order_filled_tab.setItem(row, 2, QTableWidgetItem((order_info["info"]["executedQty"])))
        self.ui.Order_filled_tab.setItem(row, 3, QTableWidgetItem((order_info["info"]["price"])))
        self.ui.Order_filled_tab.setItem(row, 4, QTableWidgetItem((str(order_info["info"]["time"]))))

    def on_mount(self, api):
        for symbol in api.exchange.markets:
            self.ui.pair_comboBox.addItem(symbol)

        self.ui.Order_filled_tab.setRowCount(1)
        self.ui.Order_filled_tab.setColumnCount(5)

        self.ui.Order_filled_tab.setItem(0, 0, QTableWidgetItem("Order ID"))
        self.ui.Order_filled_tab.setItem(0, 1, QTableWidgetItem("Side"))
        self.ui.Order_filled_tab.setItem(0, 2, QTableWidgetItem("Qty"))
        self.ui.Order_filled_tab.setItem(0, 3, QTableWidgetItem("Price"))
        self.ui.Order_filled_tab.setItem(0, 4, QTableWidgetItem("Time"))

        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(4)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Buy Price"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Buy Qty"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("Cumulative"))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem("Cumulative max"))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Sell Price"))

    def update_visual(self, order_book, buy_filled, sell_filled, buy_order, sell_order):
        print(order_book['bids'][0])
        bid_price = float(order_book['bids'][0][0])
        ask_price = float(order_book['asks'][0][0])
        # we assume that price equal mean between bids and ask price (dont need to call the api again)
        current_price = (bid_price + ask_price) / 2

        self.ui.price_label.setText(str(round(current_price, 2)))  # TODO get rid of hardcode
        self.ui.ask_price_label.setText(str(round(ask_price, 2)))  # TODO get rid of hardcode
        self.ui.bid_price_label.setText(str(round(bid_price, 2)))  # TODO get rid of hardcode

        # calculate profit if selling all at bid price (to be sure that its get filled)
        fee_rate = self.api.exchange.markets[self.simplino.pair]['maker']
        sell_profits = self.simplino.invested + (
                1 - fee_rate * MAKER_REFERAL_DISCOUNT) * bid_price * self.simplino.buy_qty

        self.ui.gain_label.setText(str(round(sell_profits, 2)))  # TODO get rid of hardcode

        if buy_filled:
            self.add_filled_order_in_tab(buy_order)
            self.ui.Buy_order_filled_label.setText(str(self.simplino.nb_buys))
            self.ui.Possible_sell.setText(str(self.simplino.nb_possible_sell))
            self.ui.Buy_Qty_label.setText(str(round(self.simplino.buy_qty, 5)))  # TODO get rid of hardcode
            self.ui.invested_label.setText(str(round(self.simplino.invested, 2)))  # TODO get rid of hardcode
            self.ui.Buy_order_ID_label.setText(str(self.simplino.buy_order_id))

        if sell_filled:
            self.add_filled_order_in_tab(sell_order)
            self.ui.Sell_order_filled_label.setText(str(self.simplino.nb_sells))
            self.ui.Possible_sell.setText(str(self.simplino.nb_possible_sell))
            self.ui.Sell_order_ID_label.setText(str(self.simplino.sell_order_id))

        self.ui.buy_qty_label.setText(buy_order["info"]['origQty'])
        self.ui.buy_filled_Qty_label.setText(buy_order["info"]["executedQty"])

        if sell_order is not None:
            self.ui.sell_qty_label.setText(sell_order["info"]['origQty'])
            self.ui.sell_filled_Qty_label.setText(sell_order["info"]["executedQty"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    #QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = TopSimplino()
    sys.exit(app.exec_())
