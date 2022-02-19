from sdk.ethsnarks.eddsa import PoseidonEdDSA
from sdk.loopring_v3_client import LoopringV3Client
import ujson
import time
import Keys

loopring_rest_sample = LoopringV3Client()
loopring_rest_sample.connect(Keys.loopring_exported_account)

# t = loopring_rest_sample.query_srv_time()
# print(t)

#exchange_info = loopring_rest_sample.query_info("exchange/info")
#print(ujson.dumps(exchange_info, indent=4, sort_keys=True))


#market_info = loopring_rest_sample.query_market_config()
#print(ujson.dumps(market_info, indent=4, sort_keys=True))

#account_info = loopring_rest_sample.get_account()
#print(ujson.dumps(account_info, indent=4, sort_keys=True))

#balance = loopring_rest_sample.query_balance()
#print(ujson.dumps(balance, indent=4, sort_keys=True))

#orders = loopring_rest_sample.get_orders()
#print(ujson.dumps(orders, indent=4, sort_keys=True))

#order = loopring_rest_sample.get_order("1371414171107056839874821144675657211013805939786302300071776478813101588778") # hash of the order
#print(ujson.dumps(order, indent=4, sort_keys=True))


print(loopring_rest_sample.get_storageId(6))
sell_response = loopring_rest_sample.send_order("ETH", "USDC", True, 2900, 0.04)    # base_token, quote_token, buy, price, volume, ammPoolAddress = None
print(sell_response)

#buy_response = loopring_rest_sample.send_order("ETH", "USDT", True, 1500, 0.04)    # base_token, quote_token, buy, price, volume, ammPoolAddress = None
#print(buy_response)