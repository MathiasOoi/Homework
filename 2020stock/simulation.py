import os
import time
import numpy as np
import pandas as pd
from spreadsheet import *
from scraper import *


if __name__ == '__main__':
    # Iterate over stock prices (Daily)
    sp = Sheet()
    for name, ticker, price in getPrices():
        print(name, ticker, price)
        print(type(ticker))
        try:
            sp.createNewWkst(ticker, 200, 20)
        except:
            sp.createNewWkst(("\\" + str(ticker)), 200, 20)

