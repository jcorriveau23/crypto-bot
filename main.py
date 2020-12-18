from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMdiArea, QMainWindow, QGridLayout, QVBoxLayout, QTabWidget, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets
import logging
import threading
import time

from api import API
from Algos import Simplino

from ui_main import Ui_MainWindow

MAKER_REFERAL_DISCOUNT = 0.6

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("log_file.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class TopSimplino(QMainWindow):
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
        '''
        Button trigger the calculation of Simplino buy sell prevision and store it in the ui tab
        :return:
        '''

        start_price = float(self.ui.start_price_text_input.text())
        nb_buy = int(self.ui.nb_buy_text_input.text())
        drop_percent = float(self.ui.drop_poucent_text_input.text())
        pair = self.ui.pair_comboBox.currentText()
        more_percent = float(self.ui.percent_more_buy_label.text())

        self.simplino = Simplino(pair)

        info = self.api.exchange.fetch_balance()
        balances = info['info']['balances']

        balance = 0
        for asset in balances:  # fetch the balance of the pairing asset. Selling side
            if asset['asset'] == self.simplino.sell_asset:
                balance = float(asset['free'])

        self.simplino.simplino_algo_create_buys(balance, start_price, drop_percent / 100, nb_buy, more_percent)

        self.create_table()
        self.set_pair_label()

    def btn_start(self):
        '''
        Button that start the thread for simplino strategy
        You can restart a previous stopped run
        :return:
        '''
        if self.simplino.ready:  # if buy and sell price ready
            if not self.running:

                if self.simplino.buy_order_id == 0:  # New run started
                    success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                      "Buy",
                                                                                      self.simplino.buyPrices[0],
                                                                                      self.simplino.buy_qtys[0])
                    self.ui.tableWidget.item(1, 0).setBackground(QColor(0, 180, 0))
                    self.ui.tableWidget.item(1, 1).setBackground(QColor(0, 180, 0))
                else:  # restart the previous run
                    logger.info("Restart the previous run")
                    success = True

                if success:
                    logger.info("Simplino start")
                    self.ui.start_time_label.setText(str(time.time()))
                    logger.info("Starting thread for simplino")
                    self.running = True
                    self.thread_simplino = threading.Thread(target=self.main_simplino)
                    self.thread_simplino.start()

                    return True

                else:
                    logger.error("Could not start simplino")
                    return False

            else:
                logger.error("Simplino already running")
                return False

        else:
            logger.error("Simplino context not set")
            return False

    def btn_stop(self):
        '''
        kill the simplino thread strategy
        :return:
        '''
        if self.running:
            self.thread_simplino_kill = True
            self.thread_simplino.join()
            self.thread_simplino_kill = False
            self.running = False
            logger.debug("thread KILLED")
        else:
            logger.info("Simplino is not running")

    def main_simplino(self):
        '''
        main loop of the simplino strategy. This loop is run in its own thread
        :return:
        '''
        while True:
            if self.thread_simplino_kill:
                return

            order_book = self.api.exchange.fetch_order_book(self.simplino.pair)

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

            self.update_visual(order_book, buy_filled, sell_filled, buy_order_info, sell_order_info)

            time.sleep(1)  # exchange polling rate

    def buy_order_filled(self, order_info):
        '''
        call when a buy order is filled, cancel current sell order and resend a buy + sell order depending on
        the context
        :param order_info: JSON from api that contain the filled order info
        :return:
        '''
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
            logger.info("no active sell order")

        if self.simplino.nb_possible_sell < self.simplino.nb_buy_depth:
            buy_price = self.simplino.buyPrices[self.simplino.nb_possible_sell]
            buy_qty = self.simplino.buy_qtys[self.simplino.nb_possible_sell]

            success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                              "Buy",
                                                                              buy_price,
                                                                              buy_qty)
            # TODO use the success to retrigger another try if not success
        else:
            logger.info("Buy depth reached cant buy more!")

        # Always can sell after a buy order is filled
        sell_price = self.simplino.sell_prices[self.simplino.nb_possible_sell - 1]
        sell_qty = self.simplino.buy_qty / self.simplino.nb_possible_sell

        success, self.simplino.sell_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                           "Sell",
                                                                           sell_price,
                                                                           sell_qty)
        # TODO use the success to retrigger another try if not success

    def sell_order_filled(self, order_info):
        '''
        call when a sell order is filled, cancel current buy order and resend buy + sell order depending on the context
        :param order_info: JSON from api that contain the filled order info
        :return:
        '''
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
            # TODO use the success to retrigger another try if not success
            if self.simplino.nb_possible_sell > 0:
                sell_price = self.simplino.sell_prices[self.simplino.nb_possible_sell - 1]
                sell_qty = self.simplino.buy_qty / self.simplino.nb_possible_sell

                success, self.simplino.sell_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                   "Sell",
                                                                                   sell_price,
                                                                                   sell_qty)
                # TODO use the success to retrigger another try if not success
            else:
                self.simplino.sell_order_id = 0  # NULL order ID so don't get fill checked

    def create_table(self):
        '''
        generate simplino calculation table
        :return:
        '''
        self.ui.start_price_label.setText(str(round(self.simplino.start_price, 2)))  # TODO get rid of hardcode
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(self.simplino.buyPrices) + 1)
        self.ui.tableWidget.setColumnCount(5)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Buy Price"))
        self.ui.tableWidget.item(0, 0).setBackground(QColor(200, 200, 200))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Buy Qty"))
        self.ui.tableWidget.item(0, 1).setBackground(QColor(200, 200, 200))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("Cumulate"))
        self.ui.tableWidget.item(0, 2).setBackground(QColor(200, 200, 200))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem("Cumulative max"))
        self.ui.tableWidget.item(0, 3).setBackground(QColor(200, 200, 200))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Sell Price"))
        self.ui.tableWidget.item(0, 4).setBackground(QColor(200, 200, 200))

        cumulative = 0

        for i in range(1, len(self.simplino.buyPrices) + 1):
            cumulative_max = i * self.simplino.buy_qtys[i - 1] * self.simplino.buyPrices[i - 1]
            cumulative += self.simplino.buy_qtys[i - 1] * self.simplino.buyPrices[i - 1]

            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem((str(round(self.simplino.buyPrices[i - 1], 5)))))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem((str(round(self.simplino.buy_qtys[i - 1], 5)))))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem((str(round(cumulative, 5)))))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem((str(round(cumulative_max, 5)))))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem((str(round(self.simplino.sell_prices[i - 1], 5)))))

    def set_pair_label(self):
        '''
        Set pair label depending on the paring chosen
        :return:
        '''
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
        '''
        Add the information of a filled order in the order filled ui tab
        :param order_info:
        :return:
        '''
        row = self.simplino.nb_buys + self.simplino.nb_sells
        self.ui.Order_filled_tab.setRowCount(row + 1)
        self.ui.Order_filled_tab.setItem(row, 0, QTableWidgetItem((str(order_info["info"]["orderId"]))))
        self.ui.Order_filled_tab.setItem(row, 1, QTableWidgetItem((order_info["info"]["side"])))
        self.ui.Order_filled_tab.setItem(row, 2, QTableWidgetItem((order_info["info"]["executedQty"])))
        self.ui.Order_filled_tab.setItem(row, 3, QTableWidgetItem((order_info["info"]["price"])))
        self.ui.Order_filled_tab.setItem(row, 4, QTableWidgetItem((str(order_info["info"]["time"]))))

    def on_mount(self, api):
        '''
        Call when app started, set tab title and combo box available pairs
        :param api:
        :return:
        '''
        for symbol in api.exchange.markets:
            self.ui.pair_comboBox.addItem(symbol)

        self.ui.Order_filled_tab.setRowCount(1)
        self.ui.Order_filled_tab.setColumnCount(5)

        self.ui.Order_filled_tab.setItem(0, 0, QTableWidgetItem("Order ID"))
        self.ui.Order_filled_tab.item(0, 0).setBackground(QColor(200, 200, 200))
        self.ui.Order_filled_tab.setItem(0, 1, QTableWidgetItem("Side"))
        self.ui.Order_filled_tab.item(0, 1).setBackground(QColor(200, 200, 200))
        self.ui.Order_filled_tab.setItem(0, 2, QTableWidgetItem("Qty"))
        self.ui.Order_filled_tab.item(0, 2).setBackground(QColor(200, 200, 200))
        self.ui.Order_filled_tab.setItem(0, 3, QTableWidgetItem("Price"))
        self.ui.Order_filled_tab.item(0, 3).setBackground(QColor(200, 200, 200))
        self.ui.Order_filled_tab.setItem(0, 4, QTableWidgetItem("Time"))
        self.ui.Order_filled_tab.item(0, 4).setBackground(QColor(200, 200, 200))

    def update_visual(self, order_book, buy_filled, sell_filled, buy_order, sell_order):
        '''
        general real time visual update functions. Called every period of filled order check.
        :param order_book: JSON from API of bid and ask price
        :param buy_filled: bool that tells us if the buy order is filled
        :param sell_filled: bool that tells us if the sell order is filled
        :param buy_order: JSON from API of buy order information
        :param sell_order: JSON from API of sell order information
        :return:
        '''

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

        if buy_filled or sell_filled:

            self.set_buy_sell_tab_color(self.simplino.nb_possible_sell, buy_filled)

            self.ui.Buy_order_filled_label.setText(str(self.simplino.nb_buys))
            self.ui.Sell_order_filled_label.setText(str(self.simplino.nb_sells))
            self.ui.Possible_sell.setText(str(self.simplino.nb_possible_sell))

            self.ui.Buy_Qty_label.setText(str(round(self.simplino.buy_qty, 5)))  # TODO get rid of hardcode
            self.ui.invested_label.setText(str(round(self.simplino.invested, 2)))  # TODO get rid of hardcode
            self.ui.Buy_order_ID_label.setText(str(self.simplino.buy_order_id))
            self.ui.Sell_order_ID_label.setText(str(self.simplino.sell_order_id))

            if sell_filled:
                self.add_filled_order_in_tab(sell_order)
            if buy_filled:
                self.add_filled_order_in_tab(buy_order)

        if buy_order is not None:
            self.ui.buy_qty_label.setText(buy_order["info"]['origQty'])
            self.ui.buy_filled_Qty_label.setText(buy_order["info"]["executedQty"])
            self.ui.buy_order_price_label.setText(buy_order["info"]["price"])

        if sell_order is not None:
            self.ui.sell_qty_label.setText(sell_order["info"]['origQty'])
            self.ui.sell_filled_Qty_label.setText(sell_order["info"]["executedQty"])
            self.ui.sell_order_price_label.setText(sell_order["info"]["price"])

    def set_buy_sell_tab_color(self, possible_sell, buy_filled):
        '''
        This function generate the logic for the color pointer in simplino context table. Help the use to understand
        Simplino

        :param possible_sell: variable of simplino database that tell us the number of possible sells
        :param buy_filled: bool that tells us if its a sell order that got filled or a buy order
        :return:
        '''
        if possible_sell == 0:

            self.ui.tableWidget.item(possible_sell + 2, 0).setBackground(QColor(255, 255, 255))     # Last
            self.ui.tableWidget.item(possible_sell + 2, 1).setBackground(QColor(255, 255, 255))
            self.ui.tableWidget.item(possible_sell + 1, 4).setBackground(QColor(255, 255, 255))

            self.ui.tableWidget.item(possible_sell + 1, 0).setBackground(QColor(0, 180, 0))             # New
            self.ui.tableWidget.item(possible_sell + 1, 1).setBackground(QColor(0, 180, 0))

        elif possible_sell == 1:
            if buy_filled: # No sell order
                self.ui.tableWidget.item(possible_sell, 0).setBackground(QColor(255, 255, 255)) # Last
                self.ui.tableWidget.item(possible_sell, 1).setBackground(QColor(255, 255, 255))
            else:
                self.ui.tableWidget.item(possible_sell + 2, 0).setBackground(QColor(255, 255, 255)) # Last
                self.ui.tableWidget.item(possible_sell + 2, 1).setBackground(QColor(255, 255, 255))
                self.ui.tableWidget.item(possible_sell + 1, 4).setBackground(QColor(255, 255, 255))

            self.ui.tableWidget.item(possible_sell + 1, 0).setBackground(QColor(0, 180, 0))             # New
            self.ui.tableWidget.item(possible_sell + 1, 1).setBackground(QColor(0, 180, 0))
            self.ui.tableWidget.item(possible_sell, 4).setBackground(QColor(180, 0, 0))

        else:
            if buy_filled:
                self.ui.tableWidget.item(possible_sell, 0).setBackground(QColor(255, 255, 255))  # Last
                self.ui.tableWidget.item(possible_sell, 1).setBackground(QColor(255, 255, 255))
                self.ui.tableWidget.item(possible_sell - 1, 4).setBackground(QColor(255, 255, 255))
            else:
                self.ui.tableWidget.item(possible_sell + 2, 0).setBackground(QColor(255, 255, 255))     #Last
                self.ui.tableWidget.item(possible_sell + 2, 1).setBackground(QColor(255, 255, 255))
                self.ui.tableWidget.item(possible_sell + 1, 4).setBackground(QColor(255, 255, 255))

            self.ui.tableWidget.item(possible_sell + 1, 0).setBackground(QColor(0, 180, 0))             # New
            self.ui.tableWidget.item(possible_sell + 1, 1).setBackground(QColor(0, 180, 0))
            self.ui.tableWidget.item(possible_sell, 4).setBackground(QColor(180, 0, 0))



if __name__ == "__main__":
    app = QApplication([])

    top = TopSimplino()
    top.show()

    app.exec_()
