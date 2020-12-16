
class Simplino():
    def __init__(self, pair):
        self.pair = pair

        trading_asset = pair.split('/')
        self.buy_asset = trading_asset[0]
        self.sell_asset = trading_asset[1]

        self.last_buys = {}
        self.last_sells = {}

        self.buy_qtys = []
        self.buyPrices = []
        self.sell_prices = []

        self.nb_sells = 0
        self.nb_buys = 0

        self.buy_qty = 0

        self.buy_order_id = 0
        self.sell_order_id = 0

        self.ready = False

    def simplino_algo_create_buys(self, balance, start_price, loss_depth, buys_nb_depth, buy_more_pourcent):
        self.buyPrices = []
        self.sell_prices = []
        self.buy_qtys = []

        lowest_price = start_price * (1 - loss_depth)

        buy_coef = 1 - (lowest_price/start_price)**(1/buys_nb_depth)

        buy_qty = []
        mult = []
        buy_price = start_price

        for i in range(buys_nb_depth):
            buy_price *= (1 - buy_coef)
            self.buyPrices.append(buy_price)
            if i == 0:
                self.sell_prices.append(self.buyPrices[i]*1.005) #TODO get rid of hardcode pourcentage on first sell
            else:
                self.sell_prices.append(self.buyPrices[i] + (self.buyPrices[i-1] - self.buyPrices[i]) / 2)

            buy_qty.append(buy_more_pourcent**i)

            mult.append(buy_qty[i]*self.buyPrices[i])


        start_qty = balance/sum(mult)
        qty = start_qty
        for i in range(buys_nb_depth):
            self.buy_qtys.append(qty)
            qty *= buy_more_pourcent

        print("buy price list value: {}".format(self.buyPrices))
        print("buy qty list value: {}".format(self.buy_qtys))
        print("sell price list value: {}".format(self.sell_prices))

        self.ready = True

a = Simplino("ETH/USDT")
a.simplino_algo_create_buys(2000, 600, 0.3, 23, 1.08)

