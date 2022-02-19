# Crypto-trading-bot

Simple trading bot that support binance and loopring DEX exchange using ccxt library and loopring sdk.

## Binance bot

Create in the root folder a Keys.py file with your binance api keys writin as:

api_key = "your binance api public key"

api_secret = "your binance api private key"

## Loopring bot

Create in the root folder a Keys.py file with your loopring exported account info writin as:

loopring_exported_account = {"your loopring exported account info"}

## Libraries

pip install pyqt5

pip install ccxt

## to modify the ui with QTdesigner

1) open Qt designer
2) go to file => open and chose **ui_main.py**
3) modify the ui with the tool
4) save it as the same name (erase the last one)
5) in the project repo in command line, enter: **pyuic5 -o ui_main.py** main.ui to create the **ui_main.py**
