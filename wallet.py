from PySide2 import QtCore, QtGui, QtWidgets
from main import MainWindow
from ui_helpers import *
from pathlib import Path


class WalletFrontEnd(MainWindow):

    def display_crypto(self):

        info = self.api.client.get_account()

        favorite_coin = ['ETH', 'BTC', 'USDT']

        # Generate empty table
        for row in range(0, 10):
            self.ui.table_wallet.insertRow(row)
        for column in range(0, 6):
            self.ui.table_wallet.insertColumn(column)

        # Table header
        self.ui.table_wallet.setCellWidget(0, 0, create_label('Coin'))
        self.ui.table_wallet.setCellWidget(0, 1, create_label('Total'))
        self.ui.table_wallet.setCellWidget(0, 2, create_label('Available'))
        self.ui.table_wallet.setCellWidget(0, 3, create_label('Locked'))
        self.ui.table_wallet.setCellWidget(0, 4, create_label('USDT Value'))
        self.ui.table_wallet.setCellWidget(0, 5, create_label('US Dollar'))

        # Table info
        row_number = 1
        print( info['balances'])
        for assets in info['balances']:
            if assets['asset'] in favorite_coin:
                print(assets['asset'])

                coin_name = assets['asset']

                btn_coin = create_button_coin(coin_name)
                self.ui.table_wallet.setCellWidget(row_number, 0, btn_coin)
                self.ui.table_wallet.setCellWidget(row_number, 1, create_label(str(float(assets['free']) +
                                                                                   float(assets['locked']))))
                self.ui.table_wallet.setCellWidget(row_number, 2, create_label(assets['free']))
                self.ui.table_wallet.setCellWidget(row_number, 3, create_label(assets['locked']))
                self.ui.table_wallet.setCellWidget(row_number, 4, create_label('todo'))
                self.ui.table_wallet.setCellWidget(row_number, 5, create_label('todo'))
                self.ui.table_wallet.resizeRowToContents(row_number)
                row_number = row_number + 1


def create_button_coin(coin_name):

    btn_coin_name = "btn_{}".format(coin_name)

    cwd = str(Path.cwd()).replace("\\", "/")
    icon_path = cwd + "/icons/crypto_icons/{}.png".format(coin_name.lower())

    font = QFont()
    font.setFamily(u"Segoe UI")
    button = QtWidgets.QPushButton()
    button.setObjectName(btn_coin_name)
    size_policy_3 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    size_policy_3.setHorizontalStretch(0)
    size_policy_3.setVerticalStretch(0)
    size_policy_3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
    button.setSizePolicy(size_policy_3)
    button.setMinimumSize(QSize(70, 70))
    button.setLayoutDirection(Qt.LeftToRight)
    button.setFont(font)
    button.setIcon(QIcon(icon_path))
    button.setIconSize(QSize(32, 32))
    button.setText(coin_name)
    button.setToolTip(coin_name)
    # button.clicked.connect(self.button)
    return button

