from PyQt5.QtWidgets import QMdiArea, QMainWindow, QGridLayout, QVBoxLayout, QTabWidget, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets
import logging

from api import API
from Algos import Simplino


from ui_main import Ui_MainWindow

class top(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.calculate_button.clicked.connect(lambda: self.btn_calculate_simplino())

        self.api = API("binance")   # Create and instance that can communicate with an exchange
        self.simplino = Simplino()
        self.list_pair(self.api)
        self.list_open_order(self.api)


    def btn_calculate_simplino(self):
        start_price = float(self.ui.start_price_text_input.text())
        nb_buy = int(self.ui.nb_buy_text_input.text())
        drop_pourcent = float(self.ui.drop_poucent_text_input.text())
        pair = self.ui.pair_comboBox.currentText()

        trading_asset = pair.split('/')
        print(trading_asset[1])

        info = self.api.exchange.fetch_balance()
        balances = info['info']['balances']
        print(balances)
        for asset in balances:
            if asset['asset'] == trading_asset[1]:
                print(asset['free'])
                balance = float(asset['free'])

        self.simplino.simplino_algo_create_buys(balance, start_price, drop_pourcent/100, nb_buy, 1.08)  #TODO get rid
                                                                                                    # of hardcode

        self.create_table()

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



    def list_pair(self, api):
        for symbol in api.exchange.markets:
            self.ui.pair_comboBox.addItem(symbol)

    def list_open_order(self, api):
        orders = api.exchange.fetch_open_orders(symbol="ETH/USDT")
        i = 0
        for order in orders:
            print("Order {}: {}".format(i, order["info"]))
            i += 1




if __name__ == "__main__":
    app = QApplication([])

    top = top()
    top.show()

    app.exec_()