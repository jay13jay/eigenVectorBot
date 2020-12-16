import eigenBot
import datetime as dt
import pandas as pd


# Set constants
startTime = dt.datetime(2012, 1, 1)
endTime = dt.datetime(2013, 12, 31)
prices = pd.DataFrame()


if __name__ == "__main__":
  config, tickers = eigenBot.loadConfig()
  
  numTicks = 1
  for tick in tickers:
    prices[tick] = eigenBot.getTickerQuotes(config, tick, startTime, endTime)

  print("Data:\n", prices.head())
  returns = prices.pct_change()
  print("Percent Change:\n", returns.head())