
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from binance.client import Client
from binance.enums import *

import Keys

class API():
    def __init__(self):
        self.client = Client(api_key=Keys.api_key, api_secret=Keys.api_secret)
        self.info = self.client.get_exchange_info()