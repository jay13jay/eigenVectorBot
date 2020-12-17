import eigenBot
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# Set constants
startTime = dt.datetime(2012, 1, 1)
endTime = dt.datetime(2013, 12, 31)
prices = pd.DataFrame()


if __name__ == "__main__":
    config, tickers = eigenBot.loadConfig()

    numTicks = 1
    for tick in tickers:
        prices[tick] = eigenBot.getTickerQuotes(config, tick, startTime, endTime)


    returns = prices.pct_change()
    #   print("Data:\n", prices.head())
    #   print("Percent Change:\n", returns.head())

    returns = returns.iloc[1:, :] # Remove first row of NA's
    training_period = 30
    in_sample = returns.iloc[:(returns.shape[0]-training_period), :].copy()
    
    # Save the tickers
    tickList = returns.columns.copy()

    # Set up plotting
    covariance_matrix = in_sample.cov()
    
    D, S = np.linalg.eigh(covariance_matrix)
    eigenportfolio_1 = S[:,-1] / np.sum(S[:,-1]) # Normalize to sum to 1
    eigenportfolio_2 = S[:,-2] / np.sum(S[:,-2]) # Normalize to sum to 1


    # Setup Portfolios
    eigenportfolio = pd.DataFrame(data= eigenportfolio_1, columns = ['Investment Weight'], index = tickers)
    eigenportfolio2 = pd.DataFrame(data= eigenportfolio_2, columns = ['Investment Weight'], index = tickers)
    
    # Plot
    # %matplotlib inline
    f = plt.figure()
        
    ax = plt.subplot(121)
    eigenportfolio.plot(kind='bar', ax=ax, legend=False)
    plt.title("Max E.V. Eigenportfolio")
    ax = plt.subplot(122)
    eigenportfolio2.plot(kind='bar', ax=ax, legend=False)
    plt.title("2nd E.V. Eigenportfolio")

    plt.show()
