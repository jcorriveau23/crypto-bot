from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5 import QtWidgets
import logging
import threading
import time
import json

from api import API
from Algos import Simplino

from ui_main import Ui_MainWindow

MAKER_REFERRAL_DISCOUNT = 0.6

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("log_file.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

gray = QColor(200, 200, 200)
red = QColor(200, 120, 120)
green = QColor(120, 200, 120)
white = QColor(255, 255, 255)


class TopSimplino(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.available_exchange()

        self.ui.calculate_button.clicked.connect(lambda: self.btn_calculate_simplino())
        self.ui.start_button.clicked.connect(lambda: self.btn_start())
        self.ui.stop_button.clicked.connect(lambda: self.btn_stop())
        self.ui.load_run_button.clicked.connect(lambda: self.btn_load_simplino_persistent_storage())
        self.ui.exchange_comboBox.currentTextChanged.connect(lambda: self.update_available_pair())

        self.simplino = None

        self.thread_simplino = None
        self.thread_simplino_kill = False
        self.running = False

        self.update_available_pair()

    def btn_calculate_simplino(self):
        """
        Button trigger the calculation of Simplino buy sell prevision and store it in the ui tab
        :return:
        """
        if not self.running:
            pair = self.ui.pair_comboBox.currentText()

            # input parameters handler
            success_text, trading_qty, start_price, nb_buy, drop_percent, more_percent = self.text_input_handler()

            if success_text:
                self.simplino = Simplino(pair)

                # get account asset balance
                success_balance, balance = self.api.get_asset_balance(self.simplino.sell_asset)

                if success_balance:
                    if trading_qty < balance:

                        # create simplino context
                        self.simplino.simplino_algo_create_buys(trading_qty, start_price, drop_percent / 100, nb_buy,
                                                                more_percent / 100)

                        self.create_table()
                        self.set_pair_label()

                        self.simplino.buy_order_id = 0
                        self.simplino.sell_order_id = 0
                        return True

                    else:
                        print(f"not enough balance => Trading qty: {trading_qty}, balance: {balance}")
                        return False

                else:
                    print("Could not get balance info")
                    return False
            else:
                print("text input check not valid")
                return False
        else:
            print("can't calculate when Simplino is running")
            return False

    def btn_start(self):
        """
        Button that start the thread for simplino strategy
        You can restart a previous stopped run
        :return:
        """
        if self.simplino.ready:  # if buy and sell price ready
            if not self.running:
                if self.simplino.buy_order_id == 0:  # New run started
                    success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                      "Buy",
                                                                                      self.simplino.buy_prices[0],
                                                                                      self.simplino.buy_qtys[0])
                    if success:
                        self.ui.tableWidget.item(1, 0).setBackground(green)
                        self.ui.tableWidget.item(1, 1).setBackground(green)

                else:  # restart the previous run
                    logger.info("Restart the previous run")
                    success = True

                if success:
                    logger.info("Simplino start")
                    self.ui.start_time_label.setText(str(time.time())) # TODO display the time in date-time short time format.

                    # Create and start the thread.
                    self.thread_simplino = MainThread(self.api, self.simplino)
                    self.thread_simplino.start()
                    self.thread_simplino.update_visual_signal.connect(self.update_visual)

                    self.ui.simplino_parameters_group.setEnabled(False)
                    logger.info("Starting thread for simplino")

                    self.running = True
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
        """
        kill the simplino thread strategy
        :return:
        """
        if self.running:
            self.thread_simplino.stop()
            self.running = False
            logger.debug("thread KILLED")
            self.ui.simplino_parameters_group.setEnabled(True)
        else:
            logger.info("Simplino is not running")

    def create_table(self):
        """
        generate simplino calculation table

        :return:
        """
        price_precision = self.api.exchange.markets[self.simplino.pair]['precision']['price']
        qty_precision = self.api.exchange.markets[self.simplino.pair]['precision']['amount']

        print("Price: " + str(price_precision))

        self.ui.start_price_label.setText(str(round(self.simplino.start_price, price_precision)))
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(self.simplino.buy_prices) + 1)
        self.ui.tableWidget.setColumnCount(5)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Buy Price"))
        self.ui.tableWidget.item(0, 0).setBackground(gray)
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("Buy Qty"))
        self.ui.tableWidget.item(0, 1).setBackground(gray)
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("Cumulate"))
        self.ui.tableWidget.item(0, 2).setBackground(gray)
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem("Cumulative max"))
        self.ui.tableWidget.item(0, 3).setBackground(gray)
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem("Sell Price"))
        self.ui.tableWidget.item(0, 4).setBackground(gray)

        cumulative = 0

        for i in range(1, len(self.simplino.buy_prices) + 1):
            cumulative_max = i * self.simplino.buy_qtys[i - 1] * self.simplino.buy_prices[i - 1]
            cumulative += self.simplino.buy_qtys[i - 1] * self.simplino.buy_prices[i - 1]

            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem((str(round(self.simplino.buy_prices[i - 1],
                                                                          price_precision)))))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem((str(round(self.simplino.buy_qtys[i - 1],
                                                                          qty_precision)))))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem((str(round(cumulative, price_precision)))))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem((str(round(cumulative_max, price_precision)))))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem((str(round(self.simplino.sell_prices[i - 1],
                                                                          price_precision)))))

    def set_pair_label(self):
        """
        Set pair label depending on the paring chosen

        :return:
        """
        self.ui.price_pairing_label.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_2.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_3.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_4.setText(self.simplino.sell_asset)
        self.ui.price_pairing_label_5.setText(self.simplino.sell_asset)
        self.ui.Pairing_label.setText(self.simplino.pair)
        self.ui.sell_asset_label.setText(self.simplino.sell_asset)
        self.ui.sell_asset_label_2.setText(self.simplino.sell_asset)
        self.ui.Buy_asset_label.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_2.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_3.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_4.setText(self.simplino.buy_asset)
        self.ui.Buy_asset_label_5.setText(self.simplino.buy_asset)

    def add_filled_order_in_tab(self, order_info):
        """
        Add the information of a filled order in the order filled ui tab

        :param order_info:
        :return:
        """
        row = self.simplino.nb_buys + self.simplino.nb_sells
        self.ui.Order_filled_tab.setRowCount(row + 1)
        self.ui.Order_filled_tab.setItem(row, 0, QTableWidgetItem((str(order_info["info"]["orderId"]))))
        self.ui.Order_filled_tab.setItem(row, 1, QTableWidgetItem((order_info["info"]["side"])))
        self.ui.Order_filled_tab.setItem(row, 2, QTableWidgetItem((order_info["info"]["executedQty"])))
        self.ui.Order_filled_tab.setItem(row, 3, QTableWidgetItem((order_info["info"]["price"])))
        self.ui.Order_filled_tab.setItem(row, 4, QTableWidgetItem((str(order_info["info"]["time"]))))

    def text_input_handler(self):
        """
        validate all 4 input for Simplino parameters. they need to be valid for a great simplino price and quantity
        calculation

        :return:
        """
        trading_qty = self.ui.trading_qty_text_input.text()
        start_price = self.ui.start_price_text_input.text()
        nb_buy = self.ui.nb_buy_text_input.text()
        drop_percent = self.ui.drop_poucent_text_input.text()
        more_percent = self.ui.percent_more_buy_label.text()

        if self.is_number(trading_qty):
            trading_qty = float(trading_qty)
            if trading_qty > 0:
                pass
            else:
                print("trading_qty: {}, is not a positive number".format(trading_qty))
                return False, None, None, None, None, None
        else:
            print("trading_qty: {}, input is not numeric".format(trading_qty))
            return False, None, None, None, None, None

        if self.is_number(start_price):
            start_price = float(start_price)
            if start_price > 0:
                pass
            else:
                print("price: {}, is not a positive number".format(start_price))
                return False, None, None, None, None, None
        else:
            print("price: {}, input is not numeric".format(start_price))
            return False, None, None, None, None, None

        if self.is_number(nb_buy):
            nb_buy = int(nb_buy)
            if nb_buy > 0:
                pass
            else:
                print("nb_buy: {}, is not a positive number".format(nb_buy))
                return False, None, None, None, None, None
        else:
            print("nb_buy: {}, input is not numeric".format(nb_buy))
            return False, None, None, None, None, None

        if self.is_number(drop_percent):
            drop_percent = float(drop_percent)
            if 0 < drop_percent < 100:
                pass
            else:
                print("drop_percent: {}, is not a valid percentage".format(drop_percent))
                return False, None, None, None, None, None
        else:
            print("drop_percent: {}, is not numeric".format(drop_percent))
            return False, None, None, None, None, None

        if self.is_number(more_percent):
            more_percent = float(more_percent)
            if 0 < more_percent < 100:
                pass
            else:
                print("more_percent: {}, is not a valid percentage".format(more_percent))
                return False, None, None, None, None, None
        else:
            print("drop_percent: {}, is not numeric".format(drop_percent))
            return False, None, None, None, None, None

        return True, trading_qty, start_price, nb_buy, drop_percent, more_percent

    def update_available_pair(self):
        """
        Call when app started, set tab title and combo box available pairs

        :param api:
        :return:
        """
        self.ui.pair_comboBox.clear()
        self.api = API(self.ui.exchange_comboBox.currentText())  # Default api is first of drop box

        for symbol in self.api.exchange.markets:
            self.ui.pair_comboBox.addItem(symbol)

        self.ui.Order_filled_tab.setRowCount(1)
        self.ui.Order_filled_tab.setColumnCount(5)

        self.ui.Order_filled_tab.setItem(0, 0, QTableWidgetItem("Order ID"))
        self.ui.Order_filled_tab.item(0, 0).setBackground(gray)
        self.ui.Order_filled_tab.setItem(0, 1, QTableWidgetItem("Side"))
        self.ui.Order_filled_tab.item(0, 1).setBackground(gray)
        self.ui.Order_filled_tab.setItem(0, 2, QTableWidgetItem("Qty"))
        self.ui.Order_filled_tab.item(0, 2).setBackground(gray)
        self.ui.Order_filled_tab.setItem(0, 3, QTableWidgetItem("Price"))
        self.ui.Order_filled_tab.item(0, 3).setBackground(gray)
        self.ui.Order_filled_tab.setItem(0, 4, QTableWidgetItem("Time"))
        self.ui.Order_filled_tab.item(0, 4).setBackground(gray)

    def available_exchange(self):
        """
        Called when apps boots and add available exchange on drop box

        Only available exchange is binance for now
        :return:
        """

        self.ui.exchange_comboBox.addItem("binance")
        self.ui.exchange_comboBox.addItem("Loopring")


    def update_visual(self, bid_price, ask_price, current_price, buy_filled, sell_filled, buy_order, sell_order):
        """
        general real time visual update functions. Called every period of filled order check.

        :param bid_price:
        :param ask_price:
        :param current_price:
        :param buy_filled: bool that tells us if the buy order is filled
        :param sell_filled: bool that tells us if the sell order is filled
        :param buy_order: JSON from API of buy order information
        :param sell_order: JSON from API of sell order information
        :return:
        """
        price_precision = self.api.exchange.markets[self.simplino.pair]['precision']['price']
        qty_precision = self.api.exchange.markets[self.simplino.pair]['precision']['amount']
        if qty_precision > 4:
            qty_precision = 4


        self.ui.price_label.setText(str(round(current_price, price_precision)))
        self.ui.ask_price_label.setText(str(round(ask_price, price_precision)))
        self.ui.bid_price_label.setText(str(round(bid_price, price_precision)))

        # calculate profit if selling all at bid price (to be sure that its get filled)
        fee_rate = self.api.exchange.markets[self.simplino.pair]['maker']
        sell_profits = self.simplino.invested + (
                1 - fee_rate * MAKER_REFERRAL_DISCOUNT) * bid_price * self.simplino.buy_qty

        self.ui.gain_label.setText(str(round(sell_profits, price_precision)))

        if buy_filled or sell_filled:

            self.set_buy_sell_tab_color(self.simplino.nb_possible_sell, buy_filled)

            self.ui.Buy_order_filled_label.setText(str(self.simplino.nb_buys))
            self.ui.Sell_order_filled_label.setText(str(self.simplino.nb_sells))
            self.ui.Possible_sell.setText(str(self.simplino.nb_possible_sell))

            self.ui.Buy_Qty_label.setText(str(round(self.simplino.buy_qty, qty_precision)))
            self.ui.invested_label.setText(str(round(self.simplino.invested, price_precision)))
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
            if self.simplino.sell_order_id == 0:
                self.ui.sell_qty_label.setText(" - ")
                self.ui.sell_filled_Qty_label.setText(" - ")
                self.ui.sell_order_price_label.setText(" - ")
            else:
                self.ui.sell_qty_label.setText(sell_order["info"]['origQty'])
                self.ui.sell_filled_Qty_label.setText(sell_order["info"]["executedQty"])
                self.ui.sell_order_price_label.setText(sell_order["info"]["price"])

    def set_buy_sell_tab_color(self, possible_sell, buy_filled):
        """
        This function generate the logic for the color pointer in simplino context table. Help the use to understand
        Simplino

        :param possible_sell: variable of simplino database that tell us the number of possible sells
        :param buy_filled: bool that tells us if its a sell order that got filled or a buy order
        :return:
        """
        if possible_sell == 0:

            self.ui.tableWidget.item(possible_sell + 2, 0).setBackground(white)  # Last
            self.ui.tableWidget.item(possible_sell + 2, 1).setBackground(white)
            self.ui.tableWidget.item(possible_sell + 1, 4).setBackground(white)

            self.ui.tableWidget.item(possible_sell + 1, 0).setBackground(green)  # New
            self.ui.tableWidget.item(possible_sell + 1, 1).setBackground(green)

        elif possible_sell == 1:
            if buy_filled:  # No sell order
                self.ui.tableWidget.item(possible_sell, 0).setBackground(white)  # Last
                self.ui.tableWidget.item(possible_sell, 1).setBackground(white)
            else:
                self.ui.tableWidget.item(possible_sell + 2, 0).setBackground(white)  # Last
                self.ui.tableWidget.item(possible_sell + 2, 1).setBackground(white)
                self.ui.tableWidget.item(possible_sell + 1, 4).setBackground(white)

            self.ui.tableWidget.item(possible_sell + 1, 0).setBackground(green)  # New
            self.ui.tableWidget.item(possible_sell + 1, 1).setBackground(green)
            self.ui.tableWidget.item(possible_sell, 4).setBackground(red)

        elif possible_sell == self.simplino.nb_buy_depth:
            self.ui.tableWidget.item(possible_sell, 0).setBackground(white)  # Last
            self.ui.tableWidget.item(possible_sell, 1).setBackground(white)
            self.ui.tableWidget.item(possible_sell - 1, 4).setBackground(white)

            self.ui.tableWidget.item(possible_sell, 4).setBackground(red)  # New

        else:
            if buy_filled:
                self.ui.tableWidget.item(possible_sell, 0).setBackground(white)  # Last
                self.ui.tableWidget.item(possible_sell, 1).setBackground(white)
                self.ui.tableWidget.item(possible_sell - 1, 4).setBackground(white)
            else:
                self.ui.tableWidget.item(possible_sell + 2, 0).setBackground(white)  # Last
                self.ui.tableWidget.item(possible_sell + 2, 1).setBackground(white)
                self.ui.tableWidget.item(possible_sell + 1, 4).setBackground(white)

            self.ui.tableWidget.item(possible_sell + 1, 0).setBackground(green)  # New
            self.ui.tableWidget.item(possible_sell + 1, 1).setBackground(green)
            self.ui.tableWidget.item(possible_sell, 4).setBackground(red)



    def btn_load_simplino_persistent_storage(self):
        """
        when the load run button is pressed, this function is called to load the json from "run.json file.
        a new simplino object is being created

        Simplino must not be running.

        :return:
        """
        if not self.running:
            f = open('run.json')  # TODO get rid of hardcode, can load any json file
            data = json.load(f)

            self.simplino = Simplino(data['pair'])

            self.simplino.pair = data['pair']
            self.simplino.buy_asset = data['buy_asset']
            self.simplino.sell_asset = data['sell_asset']
            self.simplino.buy_qtys = data['buy_qtys']
            self.simplino.buy_prices = data['buy_prices']
            self.simplino.sell_prices = data['sell_prices']
            self.simplino.nb_buy_depth = data['nb_buy_depth']
            self.simplino.nb_sells = data['nb_sells']

            self.simplino.nb_buys = data['nb_buys']
            self.simplino.nb_possible_sell = data['nb_possible_sell']
            self.simplino.buy_qty = data['buy_qty']
            self.simplino.invested = data['invested']
            self.simplino.buy_order_id = data['buy_order_id']
            self.simplino.sell_order_id = data['sell_order_id']
            self.simplino.start_price = data['start_price']
            self.simplino.ready = data['ready']

            buy_filled, buy_order_info = self.api.order_isfilled(self.simplino.pair,
                                                                 self.simplino.buy_order_id)
            print(buy_filled)

            if buy_filled:
                buy_price = self.simplino.buy_prices[self.simplino.nb_possible_sell]
                buy_qty = self.simplino.buy_qtys[self.simplino.nb_possible_sell]
                success, self.simplino.buy_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                  "Buy",
                                                                                  buy_price,
                                                                                  buy_qty)
                print("Buy Resent")

            sell_filled, sell_order_info = self.api.order_isfilled(self.simplino.pair,
                                                                   self.simplino.sell_order_id)
            if sell_filled:
                sell_price = self.simplino.sell_prices[self.simplino.nb_possible_sell - 1]
                sell_qty = self.simplino.buy_qty / self.simplino.nb_possible_sell
                success, self.simplino.sell_order_id = self.api.create_limit_order(self.simplino.pair,
                                                                                   "Sell",
                                                                                   sell_price,
                                                                                   sell_qty)
                print("Sell Resent")

            self.create_table()
            self.set_pair_label()
            logger.info('last run loaded !')
        else:
            logger.error('App is currently running')

    def is_number(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False


class MainThread(QThread):
    update_visual_signal = pyqtSignal(float, float, float, object, object, object, object)

    def __init__(self, api, simplino):
        super().__init__()
        self.api = api
        self.simplino = simplino

        #self.main_simplino()

    def run(self):
        """
        main loop of the simplino strategy. This loop is run in its own thread

        :return:
        """
        while True:

            success, order_book = self.api.get_order_book(self.simplino.pair)

            if success:

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

                bid_price = float(order_book['bids'][0][0])
                ask_price = float(order_book['asks'][0][0])
                # we assume that price equal mean between bids and ask price (dont need to call the api again)
                current_price = (bid_price + ask_price) / 2

                # TODO send by thread signal
                self.update_visual_signal.emit(bid_price, ask_price, current_price, buy_filled, sell_filled,
                                               buy_order_info, sell_order_info)

            time.sleep(2)  # exchange polling rate

    def buy_order_filled(self, order_info):
        """
        call when a buy order is filled, cancel current sell order and resend a buy + sell order depending on
        the context

        :param order_info: JSON from api that contain the filled order info
        :return:
        """
        self.simplino.nb_buys += 1
        qty = float(order_info["info"]["executedQty"])
        price = float(order_info["info"]["price"])
        self.simplino.buy_qty += qty
        self.simplino.nb_possible_sell = self.simplino.nb_buys - self.simplino.nb_sells

        fee_rate = self.api.exchange.markets[self.simplino.pair]['maker']

        self.simplino.invested -= (1 + (fee_rate * MAKER_REFERRAL_DISCOUNT)) * qty * price

        if self.simplino.nb_possible_sell > 1:  # a sell order is open?
            self.api.cancel_order(self.simplino.sell_order_id, self.simplino.pair)
        else:
            logger.info("no active sell order")

        if self.simplino.nb_possible_sell < self.simplino.nb_buy_depth:
            buy_price = self.simplino.buy_prices[self.simplino.nb_possible_sell]
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

        self.update_simplino_persistent_storage()  # store the information of the current run

    def sell_order_filled(self, order_info):
        """
        call when a sell order is filled, cancel current buy order and resend buy + sell order depending on the context

        :param order_info: JSON from api that contain the filled order info
        :return:
        """
        self.simplino.nb_sells += 1
        qty = float(order_info["info"]["executedQty"])
        price = float(order_info["info"]["price"])
        self.simplino.buy_qty -= qty

        fee_rate = self.api.exchange.markets[self.simplino.pair]['maker']

        self.simplino.invested += (1 - (fee_rate * MAKER_REFERRAL_DISCOUNT)) * qty * price

        if self.api.cancel_order(self.simplino.buy_order_id, self.simplino.pair):
            self.simplino.nb_possible_sell = self.simplino.nb_buys - self.simplino.nb_sells

            buy_price = self.simplino.buy_prices[self.simplino.nb_possible_sell]
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

        self.update_simplino_persistent_storage()  # store the information of the current run

    def update_simplino_persistent_storage(self):
        """
        Each time a buy or sell order is filled in a simplino run, this functions is called for persistant storage
        The simplino data is stored in a file called "run.json"

        :return:
        """
        data = {'pair': self.simplino.pair, 'buy_asset': self.simplino.buy_asset,
                'sell_asset': self.simplino.sell_asset, 'buy_qtys': self.simplino.buy_qtys,
                'buy_prices': self.simplino.buy_prices, 'sell_prices': self.simplino.sell_prices,
                'nb_buy_depth': self.simplino.nb_buy_depth, 'nb_sells': self.simplino.nb_sells,
                'nb_buys': self.simplino.nb_buys, 'nb_possible_sell': self.simplino.nb_possible_sell,
                'buy_qty': self.simplino.buy_qty, 'invested': self.simplino.invested,
                'buy_order_id': self.simplino.buy_order_id, 'sell_order_id': self.simplino.sell_order_id,
                'start_price': self.simplino.start_price, 'ready': self.simplino.ready}

        with open('run.json', 'w') as f:
            json.dump(data, f)


if __name__ == "__main__":
    app = QApplication([])

    top = TopSimplino()
    top.show()

    app.exec_()
