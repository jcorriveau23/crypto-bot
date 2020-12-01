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

        self.api = API("Binance")   # Create and instance that can communicate with an exchange
        self.get_exchange_info(self.api)

    def get_exchange_info(self, api):
        for symbol in api.info["symbols"]:
            self.ui.pair_comboBox.addItem(symbol["symbol"])

if __name__ == "__main__":
    app = QApplication([])

    top = top()
    top.show()

    app.exec_()