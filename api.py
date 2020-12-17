import ccxt
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

    ##
    #  input:   pair: ex: ETHUSDT (str)
    #           side: "Buy" or "Sell"
    #           price:  price value (float)
    #  return:  ID of the order created
    #           success or failed
    def create_limit_order(self, pair, side, price, qty):
        """
        initiate an order of a specific pairing side and price and qty
        :param pair:
        :param side:    Buy or Sell
        :param price:
        :param qty:
        :return:
        """
        if side is "Buy":
            try:
                order_id = self.exchange.create_limit_buy_order(pair,
                                                                round(qty, 5),
                                                                # TODO uses contraints of pairing from binance api
                                                                round(price, 2)
                                                                # TODO uses contraints of pairing
                                                                )

                logger.info('Buy Order Sent => QTY: {} ETH, PRICE: {} USDT/ETH'.format(qty, price))
                return True, order_id['info']['orderId']
            except Exception as e:
                logger.error('Buy Order could not be send! Exception: {}'.format(e))
                return False, None

        elif side is "Sell":
            try:
                order_id = self.exchange.create_limit_sell_order(pair,
                                                                 round(qty, 5),
                                                                 # TODO uses contraints of pairing
                                                                 round(price, 2))  # TODO uses contraints of pairing

                logger.info('Buy Order Sent => QTY: {} ETH, PRICE: {} USDT/ETH'.format(qty, price))
                return True, order_id['info']['orderId']
            except Exception as e:
                logger.error('Buy Order could not be send! Exception: {}'.format(e))
                return False, None
        else:
            return False, None

    def order_isfilled(self, pair, order_id):
        """
        Validate if that buy and sell order is  fill

        :param pair:
        :param order_id:
        :return:
        """
        try:
            order = self.exchange.fetch_order(id=order_id, symbol=pair)
            print(order)
            if order["info"]["status"] == "FILLED":
                logger.info('{} order is filled'.format(order["info"]["side"]))
                return True, order
            else:
                return False, order

        except Exception as e:
            logging.error("Order info could not be fetch, Exception: {} ".format(e))
            return False, None, None

    def cancel_order(self, order_id, pair):
        """
        Cancel a specific order

        :param order_id: ID of the order you want to cancel
        :param pair:
        :return:
        """
        try:
            self.exchange.cancel_order(order_id, pair)
            logger.info('Order canceled: ID: {}'.format(order_id))
            return True
        except Exception as e:
            logger.error(
                "Buy Order Cancel has not worked: Pair: {}, OrderId: {}, Exception: {} ".format(pair, order_id, e))
            return False
