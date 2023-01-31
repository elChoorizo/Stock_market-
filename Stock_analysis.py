# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:25:54 2022

@author: Thomas Chantoin
"""
import numpy as np
import pandas_datareader
from pandas_datareader import data as pdr
import datetime as dt
import pandas as pd
import yfinance as yf
#import fix_yahoo_finance 
yf.pdr_override()
import matplotlib.pyplot as plt
start = dt.datetime(2022, 6, 1)
end = dt.datetime(2023,1,30)
stock_name = "SOI.PA"
data = pdr.get_data_yahoo(stock_name, start)
data.head()
high_low = data['High'] - data['Low']
high_cp = np.abs(data['High'] - data['Close'].shift())
low_cp = np.abs(data['Low'] - data['Close'].shift())
df = pd.concat([high_low, high_cp, low_cp], axis=1)
true_range = np.max(df, axis=1)
average_true_range = true_range.rolling(25).mean()
#moving_average_25 =  data['Close'].rolling(50).mean()



#fig, ax = plt.subplots()
#average_true_range.plot(ax=ax)
#ax2 = data['Close'].plot(ax=ax, secondary_y=True, alpha=.5, color ='red')
#ax.set_ylabel("ATR")
#ax2.set_ylabel("Price")

fig, ax = plt.subplots(figsize=(10, 6), dpi = 400)
ax.set(title = stock_name)
ax2 = data['Close'].plot(ax=ax, secondary_y=False, alpha=.5, color ='red')
ax2.set_ylabel("Price")
ax3 = average_true_range.plot(ax=ax, secondary_y=True, alpha=.5, color ='blue')
ax3.set_ylabel("ATR")
fig, ax = plt.subplots(figsize=(10, 6), dpi = 400)
ax.set(title = stock_name)
ax2 = data['Close'].plot(ax=ax, secondary_y=False, alpha=.5, color ='red')
data['MA20'] = data['Close'].rolling(100).mean()
#data.tail()
data['EMA21'] = data['Close'].ewm(span=105, adjust=False).mean()
#data.tail()
#fig, ax = plt.subplots()
data[['MA20', 'EMA21']].loc['2019-01-01':].plot(ax=ax)
