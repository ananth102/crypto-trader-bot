

import constants
import time
import main
from ccxt.base.decimal_to_precision import decimal_to_precision as des
from ccxt.base.decimal_to_precision import TRUNCATE
from ccxt.base.decimal_to_precision import DECIMAL_PLACES

#import asyncio
import datetime
import matplotlib
import binance

api_key = 'fpbbveGPWhP0r0ozRpfMdKkMfwhD1J6lGBVpzqIZW3IcA7NQ06kYT9p9uF37nCXz'
secret = 'gUie4OPO6F3O1IME54dOMQdiMraQHRmC9H3qfA9p4zunPUl9iRpCOOJ3dhJybl1n'
binance.set(api_key,secret) # setting up

btcBalance = float(binance.balances()["BTC"]['free']) # reterives my btc balance
print("Your bitcoin balance is %s"%btcBalance) # my btc balance


def testforNumberErrors():
    list = binance.balances()
    for sym in list:
        if(sym == "USDT" or sym == "BTC"):continue

        sym = sym + "BTC"

        pof = float(binance.prices()[sym])
        if (btcBalance < pof):
            are = float(main.calcAmountNeeded(pof, btcBalance, constants.PERCENT))
            are = des(are, TRUNCATE, 3, DECIMAL_PLACES)
        else:
            are = int(main.calcAmountNeeded(pof, btcBalance, constants.PERCENT))

        try:

            pof = des(pof, TRUNCATE, 8, DECIMAL_PLACES)
            binance.order(sym, binance.BUY, are, pof, binance.LIMIT, binance.GTC,test=True)
        except Exception as e:
            print(e)
            print(sym)
        finally:
            time.sleep(1)
            print(sym)

    return
