#import libraries
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#load the data
AAPL = pd.read_csv(r'C:\Users\aniaw\PycharmProjects\AAPL.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#print(AAPL)
'''
#Vizualize the data
plt.figure(figsize=(12.5, 4.5))
plt.plot(AAPL['Adj Close'], label='AAPL')
plt.title('Apple Adjusted Close Price History')
plt.xlabel('Sep.29, 2014 - Mar.29, 2018')
plt.ylabel('Adjusted Close Price in USD($)')
plt.legend(loc='upper left')
plt.show()
'''

#create simple moving averge over 30 days
SMA30 = pd.DataFrame()
SMA30['Adj Close'] = AAPL['Adj Close'].rolling(window=30).mean()
#print("The SMA30 is", SMA30)


#create a SMA100 average
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = AAPL['Adj Close'].rolling(window=100).mean()
print()
#print("The SMA100 is", SMA100)


'''
#Visualize this data
plt.figure(figsize=(12.5, 4.5))
plt.plot(AAPL['Adj Close'], label='AAPL')
plt.plot(SMA30['Adj Close'], label='SMA30')
plt.plot(SMA100['Adj Close'], label='SMA100')
plt.title('Apple Adjusted Close Price History')
plt.xlabel('Sep.29, 2014 - Mar.29, 2018')
plt.ylabel('Adjusted Close Price in USD($)')
plt.legend(loc='upper left')
plt.show()
'''

#Creating a new DataFrame to stora new data
data = pd.DataFrame()
data['AAPL'] = AAPL['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']
#print(data)

#Create a function that will return buy and sell price
def buy_and_sell(data):
    signalPriceBuy = []
    signalPriceSell = []
    flag = -1
    for i in range(len(data)):
        if (data['SMA30'][i]) > (data['SMA100'][i]):
            if(flag != 1):
                 signalPriceBuy.append(data['AAPL'][i])
                 signalPriceSell.append(np.nan)
                 flag = 1
            else:
                signalPriceBuy.append(np.nan)
                signalPriceSell.append(np.nan)
        elif (data['SMA30'][i]) < (data['SMA100'][i]):
            if (flag != 0):
                signalPriceBuy.append(np.nan)
                signalPriceSell.append(data['AAPL'][i])
                flag = 0
            else:
                signalPriceBuy.append(np.nan)
                signalPriceSell.append(np.nan)
        else:
            signalPriceBuy.append(np.nan)
            signalPriceSell.append(np.nan)


    return (signalPriceBuy, signalPriceSell)

#Store the buy and sell data into a variable(data)
buy_sell = buy_and_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#Show data
print(data)

#vizualize the data and the strategy to buy and sell
plt.figure(figsize=(12.6, 4.6))
plt.plot(data['AAPL'], label='AAPL', alpha= 0.35)
plt.plot(data['SMA30'], label='SMA30', alpha= 0.35)
plt.plot(data['SMA100'], label='SMA100', alpha= 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy Signal', marker='^', color= 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell Signal', marker='v', color= 'blue')
plt.title("Apple buy and sell signal")
plt.xlabel('Sep.29, 2014 - Mar.29, 2018')
plt.ylabel('Adjusted Close Price in USD($)')
plt.legend(loc='upper left')
plt.show()
