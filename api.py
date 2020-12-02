from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from binance.client import Client
from binance.enums import *
import logging

import Keys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("log_file.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class API():
    def __init__(self, exchange):
        self.client = Client(api_key=Keys.api_key, api_secret=Keys.api_secret)
        self.info = self.client.get_exchange_info()
        self.exchange = exchange  # exchange name

    ## initiate an order of a specific pairing side and price and qty
    #  input:   pair: ex: ETHUSDT (str)
    #           side: "Buy" or "Sell"
    #           price:  price value (float)
    #  return:  ID of the order created
    #           success or failed
    def create_limit_order(self, pair, side, price, qty):
        if side is "Buy":
            try:
                orderID = self.client.order_limit_buy(symbol=pair,
                                                    quantity=round(qty, 5), #TODO uses contraints of pairing from binance api
                                                    price=str(round(price, 2)))  #TODO uses contraints of pairing

                logger.info('Buy Order Sent => QTY: {} ETH, PRICE: {} USDT/ETH'.format(qty, price))
                return True, orderID
            except Exception as e:
                logger.error('Buy Order could not be send! Exception: {}'.format(e))
                return False, None

        elif side is "Sell":
            try:
                orderID = self.client.order_limit_buy(symbol=pair,
                                                    quantity=round(qty, 2), #TODO uses contraints of pairing
                                                    price=str(round(price, 2)))  #TODO uses contraints of pairing

                logger.info('Buy Order Sent => QTY: {} ETH, PRICE: {} USDT/ETH'.format(qty, price))
                return True, orderID
            except Exception as e:
                logger.error('Buy Order could not be send! Exception: {}'.format(e))
                return False, None
        else:
            return False


    ## Validate if an order is filled or not
    #  input:   orderID: ID of the order you want to check if it is filled
    #  return:  success or failed
    def order_isfilled(self, orderID, pair):
        try:
            order = self.client.get_order(symbol=pair, orderId=orderID)
            if order['status'] == 'FILLED':
                logger.info("Buy order is filled: {}".format(order))
                return True

        except Exception as e:
            logger.error("Buy Order info could not be fetch:pair: {} OrderId: {}, Exception: {} ".format(pair, orderID, e))
            return False

    ## Cancel a specific order
    #  input:   orderID: ID of the order you want to cancel
    #  return:  success or failed
    def cancel_order(self, oderID, pair):
        try:
            self.client.cancel_order(symbol=pair, orderId=oderID)
            logger.info('Sell Order canceled')
            return True
        except Exception as e:
            logger.error("Buy Order Cancel has not worked: Pair: {}, OrderId: {}, Exception: {} ".format(pair, oderID, e))
            return False