# Yahoo finance Python script that plots the coorelation between coins
# Analyzing Cryptocurrencies in Python
# NeuralNine Youtube Channel
# https://www.youtube.com/watch?v=HqGlkACB3rg

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yf
import seaborn as sns
import datetime as dt  

currency = "USD"
metric = "Close"

start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()


crypto = ['BTC', 'ETH', 'HEX', 'MATIC', 'DOT', 'FTM', 'ANC', 'TERRA']
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

#COORELATION CHART
#COMMENT OUT COORELATION HEATMAP BEFORE USING
plt.yscale('log')

for ticker in crypto:
   plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")

#COORELATION HEATMAP
#COMMENT OUT COORELATION CHART BEFORE USING
# combined = combined.pct_change().corr(method="pearson")
# sns.heatmap(combined, annot=True, cmap="coolwarm")


plt.show()




