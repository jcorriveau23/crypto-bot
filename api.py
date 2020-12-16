from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
import ccxt
import time
from binance.enums import *
import logging

import Keys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("log_file.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class API:
    def __init__(self, ex):
        self.exchange_id = ex
        exchange_class = getattr(ccxt, ex)
        self.exchange = exchange_class({
            'apiKey': Keys.api_key,
            'secret': Keys.api_secret,
            'timeout': 50000,
            'enableRateLimit': True,
        })
        self.exchange.load_markets()

    ## initiate an order of a specific pairing side and price and qty
    #  input:   pair: ex: ETHUSDT (str)
    #           side: "Buy" or "Sell"
    #           price:  price value (float)
    #  return:  ID of the order created
    #           success or failed
    def create_limit_order(self, pair, side, price, qty):
        if side is "Buy":
            try:
                orderID = self.exchange.create_limit_buy_order(pair,
                                                               round(qty, 5),
                                                               # TODO uses contraints of pairing from binance api
                                                               round(price, 2)
                                                               # TODO uses contraints of pairing
                                                               )


                logger.info('Buy Order Sent => QTY: {} ETH, PRICE: {} USDT/ETH'.format(qty, price))
                return True, orderID['info']['orderId']
            except Exception as e:
                logger.error('Buy Order could not be send! Exception: {}'.format(e))
                return False, None

        elif side is "Sell":
            try:
                orderID = self.exchange.create_limit_sell_order(pair,
                                                                round(qty, 2),
                                                                # TODO uses contraints of pairing
                                                                round(price, 2))  # TODO uses contraints of pairing

                logger.info('Buy Order Sent => QTY: {} ETH, PRICE: {} USDT/ETH'.format(qty, price))
                return True, orderID['info']['orderId']
            except Exception as e:
                logger.error('Buy Order could not be send! Exception: {}'.format(e))
                return False, None
        else:
            return False, None

    ## Validate if an order is filled or not
    #  input:   orderID: ID of the order you want to check if it is filled
    #  return:  success or failed
    def order_isfilled(self, pair, buy_order_id, sell_order_id):
        try:
            orders = self.exchange.fetch_open_orders(symbol=pair)
            for order in orders:
                if order["info"]["orderId"] == buy_order_id:
                    if order["info"]["status"] == "FILLED":
                        return True, "BUY", order
                    else:
                        # TODO other cases
                        return False, None, orders

                elif order["info"]["orderId"] == sell_order_id:
                    if order["info"]["status"] == "FILLED":
                        return True, "SELL", order
                    else:
                        # TODO other cases
                        return False, None, orders

        except Exception as e:
            logging.error("Order info could not be fetch, Exception: {} ".format(e))
            return False, None, orders

    ## Cancel a specific order
    #  input:   orderID: ID of the order you want to cancel
    #  return:  success or failed
    def cancel_order(self, oderID, pair):
        try:
            self.exchange.cancel_order(symbol=pair, orderId=oderID)
            logger.info('Sell Order canceled')
            return True
        except Exception as e:
            logger.error(
                "Buy Order Cancel has not worked: Pair: {}, OrderId: {}, Exception: {} ".format(pair, oderID, e))
            return False
