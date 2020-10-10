import os
import bs4
import xlrd
import requests
from stocks import *
from bs4 import BeautifulSoup



def getPrice(ticker):
    url = "https://google.com/search?q={}+stock".format(ticker)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    p = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).find("div").text
    p = p[:p.find(" ")].replace(",", "")
    return float(p)

def getPrices():
    # Return tuple of ticker and the current price
    good = 0
    bad = 0
    for (name, ticker, _, _, _, _) in stocks:
        try:
            yield name, ticker, getPrice(ticker)
            good += 1
        except AttributeError:
            bad += 1
