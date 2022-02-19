import hashlib
import hmac
import ujson
from copy import copy
from datetime import datetime, timedelta
from enum import Enum, Flag
from threading import Lock
from operator import itemgetter
from py_eth_sig_utils import utils as sig_utils
from py_eth_sig_utils.signing import v_r_s_to_signature
from random import randint
import re
import sys
from time import time, sleep
import urllib
from web3 import Web3

from .request_utils.rest_client import RestClient
from .ethsnarks.eddsa import PureEdDSA, PoseidonEdDSA
from .ethsnarks.field import FQ, SNARK_SCALAR_FIELD
from .ethsnarks.poseidon import poseidon_params, poseidon
from .sig_utils.ecdsa_utils import *
from .sig_utils.eddsa_utils import *

LOOPRING_REST_HOST = "https://api3.loopring.io"

class Security(Flag):
    NONE        = 0
    EDDSA_SIGN  = 1
    API_KEY     = 2
    ECDSA_AUTH  = 4

class SignatureType(Enum):
    ECDSA           = 0
    EDDSA           = 1
    HASH_APPROVED   = 2

class EthSignType:
    ILLEGAL     = "00"
    INVALID     = "01"
    EIP_712     = "02"
    ETH_SIGN    = "03"

class OffchainRequestType(Enum):
    ORDER                    = 0
    OFFCHAIN_WITHDRAWAL      = 1
    UPDATE_ACCOUNT           = 2
    TRANSFER                 = 3
    FAST_OFFCHAIN_WITHDRAWAL = 4
    OPEN_ACCOUNT             = 5
    AMM_EXIT                 = 6
    DEPOSIT                  = 7
    AMM_JOIN                 = 8


