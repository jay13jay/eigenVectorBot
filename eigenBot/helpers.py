import configparser
import yfinance as yf
from pandas_datareader import DataReader


def  getTickerQuotes(config, tick, start, end): 
    prices = DataReader(config['TICKERS'][tick],'yahoo', start, end).loc[:,'Close'] #S&P 500
    return prices


def loadConfig():
    config = configparser.ConfigParser()
    config.read('data/config.ini')
    tickers = config['TICKERS']
    return config, tickers