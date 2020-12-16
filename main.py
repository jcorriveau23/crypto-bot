from PyQt5.QtWidgets import QMdiArea, QMainWindow, QGridLayout, QVBoxLayout, QTabWidget, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets
import logging
import threading
import time
from api import API
from Algos import Simplino

from ui_main import Ui_MainWindow


class top(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
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

    def btn_calculate_simplino(self):

        start_price = float(self.ui.start_price_text_input.text())
        nb_buy = int(self.ui.nb_buy_text_input.text())
        drop_percent = float(self.ui.drop_poucent_text_input.text())
        pair = self.ui.pair_comboBox.currentText()

        self.simplino = Simplino(pair)

        info = self.api.exchange.fetch_balance()
        balances = info['info']['balances']

        for asset in balances:  # fetch the balance of the pairing asset. Selling side
            if asset['asset'] == self.simplino.sell_asset:
                balance = float(asset['free'])

        self.simplino.simplino_algo_create_buys(balance, start_price, drop_percent / 100, nb_buy, 1.08)  # TODO get rid
                                                                                                         # of hardcode

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
                    logging.info("Simplino start")
                    self.ui.start_time_label = time.time()
                    logging.debug("Starting thread for simplino")
                    self.thread_simplino = threading.Thread(target=self.main_simplino)
                    self.running = True
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
            logging.debug("thread KILLED")
        else:
            logging.info("Simplino is not running")

    def main_simplino(self):
        time.sleep(4)
        while True:
            filled, side, order_info = self.api.order_isfilled(self.simplino.pair,
                                                              self.simplino.buy_order_id,
                                                              self.simplino.sell_order_id)
            if filled:
                if side == "BUY":
                    self.buy_order_filled(order_info)
                elif side == "SELL":
                    self.sell_order_filled(order_info)


    def buy_order_filled(self, order_info):
        self.simplino.nb_buys += 1
        self.simplino.buy_qty += float(order_info["info"]["executedQty"])
        nb_possible_sell = self.simplino.nb_buys - self.simplino.nb_sells
        # TODO add filled order to tab with function  add_filled_order_in_tab
        if nb_possible_sell > 1:
            self.api.cancel_order(self.simplino.sell_order_id, self.simplino.pair)


            buy_price = self.simplino.buyPrices[nb_possible_sell]
            buy_qty = self.simplino.buy_qtys[nb_possible_sell]

            self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                     "Buy",
                                                                     buy_price,
                                                                     buy_qty)
            sell_price = self.simplino.sell_prices[nb_possible_sell - 1]
            sell_qty = self.simplino.buy_qty/nb_possible_sell

            self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                     "Sell",
                                                                     sell_price,
                                                                     sell_qty)


    def sell_order_filled(self, order_info):
        self.simplino.nb_sells += 1
        self.simplino.buy_qty -= float(order_info["info"]["executedQty"])
        #TODO add filled order to tab add_filled_order_in_tab
        if self.api.cancel_order(self.simplino.buy_order_id, self.simplino.pair):
            nb_possible_sell = self.simplino.nb_buys - self.simplino.nb_sells

            buy_price = self.simplino.buyPrices[nb_possible_sell]
            buy_qty = self.simplino.buy_qtys[nb_possible_sell]

            self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                     "Buy",
                                                                     buy_price,
                                                                     buy_qty)
            sell_price = self.simplino.sell_prices[nb_possible_sell - 1]
            sell_qty = self.simplino.buy_qty / nb_possible_sell

            self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                     "Sell",
                                                                     sell_price,
                                                                     sell_qty)

    def create_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(self.simplino.buyPrices) + 1)
        self.ui.tableWidget.setColumnCount(4)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(("Buy Price")))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(("Buy Qty")))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(("Sell Price")))

        for i in range(1, len(self.simplino.buyPrices) + 1):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem((str(round(self.simplino.buyPrices[i - 1], 5)))))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem((str(round(self.simplino.buy_qtys[i - 1], 5)))))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem((str(round(self.simplino.sell_prices[i - 1], 5)))))

    def set_pair_label(self):
        self.ui.price_pairing_label.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_2.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_3.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_4.setText(self.simplino.sell_asset)
        self.ui.Pairing_label.setText(self.simplino.pair)
        self.ui.sell_asset_label.setText(self.simplino.sell_asset)
        self.ui.Buy_asset_label.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_2.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_3.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_4.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_5.setText(self.simplino.buy_asset)

    def add_filled_order_in_tab(self, order_info):
        row = self.simplino.nb_buys + self.simplino.nb_sells
        self.ui.Order_filled_tab.setRowCount(row)
        self.ui.Order_filled_tab.setItem(0, 0, QTableWidgetItem((order_info["info"]["orderId"])))
        self.ui.Order_filled_tab.setItem(0, 1, QTableWidgetItem(())) #TODO need right keys
        self.ui.Order_filled_tab.setItem(0, 2, QTableWidgetItem(("Qty"))) #TODO need right keys
        self.ui.Order_filled_tab.setItem(0, 3, QTableWidgetItem(("Time")))#TODO need right keys


    def on_mount(self, api):
        for symbol in api.exchange.markets:
            self.ui.pair_comboBox.addItem(symbol)

        self.ui.Order_filled_tab.setRowCount(1)
        self.ui.Order_filled_tab.setColumnCount(4)

        self.ui.Order_filled_tab.setItem(0, 0, QTableWidgetItem(("order ID")))
        self.ui.Order_filled_tab.setItem(0, 1, QTableWidgetItem(("Side")))
        self.ui.Order_filled_tab.setItem(0, 2, QTableWidgetItem(("Qty")))
        self.ui.Order_filled_tab.setItem(0, 3, QTableWidgetItem(("Time")))

if __name__ == "__main__":
    app = QApplication([])

    top = top()
    top.show()

    app.exec_()


