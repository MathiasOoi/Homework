import os
import bs4
import xlrd
import requests
from stocks import *
from bs4 import BeautifulSoup



def getPrice(ticker):
    url = "https://google.com/search?q={}+stock".format(ticker)
    print(url)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    p = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
    p = p.find("div").text
    p = p[:p.find(" ")].replace(",", "")
    return float(p)

if __name__ == '__main__':
    good = 0
    bad = 0
    for (name, ticker, _, _, _, _) in stocks:
        try:
            print(name, ticker)
            print(getPrice(ticker))
            good += 1
        except AttributeError:
            print("ERROR", name, ticker)
            bad += 1
    print("Good: {}/{}".format(good, good+bad))
    print("Bad: {}/{}".format(bad, good+bad))