# import fetch_yahoo_finance_data, pandas, seaborn, matplotlib
from fetch_yahoo_finance_data import bank_stocks, returns, tickers
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # select function name amongst: Pair Plot, Distplot, Lineplot, Plotly Lineplot, Moving Average, Heatmap, Clustermap
    function_name = 'SELECT FUNCTION NAME OF THE PLOT'

    if function_name == 'Pair Plot':
        pairplot()
    elif function_name == 'Distplot':
        distplot()
    elif function_name == 'Lineplot':
        lineplot()
    elif function_name == 'Plotly Lineplot':
        plotly_lineplot()
    elif function_name == 'Moving Average':
        moving_average()
    elif function_name == 'Heatmap':
        heatmap()
    elif function_name == 'Clustermap':
        clustermap()
    else:
        print('Input valid function name of visualization plot: Pair Plot, Distplot, Lineplot, Plotly Lineplot, Moving Average, Heatmap, Clustermap')


# create a pairplot using seaborn
def pairplot():
    sns.pairplot(returns[1:])
    return plt.show()

# create distplot for the year 2020 returns for JPMorgan Chase
def distplot():
    sns.distplot(returns.loc['2020-01-01':'2020-12-31']['JPM Return'], color='blue', bins=50)
    return plt.show()

# create line plot for the Close Price over the entire period for each bank
def lineplot():
    df = bank_stocks.xs(key='Close',axis=1,level='Stock Information')
    df.plot()
    return plt.show()

# create line plot using plotly for gaining more insights over specific time-frame
def plotly_lineplot():
    pd.options.plotting.backend = "plotly"
    df = bank_stocks.xs(key='Close',axis=1,level='Stock Information')
    fig = df.plot.area()
    return fig.show()

# 30 day moving average for JPMorgan Chase stocks during time-frame 01.Jan 2020 to 01.Jan 2021
def moving_average():
    plt.figure(figsize=(12,6))
    bank_stocks['JPM']['Close'].loc['2020-01-01':'2021-01-01'].rolling(window=30).mean().plot(label='30 Day Moving Average')
    bank_stocks['JPM']['Close'].loc['2020-01-01':'2021-01-01'].plot(label='JPM CLOSE')
    plt.legend()
    return plt.show()

# create heat-map of correlation between the Close Price of stocks
def heatmap():
    sns.heatmap(bank_stocks.xs(key='Close', axis=1, level='Stock Information').corr(), annot=True)
    return plt.show()

# create cluster-map of correlation between the Close Price of stocks
def clustermap():
    sns.clustermap(bank_stocks.xs(key='Close', axis=1, level='Stock Information').corr(), annot=True)
    return plt.show()




if __name__ == "__main__":
    main()