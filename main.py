

from app_modules import *

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from api import API


class MainWindow(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api = API("Binance")   # Create and instance that can communicate with an exchange

        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        ########################################################################
        # Window attribute
        ########################################################################

        # Remove standard title bar
        UIFunctions.remove_title_bar(True)

        # Window tittle
        self.setWindowTitle('Binance Bot - Cryptocurrency Exchangee')
        UIFunctions.label_title(self, 'Home')
        UIFunctions.label_description(self, 'Set text')

        # Window size
        start_size = QSize(1280, 720)
        self.resize(start_size)
        self.setMinimumSize(start_size)

        ########################################################################
        # Create menus
        ########################################################################

        self.drag_pos = None

        # btn event
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggle_menu(self, 220, True))
        self.ui.btn_wallet_refresh.clicked.connect(lambda: WalletFrontEnd.display_crypto(self))

        # Add custom menus
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.add_new_menu(self, "Home", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.add_new_menu(self, "Wallet", "btn_wallet", "url(:/16x16/icons/16x16/cil-credit-card.png)", True)
        UIFunctions.add_new_menu(self, "Trade", "btn_trade", "url(:/16x16/icons/16x16/cil-briefcase.png)", True)
        UIFunctions.add_new_menu(self, "Virtual Trading Agent", "btn_virtual_trading_agent",
                                 "url(:/16x16/icons/16x16/cil-user.png)", True)
        UIFunctions.add_new_menu(self, "History", "btn_history", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        UIFunctions.add_new_menu(self, "Settings", "btn_settings", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)

        # Start menu default selection
        UIFunctions.select_menu("btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        # Move window, maximize and restore
        def move_window(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.return_status() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.drag_pos)
                self.drag_pos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = move_window

        # Load definitions
        UIFunctions.ui_definitions(self)

        # QTableWidget parameters
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Show main window
        self.show()

    ########################################################################
    # Menus - Dynamic widget change
    ########################################################################
    def button(self):

        # Get btn clicked event
        btn_widget = self.sender()

        # Page - Home
        if btn_widget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.reset_style(self, "btn_home")
            UIFunctions.label_page(self, "Home")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # Page - Wallet
        if btn_widget.objectName() == "btn_wallet":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_wallet)
            UIFunctions.reset_style(self, "btn_wallet")
            UIFunctions.label_page(self, "Wallet ")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))
            WalletFrontEnd.display_crypto(self)

        # Page - Trading
        if btn_widget.objectName() == "btn_trade":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_trade)
            UIFunctions.reset_style(self, "btn_trade")
            UIFunctions.label_page(self, "Trade")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # Page - Virtual Trading Agent
        if btn_widget.objectName() == "btn_virtual_trading_agent":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_virtual_agent)
            UIFunctions.reset_style(self, "btn_virtual_trading_agent")
            UIFunctions.label_page(self, "Virtual Trading Agent")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # Page - History
        if btn_widget.objectName() == "btn_history":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_history)
            UIFunctions.reset_style(self, "btn_history")
            UIFunctions.label_page(self, "History")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

        # Page - Setting
        if btn_widget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.reset_style(self, "btn_settings")
            UIFunctions.label_page(self, "Settings")
            btn_widget.setStyleSheet(UIFunctions.select_menu(btn_widget.styleSheet()))

    # Event mouse double click
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    # Event mouse click
    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    # Event key pressed
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    # Event resize
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())


