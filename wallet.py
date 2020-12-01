from main import MainWindow


class WalletFrontEnd(MainWindow):

    TMP = [ 'ETH', 'Etherium', 0.018]

    def add_crypto_display(self):
        self.ui.table_wallet.setEnabled(False)
        pass


