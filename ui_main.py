# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setObjectName("calculate_button")
        self.gridLayout_2.addWidget(self.calculate_button, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.nb_buy_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nb_buy_text_input.setObjectName("nb_buy_text_input")
        self.gridLayout_2.addWidget(self.nb_buy_text_input, 2, 1, 1, 1)
        self.start_price_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.start_price_text_input.setObjectName("start_price_text_input")
        self.gridLayout_2.addWidget(self.start_price_text_input, 1, 1, 1, 1)
        self.drop_poucent_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.drop_poucent_text_input.setObjectName("drop_poucent_text_input")
        self.gridLayout_2.addWidget(self.drop_poucent_text_input, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.pair_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.pair_comboBox.setObjectName("pair_comboBox")
        self.gridLayout_2.addWidget(self.pair_comboBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Pairing_label = QtWidgets.QLabel(self.centralwidget)
        self.Pairing_label.setObjectName("Pairing_label")
        self.gridLayout.addWidget(self.Pairing_label, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.Buy_order_filled_label = QtWidgets.QLabel(self.centralwidget)
        self.Buy_order_filled_label.setObjectName("Buy_order_filled_label")
        self.gridLayout.addWidget(self.Buy_order_filled_label, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.Buy_asset_label = QtWidgets.QLabel(self.centralwidget)
        self.Buy_asset_label.setObjectName("Buy_asset_label")
        self.gridLayout.addWidget(self.Buy_asset_label, 3, 2, 1, 1)
        self.Buy_Qty_label = QtWidgets.QLabel(self.centralwidget)
        self.Buy_Qty_label.setObjectName("Buy_Qty_label")
        self.gridLayout.addWidget(self.Buy_Qty_label, 3, 1, 1, 1)
        self.Buy_Qty_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Buy_Qty_label_2.setObjectName("Buy_Qty_label_2")
        self.gridLayout.addWidget(self.Buy_Qty_label_2, 4, 1, 1, 1)
        self.Sell_order_filled_label = QtWidgets.QLabel(self.centralwidget)
        self.Sell_order_filled_label.setObjectName("Sell_order_filled_label")
        self.gridLayout.addWidget(self.Sell_order_filled_label, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1)
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setObjectName("price_label")
        self.gridLayout_3.addWidget(self.price_label, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.price_pairing_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.price_pairing_label_4.setObjectName("price_pairing_label_4")
        self.gridLayout_3.addWidget(self.price_pairing_label_4, 0, 2, 1, 1)
        self.price_pairing_label = QtWidgets.QLabel(self.centralwidget)
        self.price_pairing_label.setObjectName("price_pairing_label")
        self.gridLayout_3.addWidget(self.price_pairing_label, 1, 2, 1, 1)
        self.ask_price_label = QtWidgets.QLabel(self.centralwidget)
        self.ask_price_label.setObjectName("ask_price_label")
        self.gridLayout_3.addWidget(self.ask_price_label, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.price_pairing_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.price_pairing_label_2.setObjectName("price_pairing_label_2")
        self.gridLayout_3.addWidget(self.price_pairing_label_2, 2, 2, 1, 1)
        self.start_price_label = QtWidgets.QLabel(self.centralwidget)
        self.start_price_label.setObjectName("start_price_label")
        self.gridLayout_3.addWidget(self.start_price_label, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)
        self.bid_price_label = QtWidgets.QLabel(self.centralwidget)
        self.bid_price_label.setObjectName("bid_price_label")
        self.gridLayout_3.addWidget(self.bid_price_label, 3, 1, 1, 1)
        self.price_pairing_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.price_pairing_label_3.setObjectName("price_pairing_label_3")
        self.gridLayout_3.addWidget(self.price_pairing_label_3, 3, 2, 1, 1)
        self.gain_label = QtWidgets.QLabel(self.centralwidget)
        self.gain_label.setObjectName("gain_label")
        self.gridLayout_3.addWidget(self.gain_label, 4, 1, 1, 1)
        self.sell_asset_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_asset_label.setObjectName("sell_asset_label")
        self.gridLayout_3.addWidget(self.sell_asset_label, 4, 2, 1, 1)
        self.start_time_label = QtWidgets.QLabel(self.centralwidget)
        self.start_time_label.setObjectName("start_time_label")
        self.gridLayout_3.addWidget(self.start_time_label, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 3, 6, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sell_filled_Qty_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_filled_Qty_label.setObjectName("sell_filled_Qty_label")
        self.gridLayout_5.addWidget(self.sell_filled_Qty_label, 2, 6, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 2, 2, 1, 1)
        self.Buy_asset_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.Buy_asset_label_3.setObjectName("Buy_asset_label_3")
        self.gridLayout_5.addWidget(self.Buy_asset_label_3, 2, 4, 1, 1)
        self.buy_qty_label = QtWidgets.QLabel(self.centralwidget)
        self.buy_qty_label.setObjectName("buy_qty_label")
        self.gridLayout_5.addWidget(self.buy_qty_label, 1, 3, 1, 1)
        self.Buy_asset_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.Buy_asset_label_5.setObjectName("Buy_asset_label_5")
        self.gridLayout_5.addWidget(self.Buy_asset_label_5, 2, 7, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 2, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)
        self.Buy_order_ID_label = QtWidgets.QLabel(self.centralwidget)
        self.Buy_order_ID_label.setObjectName("Buy_order_ID_label")
        self.gridLayout_5.addWidget(self.Buy_order_ID_label, 1, 1, 1, 1)
        self.Buy_asset_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Buy_asset_label_2.setObjectName("Buy_asset_label_2")
        self.gridLayout_5.addWidget(self.Buy_asset_label_2, 1, 4, 1, 1)
        self.buy_filled_Qty_label = QtWidgets.QLabel(self.centralwidget)
        self.buy_filled_Qty_label.setObjectName("buy_filled_Qty_label")
        self.gridLayout_5.addWidget(self.buy_filled_Qty_label, 1, 6, 1, 1)
        self.Buy_asset_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.Buy_asset_label_4.setObjectName("Buy_asset_label_4")
        self.gridLayout_5.addWidget(self.Buy_asset_label_4, 1, 7, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 1, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 1, 5, 1, 1)
        self.Sell_order_ID_label = QtWidgets.QLabel(self.centralwidget)
        self.Sell_order_ID_label.setObjectName("Sell_order_ID_label")
        self.gridLayout_5.addWidget(self.Sell_order_ID_label, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 2, 0, 1, 1)
        self.sell_qty_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_qty_label.setObjectName("sell_qty_label")
        self.gridLayout_5.addWidget(self.sell_qty_label, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.Order_filled_tab = QtWidgets.QTableWidget(self.centralwidget)
        self.Order_filled_tab.setObjectName("Order_filled_tab")
        self.Order_filled_tab.setColumnCount(0)
        self.Order_filled_tab.setRowCount(0)
        self.gridLayout_4.addWidget(self.Order_filled_tab, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.label_2.setText(_translate("MainWindow", "start price"))
        self.label_3.setText(_translate("MainWindow", "nb buy"))
        self.label_4.setText(_translate("MainWindow", "% drop"))
        self.label.setText(_translate("MainWindow", "Available pairs"))
        self.Pairing_label.setText(_translate("MainWindow", "-"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_8.setText(_translate("MainWindow", "Buy Qty"))
        self.label_9.setText(_translate("MainWindow", "Pairing"))
        self.Buy_order_filled_label.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Buy order filled"))
        self.label_7.setText(_translate("MainWindow", "Sell order filled"))
        self.label_10.setText(_translate("MainWindow", "possible sells"))
        self.Buy_asset_label.setText(_translate("MainWindow", "-"))
        self.Buy_Qty_label.setText(_translate("MainWindow", "0"))
        self.Buy_Qty_label_2.setText(_translate("MainWindow", "0"))
        self.Sell_order_filled_label.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.label_17.setText(_translate("MainWindow", "Bid price"))
        self.label_18.setText(_translate("MainWindow", "profit if sailing all now"))
        self.price_label.setText(_translate("MainWindow", "-"))
        self.label_16.setText(_translate("MainWindow", "Ask price"))
        self.label_14.setText(_translate("MainWindow", "start price"))
        self.price_pairing_label_4.setText(_translate("MainWindow", "-"))
        self.price_pairing_label.setText(_translate("MainWindow", "-"))
        self.ask_price_label.setText(_translate("MainWindow", "-"))
        self.label_13.setText(_translate("MainWindow", "Current price"))
        self.price_pairing_label_2.setText(_translate("MainWindow", "-"))
        self.start_price_label.setText(_translate("MainWindow", "-"))
        self.label_19.setText(_translate("MainWindow", "Start time"))
        self.bid_price_label.setText(_translate("MainWindow", "-"))
        self.price_pairing_label_3.setText(_translate("MainWindow", "-"))
        self.gain_label.setText(_translate("MainWindow", "-"))
        self.sell_asset_label.setText(_translate("MainWindow", "-"))
        self.start_time_label.setText(_translate("MainWindow", "-"))
        self.sell_filled_Qty_label.setText(_translate("MainWindow", "-"))
        self.label_24.setText(_translate("MainWindow", "Qty"))
        self.Buy_asset_label_3.setText(_translate("MainWindow", "-"))
        self.buy_qty_label.setText(_translate("MainWindow", "-"))
        self.Buy_asset_label_5.setText(_translate("MainWindow", "-"))
        self.label_25.setText(_translate("MainWindow", "Qty filled"))
        self.label_20.setText(_translate("MainWindow", "Buy order ID"))
        self.Buy_order_ID_label.setText(_translate("MainWindow", "-"))
        self.Buy_asset_label_2.setText(_translate("MainWindow", "-"))
        self.buy_filled_Qty_label.setText(_translate("MainWindow", "-"))
        self.Buy_asset_label_4.setText(_translate("MainWindow", "-"))
        self.label_22.setText(_translate("MainWindow", "Qty"))
        self.label_23.setText(_translate("MainWindow", "Qty filled"))
        self.Sell_order_ID_label.setText(_translate("MainWindow", "-"))
        self.label_21.setText(_translate("MainWindow", "Sell order ID"))
        self.sell_qty_label.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", "Open Orders"))
        self.label_12.setText(_translate("MainWindow", "Order filled"))
        self.label_15.setText(_translate("MainWindow", "Prevision"))
