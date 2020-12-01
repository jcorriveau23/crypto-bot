# BinanceBot

you need in the root folder a Keys.py file with your binance api keys writin as:

api_key = "your api public key"
api_secret = "your api private key"

# Libraries

pip install pyqt5
pip install python-binance

# to modify the ui with QTdesigner

1) open Qt designer
2) go to file => open and chose ui_main.py 
3) modify the ui with the tool
4) save it as the same name (erase the last one)
5) in the project repo in command line, enter: pyuic5 -o ui_main.py main.ui to create the ui_main.py
