# import pands, numpy, pandas_datareader to get bank data from yahoo finance data
from pandas_datareader import data as web
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# define start date and end date
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2021, 6, 1)

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

# print(bank_stocks.tail(10))

# set column name levels
bank_stocks.columns.names = ['Bank Ticker Name', 'Stock Information']

# print(bank_stocks.tail(10))

# EDA: Explorative Data Analysis

# get minimum closing price for all stocks from banks over the given time-frame
minimum_closing_price = bank_stocks.xs(key='Close', axis=1, level='Stock Information').min()
# print(minimum_closing_price)

# get returns for each bank's stock using percentage change between current and prior element
returns = pd.DataFrame()
for tick in tickers:
    returns[tick + ' Return'] = bank_stocks[tick]['Close'].pct_change()

# print(returns.head(10))

# create a pairplot using seaborn
sns.pairplot(returns[1:])
plt.show()