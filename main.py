from PyQt5.QtWidgets import QMdiArea, QMainWindow, QGridLayout, QVBoxLayout, QTabWidget, QApplication
from PyQt5 import QtWidgets
import logging

from api import API



from ui_main import Ui_MainWindow

class top(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api = API("binance")   # Create and instance that can communicate with an exchange
        self.list_pair(self.api)
        self.list_open_order(self.api)

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