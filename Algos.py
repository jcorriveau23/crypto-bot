
class Algo():
    def __init__(self, type):
        self.type = "jfz"
        self.last_buys = {}
        self.last_sells = {}
        self.buy_coefs = 2
        self.buy_qtys = []
        self.sell_coefs = 2
        self.buyPrices = []
        self.nb_sells = 0
        self.nb_buys = 0

    def jfz_algo_create_buys(self, balance, start_price, loss_depth, buys_nb_depth, buy_more_pourcent):
        lowest_price = start_price * (1 - loss_depth)

        buy_coef = 1 - (lowest_price/start_price)**(1/buys_nb_depth)

        buy_qty = []
        mult = []
        buy_price = start_price

        for i in range(buys_nb_depth):
            buy_price *= (1 - buy_coef)
            self.buyPrices.append(buy_price)

            buy_qty.append(buy_more_pourcent**i)

            mult.append(buy_qty[i]*self.buyPrices[i])
        print("buy price list value: {}".format(self.buyPrices))

        start_qty = balance/sum(mult)
        qty = start_qty
        for i in range(buys_nb_depth):
            self.buy_qtys.append(qty)
            qty *= buy_more_pourcent
        print("buy qty list value: {}".format(self.buy_qtys))

a = Algo("jfz")
a.jfz_algo_create_buys(2000, 600, 0.3, 23, 1.08)

