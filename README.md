# data_science_bootcamp

Data visualization of bank's stock data from Yahoo Finance Data during the period from 01. January 2018 to 01. June 2021. Explorative data analysis to visualize effect of COVID-19 on stock market.

List of chosen banks with ticker codes:
1. Morgan Stanley (MS)
2. Goldman Sachs (GS)
3. JPMorgan Chase (JPM)
4. Bank of America (BAC)
5. Wells Fargo (WFC)
6. CitiGroup (C)

# Explorative Data Analysis:
1. Minimum closing price for all stocks from banks over the given time-frame
<img width="449" alt="minimum_closing_price" src="https://user-images.githubusercontent.com/51960581/130320442-1418aae2-1451-4e53-b92b-3c1e54236958.PNG">

2. Date of occurrence for worst one-day drop in returns:
<img width="323" alt="worst_one_day_drop" src="https://user-images.githubusercontent.com/51960581/130320449-e6573741-9958-4683-b85e-5f8be3f3e925.PNG">

3. Date of occurrence for best one-day gain in returns:
<img width="318" alt="best_one_day_gain" src="https://user-images.githubusercontent.com/51960581/130320455-5c8b5c33-5a15-4548-aa36-49a042073ca2.PNG">

4. Standard deviation - Higher value shows higher risk in returns:
<img width="385" alt="standard_deviation" src="https://user-images.githubusercontent.com/51960581/130320464-03bb5dea-0c14-42b1-bafd-8b5304dd4dee.PNG">

# Following data visualizations illustrate impact of COVID-19 on stock market for chosen banks (X-Axis Date, Y-Axis Return Value):

1. Pair Plot of Stock Returns:
![stock_returns](https://user-images.githubusercontent.com/51960581/130319822-43ce5328-c2f5-4412-b010-15ea9ed51c0d.png)

2. Distplot for JPMorgan Chase (JPM): Befor COVID-19, year 2018
![jpm_2018_std_dev](https://user-images.githubusercontent.com/51960581/130319868-2c6e2c0b-3a65-45b2-a35b-19c12ba9176e.png)
 
3. Distplot for JPMorgan Chase (JPM): During COVID-19, year 2020
![jpm_2020_std_dev](https://user-images.githubusercontent.com/51960581/130319903-8711d1f4-e63f-4029-aa93-d715665699ea.png)

4. Distplot for CitiGroup (C): Befor COVID-19, year 2018
![citigroup_2018_std_dev](https://user-images.githubusercontent.com/51960581/130319920-896c9769-b363-4c41-9543-d5df25913553.png)

5. Distplot for CitiGroup (C): During COVID-19, year 2020
![citigroup_2020_std_dev](https://user-images.githubusercontent.com/51960581/130319930-8f03f3fe-6515-428c-89e7-789d4d1d2917.png)

6. Line Plot for the Close Price over the entire period for each bank:
![line_plot_banks_common_drop_returns](https://user-images.githubusercontent.com/51960581/130320055-80611a7b-54c1-40e2-9ec2-a5a57b2ce400.png)

7. Plotly Line Plot for the Close Price over the entire period for each bank:
![plotly_plot_banks_common_drop_returns](https://user-images.githubusercontent.com/51960581/130320077-bcf7b365-1af3-44ea-b9da-06a7ba0a3789.png)

8. Line Plot for 30 day moving average for JPMorgan Chase stocks during time-frame 01.Jan 2020 to 01.Jan 2021:
![jpm_30_day_moving_avg_year_2020](https://user-images.githubusercontent.com/51960581/130320122-a11467f6-2ed7-42eb-b5ee-34e2c1b1159f.png)

9. Heat-map of correlation between the Close Price of stocks:
![heatmap_stocks_returns](https://user-images.githubusercontent.com/51960581/130320155-cfdcf349-8a75-463e-ad1d-cb337fb2924b.png)

10. Cluster-map of correlation between the Close Price of stocks:
![clustermap_stocks_returns](https://user-images.githubusercontent.com/51960581/130320171-f413ec7b-4de8-4570-8655-4cb90229dd71.png)
