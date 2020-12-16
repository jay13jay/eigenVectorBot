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


if __name__ == "__main__":
  config, tickers = loadConfig()
  
  numTicks = 1
  for tick in tickers:
    data = getTickerQuotes(config['TICKERS'][tick])
    prices[tick] = DataReader(config['TICKERS'][tick],'yahoo', startTime, endTime).loc[:,'Close'] #S&P 500

  print("Data:\n", prices.head())
  returns = prices.pct_change()
  print("Percent Change:\n", returns.head())

