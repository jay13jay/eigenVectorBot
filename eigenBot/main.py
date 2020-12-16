import pandas as pd
import datetime as dt
from pandas_datareader import DataReader
import yfinance as yf
import configparser

# Define Constants
startTime = dt.datetime(2012, 1, 1)
endTime = dt.datetime(2013, 12, 31)
prices = pd.DataFrame()


def  getTickerQuotes(ticker):
  # Get historical stock data
  tick = yf.Ticker(ticker)
  # print(tick.info)
  # get historical market data
  hist = tick.history(period="5d", start=startTime, end=endTime)
  return hist


def loadConfig():
  config = configparser.ConfigParser()
  config.read('data/config.ini')
  tickers = config['TICKERS']
  return config, tickers


def createDataFrame(ticker):
  start, end = dt.datetime(2012, 1, 1), dt.datetime(2013, 12, 31)
  prices = pd.DataFrame()

  # for ticker in tickers:
  #   print("prices array:\n", prices)
  #   print ("\nprices[ticker] array:\n", prices[ticker])

  prices[ticker] = DataReader(ticker,'yahoo', start, end).loc[:,'Close'] #S&P 500
  return prices.head()


if __name__ == "__main__":
  config, tickers = loadConfig()
  
  numTicks = 1
  for tick in tickers:
    data = getTickerQuotes(config['TICKERS'][tick])
    prices[tick] = DataReader(config['TICKERS'][tick],'yahoo', startTime, endTime).loc[:,'Close'] #S&P 500

    # print("Datatype:\t %s\nData Array:\n%s" % (type(data), data['Close']))
  print("Data:\n", prices.head())
  returns = prices.pct_change()
  print("Percent Change:\n", returns.head())

