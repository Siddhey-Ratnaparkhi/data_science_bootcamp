# import pandas, datetime, pandas data reader to get bank data from yahoo finance data
from pandas_datareader import data as web
import pandas as pd
import datetime


# define start date and end date
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2021, 6, 1)
explore_data_insights = 'YES'

# Bank of America
BAC = web.DataReader("BAC", 'yahoo', start, end)

# CitiGroup
C = web.DataReader("C", 'yahoo', start, end)

# Goldman Sachs
GS = web.DataReader("GS", 'yahoo', start, end)

# JPMorgan Chase
JPM = web.DataReader("JPM", 'yahoo', start, end)

# Morgan Stanley
MS = web.DataReader("MS", 'yahoo', start, end)

# Wells Fargo
WFC = web.DataReader("WFC", 'yahoo', start, end)

# list of ticker symbols in alphabetical order
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

# concatenate all stocks together
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)

# set column name levels
bank_stocks.columns.names = ['Bank Ticker Name', 'Stock Information']

# get returns for each bank's stock using percentage change between current and prior element
returns = pd.DataFrame()
for tick in tickers:
    returns[tick + ' Return'] = bank_stocks[tick]['Close'].pct_change()

# EDA: Explorative Data Analysis
if explore_data_insights == 'YES':

    # get minimum closing price for all stocks from banks over the given time-frame
    minimum_closing_price = bank_stocks.xs(key='Close', axis=1, level='Stock Information').min()
    print('Minimum closing price for all stocks from banks over the given time-frame:\n{}'.format(minimum_closing_price))

    # check the date on occurrence of worst drop in returns
    print('Date of occurrence for worst one-day drop in returns:\n{}'.format(returns.idxmin()))

    # check the date on occurrence of best gain in returns
    print('Date of occurrence for best one-day gain in returns:\n{}'.format(returns.idxmax()))

    # check standard deviation for each stock. higher value shows risk in returns
    print('Standard deviation - Higher value shows higher risk in returns:\n{}'.format(returns.std()))
