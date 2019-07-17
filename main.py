# for pumps only

import constants
import time
from ccxt.base.decimal_to_precision import decimal_to_precision as des
from ccxt.base.decimal_to_precision import TRUNCATE
from ccxt.base.decimal_to_precision import DECIMAL_PLACES

#import asyncio
import datetime
import matplotlib
import binance

api_key = 'add api key'
secret = 'add secrect'
binance.set(api_key, secret)  # setting up

boughtCryptos = {}

# reterives my btc balance
btcBalance = float(binance.balances()["BTC"]['free'])
print("Your bitcoin balance is %s" % btcBalance)  # my btc balance

symbol = input("what currency")+"BTC"  # symbol of first
symbol = symbol.upper()
print(symbol)

# dec.decimal_to_precision()

priceOfWanted = float(binance.prices()[symbol])  # how much coin->btc is worth
print(priceOfWanted)


# binance.or
# binance.order(symbol,binance.BUY,)
#exchange.enableRateLimit = True

def calculateProfit(coinPrice, boughtPrice): return coinPrice/boughtPrice


def calcAmountNeeded(coinAmount, Volume, percent):
    # volume = current have 0-> inf
    # percent = how much of btc 0->1
    # coinAmount = how much is coin in terms of btc
    coinsNeeded = (Volume*percent)/coinAmount
    return coinsNeeded


def sellPump(boughtPrice):
    # big function
    data = []
    data.append(float(binance.prices()[symbol]))
    for num in range(constants.MAXTIME):
        if num == 0:
            continue
        data.append(float(binance.prices()[symbol]))
        if calculateProfit(data[num], boughtPrice) >= constants.IDEALPROFIT:
            binance.order(symbol, binance.SELL, (btcBalance*constants.PERCENT) /
                          boughtPrice, data[num]*0.98, binance.LIMIT, binance.GTC, test=True)
            break
        # other stuff
        time.sleep(1)

    success = 'success' if len(data) < constants.MAXTIME else 'fail'
    print(success)
    currentPrice = binance.prices()[symbol]
    # check after a minute
    return


def visual(data):
    # matplotlib.
    return


if(btcBalance < priceOfWanted):
    ar = float(calcAmountNeeded(priceOfWanted, btcBalance, constants.PERCENT))
    ar = des(ar, TRUNCATE, 3, DECIMAL_PLACES)
else:
    ar = int(calcAmountNeeded(priceOfWanted, btcBalance, constants.PERCENT))

priceOfWanted = des(priceOfWanted, TRUNCATE, 8, DECIMAL_PLACES)


binance.order(symbol, binance.BUY, ar, priceOfWanted,
              binance.LIMIT, binance.GTC, test=True)
# print(ar,priceOfWanted*constants.MULT)
print("Amount:%s,Bought price:%s,Market Price:%s" %
      (ar, priceOfWanted, priceOfWanted))
print(datetime.datetime.now())
# sellPump(priceOfWanted*constants.MULT)
#boughtCryptos[symbol] = priceOfWqanted*constants.MULT
