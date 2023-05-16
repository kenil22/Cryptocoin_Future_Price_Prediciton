import yfinance as yf
import pandas as pd
import requests

# def get_name(symbol):
#     url = f'https://min-api.cryptocompare.com/data/coin/generalinfo?fsyms={symbol}&tsym=USD'
#     response = requests.get(url)
#     data = response.json()
#     name = data['Data'][0]['CoinInfo']['FullName']
#     return name

# tickers = [f'BTC-GBP']
# data = yf.download(tickers, period='max')
# data.drop("Adj Close", inplace=True, axis=1)
# data.drop("Volume", inplace=True, axis=1)
# data.to_csv(f"last_60_days_BTC_GBP.csv")

tickers = ['BTC-GBP']
data = yf.download(tickers, period='max')
data.drop("Adj Close", inplace=True, axis=1)
data.drop("Volume", inplace=True, axis=1)
last_60_days_data = data.tail(60)
data.to_csv(f"last_60_days_BTC_GBP.csv")