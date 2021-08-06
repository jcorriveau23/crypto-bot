from sdk.ethsnarks.eddsa import PoseidonEdDSA
from sdk.loopring_v3_client import LoopringV3Client
import ujson
import time


loopring_exported_account = {
    "name":             "UAT Account 1",
    "chainId":          1,
    "exchangeName":     "Loopring Exchange v2",
    "exchangeAddress":  "0x0BABA1Ad5bE3a5C0a66E7ac838a129Bf948f1eA4",
    "accountAddress":   "0x7E8034d38B9B3fd58a6eDD456d6DC20040Db4d82",
    "accountId":        32442,
    "apiKey":           "qFveZVmKzyiwBY7lzaUwaTAdNupZIR6ablp7rXE2aohWiQ13quXji7K4KmpeMMqY",
    "publicKeyX":       "0x254a6ba24dab16ef6f26a731fc40732913f339b19b5239cb9e99f28c616fd405",
    "publicKeyY":       "0x0a1c49fbcd2b0070b2b5a898486b26698b9903bd37f9e4d134dae88ae9c8e8bf",
    "privateKey":       "0x1b4fcac04629789aa7a490f48496481f2c23f7ec714b4b1dd9f21fec559c212",
    "ecdsaKey":         "0x1",
    "whitelisted": False
}



loopring_rest_sample = LoopringV3Client()
loopring_rest_sample.connect(loopring_exported_account)

# t = loopring_rest_sample.query_srv_time()
# print(t)

#exchange_info = loopring_rest_sample.query_info("exchange/info")
#print(ujson.dumps(exchange_info, indent=4, sort_keys=True))


market_info = loopring_rest_sample.query_market_config()
print(ujson.dumps(market_info, indent=4, sort_keys=True))

#account_info = loopring_rest_sample.get_account()
#print(ujson.dumps(account_info, indent=4, sort_keys=True))

#balance = loopring_rest_sample.query_balance()
#print(ujson.dumps(balance, indent=4, sort_keys=True))

#orders = loopring_rest_sample.get_orders()
#print(ujson.dumps(orders, indent=4, sort_keys=True))

#order = loopring_rest_sample.get_order("1371414171107056839874821144675657211013805939786302300071776478813101588778") # hash of the order
#print(ujson.dumps(order, indent=4, sort_keys=True))


#print(loopring_rest_sample.get_storageId(0))
#sell_response = loopring_rest_sample.send_order("ETH", "USDT", False, 3000, 0.04)    # base_token, quote_token, buy, price, volume, ammPoolAddress = None
#print(sell_response)

#buy_response = loopring_rest_sample.send_order("ETH", "USDT", True, 1500, 0.04)    # base_token, quote_token, buy, price, volume, ammPoolAddress = None
#print(buy_response)