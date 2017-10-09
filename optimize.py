# Pick 4 stocks and optimize allocation of Rs. 100000 and find out the portfolio worth by considering
# the time frame of 6 months in histor

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo
import math

# Function to load stock data
def load_data(symbols, dates):
    # Creating consisting Dataframe for the required date range
    df = pd.DataFrame(index= dates)

    # Parsing symbols and loading corresponding symbol stock data
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(str(symbol)), usecols=['Date', 'Adj Close'], index_col='Date',
                              na_values = ['nan'], parse_dates = True, dayfirst='True')

        # Renaming Adj Close column to symbol name
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        # Joining data range dataframe with the dataframe consisting symbol stock data
        df = df.join(df_temp, how='inner')

        df[symbol] = df[symbol].astype(float)

        # Dropping NaN data
        df = df.dropna()
    return df

# Function to calculate daily returns
def get_daily_return(df):
    daily_return = df.copy()
    daily_return[1:] = (df[1:] / df[:-1].values) - 1
    daily_return.ix[0] = 0
    return daily_return

# Function to calculate portfolio value
def get_portfolio_value(df):
    portfolio_daily_return = df.sum(axis=1)
    return portfolio_daily_return

# Function to get risk free rate
def get_riskfree_rate(rate, n):
    return (1.0 + rate/100)**(1. /n) - 1

# Function to calculate Sharpe Ratio for the portfolio
def getSR(allocs, df, rf):
    capital = 100000

    df = allocs * df
    df = df * capital

    port_val = get_portfolio_value(df)
    daily_returns = get_daily_return(port_val)

    # Calculating Mean and Standard Deviation of the portfolio daily return
    rp = daily_returns.mean()
    std = daily_returns.std()

    # SR formula
    SR = math.sqrt(242) * (rp - rf)/std
    return -SR


if __name__ == "__main__":
    # Initial Allocation Ratios w.r.t. to total capital
    allocs = [0.25, 0.25, 0.25, 0.25]

    # Define Date Range
    dates = pd.date_range('2017-04-06', '2017-10-06')

    # Stock Symbols To Read
    symbols = ['INFY', 'HDFCBANK', 'LT', 'ICICIBANK']

    # Get Stock Data
    df = load_data(symbols, dates)

    share_price = df.ix[0,:].values

    # Normalizing Stock Data
    df = df / df.ix[0, :]

    # Capital of Investment
    capital = input('Enter Capital to be Invested:')

    # Calculating risk free rate
    n = 248  # number of trading days
    rate = input('Enter savings intrest rate:')  # interest rate

    # Calculating Risk Free Rate w.r.t. interest rate provided for the period of 6 months with daily sampling of data
    rf = get_riskfree_rate(rate, n)

    # Optimizing the portfolio to gain maximum Sharpe Ratio
    result = spo.minimize(getSR, np.array(allocs), args=(df, rf), method='SLSQP', options={'disp': True},
                          bounds=((0.0, 1.0), (0.0, 1.0), (0.0, 1.0), (0.0, 1.0)),
                          constraints= {
                                  'type' : 'eq',
                                  'fun' : lambda x : sum(x) -1.0
                          })

    # Converting Allocated Ratios to Amount
    amount =  np.array(result.x *capital, dtype=int)

    # Calculating portfolio value w.r.t. optimized allocations
    df = result.x * df
    df = df * capital

    port_val = get_portfolio_value(df)

    # Loading Market Index data to calculate returns if same capital was invested in the index
    df_nifty = load_data(['NIFTY'], dates)

    df_nifty = df_nifty / df_nifty.ix[0, :]

    df_nifty = df_nifty * capital

    # Finding number of shares that should have been bought to achieve the optimized target amount
    no_shares =  amount/share_price

    # Printing the final result
    print('The optimum number of shares to buy and corresponding amount is:\n')
    for i in range(0, len(symbols)):
        print symbols[i]
        print '--------------------------'
        print 'No. Shares: ', no_shares[i]
        print  'Investment Amount: ', amount[i]
        print '\n'

    # Plotting comparative graph of nifty and portfolio
    ax = df_nifty.plot(title = 'Portfolio Optimization')
    ax.plot(port_val, label='Portfolio')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show(ax)