## copie paste de lalgo sur lautre fichier repo
#
# def calculate_trigger_prices(pair):
#
#     vente_possible = Data.LastBuys[pair]['Nb'] - Data.LastSells[pair]['Nb']   #nb d'achat qui est passible d'une vente
#
#     lenLastBuys = len(Data.LastBuys[pair]['List'])
#     lenLastSells = len(Data.LastSells[pair]['List'])                       #nb de vente consécutive
#     #Best price to compare to (offset to point on the good last buy)
#     offset = lenLastBuys - 1 - vente_possible
#     Last_Buy = float(Data.LastBuys[pair]['List'][offset]['Price'])  # le Last_Buy est celui qui n'est pas des miettes
#     if lenLastSells > 0:
#         Last_Sell = float(Data.LastSells[pair]['List'][0]['Price'])
#     #to display on the GUI
#     Data.NbVentePossible[pair] = vente_possible
#
#     #Si aucun achat de realise (condition initiale + pas de vente permise)
#     if ((vente_possible == 0) and (lenLastSells == 0)):
#         Data.BuyPrice[pair] = Last_Buy - (Data.Buy_multiplication_list[pair][vente_possible] ** 1.3) * 0.0025 * Last_Buy
#         Data.SellPrice[pair] = 999999
#     #Si aucun achat restant et ventes réalisés dans le passé (on se base sur la derniere vente + Pas de vente permise)
#     elif ((vente_possible == 0) and (lenLastSells > 0)):
#         Data.LastSells[pair]['List'].clear()
#         Data.BuyPrice[pair] = Last_Sell - (Data.Buy_multiplication_list[pair][vente_possible] ** 1.3) * 0.0025 * Last_Sell #cas speciale,
#         Data.SellPrice[pair] = 999999
#     #Si achats dans lasBuys (on se base sur les derniers achats)
#     else:
#         Data.BuyPrice[pair] = Last_Buy - (Data.Buy_multiplication_list[pair][vente_possible] ** 1.3) * 0.0025 * Last_Buy
#         Data.SellPrice[pair] = Last_Buy + (Data.Sell_multiplication_list[pair][lenLastSells] ** 1.2) * 0.00255 * Last_Buy
#
#
#
# def Verif_Achat(pair):
#     # Verifie l'achat et ajoute celle-ci aux lasbuys
#     if (order_filled("Buy", pair) == True):
#         # Un achat de plus
#         Data.LastBuys[pair]['Nb'] += 1
#         LastBuys_price_average()
#         #RefreshLastBuysSells()
#         #Nouveau prix de vente et d achat
#         calculate_trigger_prices(pair)
#         # Combien de vente possible
#         nb_vente_possible = Data.LastBuys[pair]['Nb'] - Data.LastSells[pair]['Nb']
#         #Refer to list in Data.py to for buy Qty
#         nb_achat = Data.Buys_Qty[pair][nb_vente_possible]
#         # Nouvelle achat
#         Acheter(prix=Data.BuyPrice[pair], nb_achat=nb_achat, pair= pair)
#         # si plus d'une vente possible
#         if (nb_vente_possible > 1):
#             # il y avait une vente
#             cancel_order("Sell", pair)
#         # nouvelle vente (Quantité acheté
#         ####################################################################################
#         #ALGO AGRESSIF
#         nb_vente = Data.LastBuys[pair]['Qty']/(nb_vente_possible)
#         ####################################################################################
#         #nb_vente = Data.LastBuys[pair]['List'][0]['Qty']
#         Vendre(prix=Data.SellPrice[pair], nb_vente=nb_vente, pair=pair)
#
# def Verif_Vente(pair):
#     if (len(Data.LastBuys[pair]['List']) > 1):
#         # Verifie la vente et ajoute celle-ci aux lasBuys
#         if (order_filled("Sell", pair) == True):
#             # Une vente de plus
#             Data.LastSells[pair]['Nb'] += 1
#             LastBuys_price_average()
#             #RefreshLastBuysSells()
#             #Calculer prochain les prix d'achat et de vente
#             calculate_trigger_prices(pair)
#             # On cancele lordre dachat pour la mettre a jour avec la derniere vente
#             cancel_order("Buy", pair)
#             # combien de vente possible maintenant ?
#             nb_vente_possible = Data.LastBuys[pair]['Nb'] - Data.LastSells[pair]['Nb']
#             # Refer to list in Data.py to for buy Qty
#             nb_achat = Data.Buys_Qty[pair][nb_vente_possible]
#             Acheter(prix=Data.BuyPrice[pair], nb_achat=nb_achat, pair=pair)
#
#             if (nb_vente_possible > 0):
#                 # nouvelle vente or (Data.LastBuys[0]['Qty']
#                 ####################################################################################
#                 # ALGO AGRESSIF
#                 nb_vente = Data.LastBuys[pair]['Qty']/(nb_vente_possible)
#                 ####################################################################################
#                 #nb_vente = Data.LastBuys[pair]['List'][0]['Qty']
#                 Vendre(prix=Data.SellPrice[pair], nb_vente=nb_vente, pair=pair)
#
#
# def Main():
#     labelRunning.config(text='Le programme Run mon homme !')
#     breakout = root.after(4500, Main)
#     if (Data.start == True):
#
#         try:
#             get_Prix()
#             price_mean_2min()
#             price_mean_30min()
#             get_NbCryp()
#         except Timeout:
#             # write event to logfile
#             fichier.write('FAILLLLLLLLLLLLLLLLLLLLLLLLLLL   \n')
#             Data.nb_Timeout += 1
#             pass
#
#         except ConnectionError:
#             # write event to logfile
#             fichier.write('FAILLLLLLLLLLLLLLLLLLLLLLLLLLL   \n')
#             Data.nb_ConnectionError += 1
#             pass
#         for pair in Data.LastBuys.keys():
#             # Regarder si la vente ou lachat a été filled
#             Verif_Achat(pair)
#             Verif_Vente(pair)
#             #shadow_Sell()
#             print(str(Data.LastBuys))
#             print(str(Data.LastSells))
#             print(str(Data.mean2min))
#             #print("ShadowSellPrice: {}".format(Data.ShadowPrice))
#             #print(Data.Buy_multiplication_list['ETHUSDT'])
#             #print(Data.Sell_multiplication_list['ETHUSDT'])
#             # Fonction de vérification d'achat au 30 min
#             # TirtyMin()
#             Data.SellAllNowGain[pair] = Data.gain[pair] + Data.LastBuys[pair]['Qty'] * Data.BidPrice[pair]
#             RefreshApp()
#             log_condition()