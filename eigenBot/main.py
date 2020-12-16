import pandas as pd
import datetime as dt
from pandas_datareader import DataReader
import yfinance as yf
import configparser

def  getTickerQuotes(ticker):
  # Get historical stock data
  tick = yf.Ticker(ticker)
  # print(tick.info)
  # get historical market data
  hist = tick.history(period="5d")
  return hist


def loadConfig():
  config = configparser.ConfigParser()
  config.read('../data/config.ini')
  return config


def createDataFrame(ticker):
  start, end = dt.datetime(2012, 1, 1), dt.datetime(2013, 12, 31)
  # tickers = ['AAPL', 'YHOO','GOOG', 'MSFT','ALTR','WDC','KLAC'] # moved these to data/config.ini
  prices = pd.DataFrame()

  # for ticker in tickers:
  #   print("prices array:\n", prices)
  #   print ("\nprices[ticker] array:\n", prices[ticker])

  prices[ticker] = DataReader(ticker,'yahoo', start, end).loc[:,'Close'] #S&P 500
  return prices.head()


if __name__ == "__main__":
  print("main function called")
  config = loadConfig()
  tickers = config['TICKERS']

  numTicks = 1
  hist = pd.DataFrame()
  for tick in tickers:
    print("\n\nTicker %s:\t%s" % (numTicks, tick))
    numTicks += 1
    data = getTickerQuotes(config['TICKERS'][tick])
    print("Datatype:\t %s\nData Array:\n%s" % (type(data), data['Close']))