class LoopringV3Client(RestClient):
    """
    LOOPRING REST API SAMPLE
    """

    MAX_ORDER_ID = 1<<32

    def __init__(self):
        """"""
        super().__init__()
        # exported account
        self.api_key     = ""
        self.address     = ""
        self.publicKeyX  = ""
        self.publicKeyY  = ""
        self.accountId   = 0

        # self.web3 = Web3(Web3.HTTPProvider(eth_addr))
        # order related
        self.orderId     = [0] * 256
        self.offchainId     = [0] * 256
        self.time_offset = 0
        self.nonce      = 0

        self.ammPoolNames = {}
        self.ammPools = {}
        self.tokenIds = {}
        self.tokenNames = {}
        self.tokenDecimals = {}

        self.init(LOOPRING_REST_HOST)
        self.start()

    def connect(self, account_settings : dict):
        """
        Initialize connection to LOOPRING REST server.
        """
        self.accountId  = account_settings['accountId']
        self.address    = account_settings['accountAddress']
        self.api_key    = account_settings['apiKey']
        self.exchange   = account_settings['exchangeAddress']
        self.ecdsaKey   = int(account_settings['ecdsaKey'], 16).to_bytes(32, byteorder='big')
        self.eddsaKey   = account_settings['privateKey']
        self.publicKeyX = account_settings["publicKeyX"]
        self.publicKeyY = account_settings["publicKeyY"]
        self.chainId    = account_settings["chainId"]
        self.whitelisted = account_settings["whitelisted"]

        self.next_eddsaKey = None

        self.ammJoinfeeBips = 0.0015

        # align srv and local time
        self.query_time()
        self.load_tokens()
        self.fetch_account()
        self.fetch_apiKey()

        EIP712.init_env(name="Loopring Protocol",
                        version="3.6.0",
                        chainId=self.chainId,
                        verifyingContract=self.exchange)

    def sign(self, request):
        """
        Generate LOOPRING signature.
        """
        security = request.data.pop("security", Security.NONE)
        if security == Security.NONE:
            if request.method == "POST":
                request.data = request.params
                request.params = {}
            return request

        path = request.path
        if request.params:
            if request.method in ["GET", "DELETE"]:
                path = request.path + "?" + urllib.parse.urlencode(request.params)
        else:
            request.params = dict()

        # request headers
        headers = {
            "Content-Type" : "application/json",
            "Accept"       : "application/json",
            "X-API-KEY"    : self.api_key,
        }
        if request.headers != None:
            headers.update(request.headers)

        if security & Security.EDDSA_SIGN:
            signer = UrlEddsaSignHelper(self.eddsaKey, LOOPRING_REST_HOST)
            signature = signer.sign(request)
            headers.update({"X-API-SIG": signature})
        elif security & Security.ECDSA_AUTH:
            # headers.update({"X-API-SIG": request.data["X-API-SIG"]})
            assert "X-API-SIG" in headers
            pass

        request.path = path
        if request.method not in ["GET", "DELETE"]:
            request.data = ujson.dumps(request.data) if len(request.data) != 0 else request.params
            request.params = {}
        else:
            request.data = {}

        request.headers = headers

        # print(f"finish sign {request}")
        return request

    def query_srv_time(self):
        data = {
            "security": Security.NONE
        }

        response = self.request(
            "GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path="/api/v3/timestamp",
            data=data
        )
        json_resp = response.json()
        return json_resp['timestamp']

    def query_info(self, restPath):
        """"""
        data = {
            "security": Security.NONE
        }

        response = self.request(
            "GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path="/api/v3/" + restPath,
            data=data
        )
        json_resp = response.json()
        return json_resp

    def query_amm_pool_balance(self, poolAddress):
        """"""
        data = {
            "security": Security.NONE
        }

        response = self.request(
            "GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path="/api/v3/amm/balance",
            data=data,
            params={"poolAddress": poolAddress[2:]}
        )
        json_resp = response.json()
        return json_resp

    def query_time(self):
        """"""
        data = {
            "security": Security.NONE
        }

        self.request(
            "GET",
            path="/api/v3/timestamp",
            data=data
        )

    def load_tokens(self):
        """
            query market token and contract config
        """
        data = {"security": Security.NONE}

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path="/api/v3/exchange/tokens",
            data=data
        )
        json_resp = response.json()

        for d in json_resp:
            self.tokenIds[d['symbol']] = d['tokenId']
            self.tokenNames[d['tokenId']] = d['symbol']
            self.tokenDecimals[d['tokenId']] = d['decimals']


        return json_resp

    def load_markets(self):
        """
            query market token and contract config
        """
        data = {"security": Security.NONE}

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path="/api/v3/exchange/markets",
            data=data
        )
        json_resp = response.json()

        self.markets = {}

        for d in json_resp["markets"]:

            self.markets[d['market']] = {}
            self.markets[d['market']]["precision"] = {}
            self.markets[d['market']]["precision"]["price"] = d['precisionForPrice']
            self.markets[d['market']]["precision"]["amount"] = 10
            self.markets[d['market']]["maker"] = 0 # maker fees are 0 on loopring

        return json_resp

    def fetch_account(self):
        """"""
        data = {
            "security": Security.API_KEY
        }

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/account",
            params={
                "owner": self.address
            },
            data=data
        )

        json_resp = response.json()
        return json_resp

    def get_user_data(self, dataType):
        """"""
        data = {
            "security": Security.API_KEY
        }

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/user/{dataType}",
            params={
                "accountId": self.accountId
            },
            data=data
        )
        json_resp = response.json()
        return json_resp

    def get_transfers(self):
        """"""
        return self.get_user_data("transfers")

    def get_updates(self):
        """"""
        return self.get_user_data("updateInfo")

    def get_creates(self):
        """"""
        return self.get_user_data("createInfo")

    def get_trades(self):
        """"""
        return self.get_user_data("trades")

    def fetch_orders(self):
        """"""
        data = {
            "security": Security.API_KEY
        }

        params = {
            "accountId": self.accountId,
        }

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/orders",
            params=params,
            data=data
        )
        json_resp = response.json()
        return json_resp

    def fetch_order(self, id, symbol=None):
        """"""
        data = {
            "security": Security.API_KEY
        }

        params = {
            "accountId": self.accountId,
            "orderHash": id
        }

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/order",
            params=params,
            data=data
        )
        json_resp = response.json()

        base_token, quote_token = symbol.split("-")

        json_resp["info"] = {"status": "NEW",
                             "side": json_resp["side"],
                             "price": json_resp["price"],
                             "executedQty": str(float(json_resp["volumes"]["baseFilled"])/10**self.tokenDecimals[self.tokenIds[base_token]]),
                             "origQty": str(float(json_resp["volumes"]["baseAmount"])/10**self.tokenDecimals[self.tokenIds[base_token]]),
                             "orderId": json_resp["hash"]
                             }

        if json_resp["status"] == "processed": # and json_resp["volumes"]["baseFilled"] == json_resp["volumes"]["baseAmount"]
            json_resp["info"]["status"] = "FILLED"

        return json_resp

    def fetch_order_book(self, market):
        """"""
        data = {
            "security": Security.API_KEY
        }

        params = {
            "market": market,
            "level":    0,
            "limit":    3       #Only will return a depth of 3 order for bid and ask
        }

        response = self.request(
            method="GET",
            path=f"/api/v3/depth",
            params=params,
            data=data
        )
        json_resp = response.json()
        return json_resp

    def get_withdrawals(self):
        """"""
        return self.get_user_data("withdrawals")

    def get_deposits(self):
        """"""
        return self.get_user_data("deposits")

    def fetch_apiKey(self):
        """"""
        data = {
            "security": Security.EDDSA_SIGN
        }

        response = self.request(
            "GET",
            path="/api/v3/apiKey",
            data=data,
            params = {
                "accountId": self.accountId,
            }
        )

        json_resp = response.json()

        self.api_key = json_resp["apiKey"]
        self.fetch_balance()

        return json_resp

    def fetch_balance(self):
        """"""
        data = {"security": Security.API_KEY}

        params = {
            "accountId": self.accountId,
            "tokens": ','.join([str(token) for token in self.tokenIds.values()])
        }

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/user/balances",
            params=params,
            data=data
        )

        json_resp = response.json()
        info = {"info": {"balances": []}}

        for asset in json_resp:
            new_asset = {"asset": self.tokenNames[asset["tokenId"]], "free": (float(asset["total"]) - float(asset["locked"]))/10**self.tokenDecimals[asset["tokenId"]]}
            info["info"]["balances"].append(new_asset)

        return info

    def get_storageId(self, tokenSId):
        """"""
        data = {
            "security": Security.API_KEY
        }

        response = self.request(
            method="GET",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/storageId",
            params={
                        "accountId"     : self.accountId,
                        "sellTokenId"   : tokenSId
                    },
            data=data
        )

        json_resp = response.json()

        self.orderId[tokenSId] = json_resp['orderId']
        self.offchainId[tokenSId] = json_resp['offchainId']

        return json_resp

    def send_order(self, base_token, quote_token, buy, price, volume, ammPoolAddress = None):
        if self.orderId[self.tokenIds[quote_token]] == 0:
            self.get_storageId(self.tokenIds[quote_token])

        order = self._create_order(base_token, quote_token, buy, price, volume, ammPoolAddress)
        data = {"security": Security.API_KEY}

        data.update(order)

        response = self.request(
            method="POST",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/order",
            params=order,
            data=data
        )

        json_resp = response.json()

        return json_resp

    def create_limit_buy_order(self, pair, qty, price):
        base_token, quote_token = pair.split("-")
        return self.send_order(base_token, quote_token, True, price, qty)

    def create_limit_sell_order(self, pair, qty, price):
        base_token, quote_token = pair.split("-")
        return self.send_order(base_token, quote_token, False, price, qty)

    def _create_order(self, base_token, quote_token, buy, price, volume, ammPoolAddress):
        if buy:
            tokenSId = self.tokenIds[quote_token]
            tokenBId = self.tokenIds[base_token]
            amountS = str(int(10 ** self.tokenDecimals[tokenSId] * price * volume))
            amountB = str(int(10 ** self.tokenDecimals[tokenBId] * volume))
        else:
            tokenSId = self.tokenIds[base_token]
            tokenBId = self.tokenIds[quote_token]
            amountS = str(int(10 ** self.tokenDecimals[tokenSId] * volume))
            amountB = str(int(10 ** self.tokenDecimals[tokenBId] * price * volume))

        orderId = self.orderId[tokenSId]
        assert orderId < self.MAX_ORDER_ID
        self.orderId[tokenSId] += 2

        # order base
        order = {
            # sign part
            "exchange"      : self.exchange,
            "accountId"     : self.accountId,
            "storageId"     : orderId,
            "sellToken": {
                "tokenId": tokenSId,
                "volume": amountS
            },
            "buyToken" : {
                "tokenId": tokenBId,
                "volume": amountB
            },
            "validUntil"    : 1700000000,
            "maxFeeBips"    : 50,
            "fillAmountBOrS": buy,
            # "taker"         : "0000000000000000000000000000000000000000",
            # aux data
            "allOrNone"     : False,
            "clientOrderId" : "SampleOrder-" + str(int(time()*1000)),
            "orderType"     : "LIMIT_ORDER"
        }

        if ammPoolAddress is not None:
            assert ammPoolAddress in self.ammPools
            assert tokenSId in self.ammPools[ammPoolAddress]
            assert tokenBId in self.ammPools[ammPoolAddress]
            order["poolAddress"] = ammPoolAddress
            order["orderType"]   = "AMM"
            order["fillAmountBOrS"] = False

        signer = OrderEddsaSignHelper(self.eddsaKey)
        msgHash = signer.hash(order)
        signedMessage = signer.sign(order)
        # update signaure
        order.update({
            "hash"     : str(msgHash),
            "eddsaSignature" : signedMessage
        })
        return order

    def cancel_order(self, orderHash, pair=None):
        """"""
        data = {
            "security": Security.EDDSA_SIGN
        }

        params = {
            "accountId": self.accountId,
            "orderHash": orderHash
        }

        response = self.request(
            method="DELETE",
            headers={
                "Content-Type" : "application/json",
                "Accept"       : "application/json",
            },
            path=f"/api/v3/order",
            params=params,
            data=data
        )

        json_resp = response.json()
        return json_resp

    def join_amm_pool(self, poolName, tokenAmounts, mintMinAmount, validUntil=None, storageIds=None, sigType=SignatureType.EDDSA):
        data = {"security": Security.API_KEY}
        req = self._create_join_pool_request(poolName, tokenAmounts, mintMinAmount, validUntil, storageIds)
        data.update(req)

        message = generateAmmPoolJoinEIP712Hash(req)
        # print(f"join message hash = {bytes.hex(message)}")
        if sigType == SignatureType.ECDSA:
            v, r, s = sig_utils.ecsign(message, self.ecdsaKey)
            data['ecdsaSignature'] = "0x" + bytes.hex(v_r_s_to_signature(v, r, s)) + EthSignType.EIP_712
        elif sigType == SignatureType.EDDSA:
            signer = MessageHashEddsaSignHelper(self.eddsaKey)
            data['eddsaSignature'] = signer.sign(message)

        self.add_request(
            method="POST",
            path="/api/v3/amm/join",
            callback=self.on_join_pool,
            params=req,
            data=data,
            extra=req
        )

    def _create_join_pool_request(self, poolName, joinAmounts, mintMinAmount, validUntil = None, storageIds = None):
        poolAddress = self.ammPoolNames[poolName]
        tokenAId, tokenBId = self.ammPools[poolAddress][:2]
        poolTokenId = self.ammPools[poolAddress][2]
        mintMinAmount = str(int(mintMinAmount * 10**self.tokenDecimals.get(poolTokenId, 8)))
        req = {
            'poolAddress': poolAddress,
            'owner': self.address,
            "joinTokens" : {
                "pooled" : [
                    {
                        "tokenId": tokenAId,
                        "volume" : str(int(joinAmounts[0] * 10**self.tokenDecimals[tokenAId]))
                    },
                    {
                        "tokenId": tokenBId,
                        "volume" : str(int(joinAmounts[1] * 10**self.tokenDecimals[tokenBId]))
                    },
                ],
                "minimumLp" : {
                    "tokenId" : poolTokenId,
                    "volume"  : mintMinAmount
                }
            },
            'storageIds': [self.offchainId[tokenAId], self.offchainId[tokenBId]] if storageIds is None else storageIds,
            'validUntil': 1700000000
        }

        if storageIds is None:
            self.offchainId[tokenAId]+=2
            self.offchainId[tokenBId]+=2
        return req

    def on_join_pool(self, data, request):
        print(f"PoolJoin success: hash={data['hash']}")

    def exit_amm_pool(self, poolName, burnAmount, exitMinAmounts, sigType=SignatureType.EDDSA):
        data = {"security": Security.API_KEY}
        req = self._create_exit_pool_request(poolName, burnAmount, exitMinAmounts)
        # print(f"create new order {order}")
        data.update(req)

        message = generateAmmPoolExitEIP712Hash(req)
        # print(f"join message hash = {bytes.hex(message)}")
        if sigType == SignatureType.ECDSA:
            v, r, s = sig_utils.ecsign(message, self.ecdsaKey)
            data['ecdsaSignature'] = "0x" + bytes.hex(v_r_s_to_signature(v, r, s)) + EthSignType.EIP_712
        elif sigType == SignatureType.EDDSA:
            signer = MessageHashEddsaSignHelper(self.eddsaKey)
            data['eddsaSignature'] = signer.sign(message)

        self.add_request(
            method="POST",
            path="/api/v3/amm/exit",
            callback=self.on_exit_pool,
            params=req,
            data=data,
            extra=req
        )

    def _create_exit_pool_request(self, poolName, burnAmount, exitMinAmounts):
        poolAddress = self.ammPoolNames[poolName]
        tokenAId, tokenBId = self.ammPools[poolAddress][:2]
        poolTokenId = self.ammPools[poolAddress][2]
        burnAmount = str(int(burnAmount * 10**self.tokenDecimals.get(poolTokenId, 18)))
        req = {
            'poolAddress': poolAddress,
            'owner': self.address,
            "exitTokens" : {
                "unPooled" : [
                    {
                        "tokenId": tokenAId,
                        "volume" : str(int(exitMinAmounts[0] * 10**self.tokenDecimals[tokenAId]))
                    },
                    {
                        "tokenId": tokenBId,
                        "volume" : str(int(exitMinAmounts[1] * 10**self.tokenDecimals[tokenBId]))
                    },
                ],
                "burned" : {
                    "tokenId" : poolTokenId,
                    "volume"  : burnAmount
                }
            },
            'storageId': self.offchainId[poolTokenId],
            'maxFee': str(int(int(exitMinAmounts[1])*0.002)),
            'validUntil': 1700000000
        }
        self.offchainId[poolTokenId]+=2
        return req

    def on_exit_pool(self, data, request):
        print(f"PoolExit success: hash={data['hash']}")

if __name__ == "__main__":
    loopring_rest_sample = LoopringV3Client()
    srv_time = loopring_rest_sample.query_srv_time()
    print(f"srv time is {srv_time}")
