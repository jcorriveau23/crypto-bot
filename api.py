
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from binance.client import Client
from binance.enums import *

import Keys

class API():
    def __init__(self, exchange):
        self.client = Client(api_key=Keys.api_key, api_secret=Keys.api_secret)
        self.info = self.client.get_exchange_info()
        self.exchange = exchange

    ## initiate an order of a specific pairing side and price
    ## input:   pair: ex: ETHUSDT (str)
    ##          side: "buy" or "sell"
    ##          price:  price value (float)
    def create_order(self, pair, side, price):
        pass

    ## Validate if an order is filled or not
    ## input:   orderID: ID of the order you want to check if it is filled
    def order_isFilled(self, orderID):
        pass

    ## Cancel a specific order
    ## input:   orderID: ID of the order you want to cancel
    def cancel_order(self, oderID):
        pass
