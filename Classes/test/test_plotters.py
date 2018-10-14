import quandl
import pandas
import datetime
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, 'D:\Github\Algo_Trading\Classes')
import plotters


quandl.ApiConfig.api_key = 'JpGFAk7oxQcx3U1ygXrB'


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2018,1,1)
end = datetime.datetime.now();


# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
s = "AAPL"
apple = quandl.get("WIKI/" + s, start_date=start, end_date=end)



# Plot open 
x = plotters.open_close_plots()
x.open(apple)

# Plot close 
x = plotters.open_close_plots()
x.close(apple)

# Plot candlestick plot
y = plotters.candlestick_plot()
y.pandas_candlestick_ohlc(apple, "day", True)




