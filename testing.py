import yfinance as yf

# def get_future_price(tickers='ETH-GBP', period_tag='1M'):


# tickers = [ cryptocoin_dict[tickers]]
# def historical_data_func(tickers='ETH-GBP', period_tag='1mo'):
# tickers = ['DOGE-GBP']
data = yf.download(['BTC-GBP'], period='1mo')
data.drop("Adj Close", inplace=True, axis=1)
data.drop("Volume", inplace=True, axis=1)
data.drop("Open", inplace=True, axis=1)
data.drop("High", inplace=True, axis=1)
data.drop("Low", inplace=True, axis=1)
data.reset_index(inplace=True)
x = data['Close'].iloc[-1]

Bitcoins = 5
Buying_Price = 50
Current_price = 10
Profit = Current_price*Bitcoins - Buying_Price*Bitcoins 
if Profit < 0:
    print(f"Loss of {abs(Profit)}")
else:
    print(f"Profit of {Profit}")
    


# import datetime
# from datetime import datetime, timedelta
# date_str = '2023-05-10'
# date = datetime.strptime(date_str, '%Y-%m-%d')

# # Add one day to the date
# new_date = date + timedelta(days=1)

# # Convert the new date to a string
# new_date_str = new_date.strftime('%Y-%m-%d')

# print(new_date_str)






# import requests
# import pandas as pd

# df = pd.read_csv('sym.csv', index_col=None)
# x =  df['Symbol'].tolist()

# def get_name(symbol):
#     url = f'https://min-api.cryptocompare.com/data/coin/generalinfo?fsyms={symbol}&tsym=USD'
#     response = requests.get(url)
#     data = response.json()
#     name = data['Data'][0]['CoinInfo']['FullName']
#     return name

# for sym in x:
#     print(sym)
#     print(get_name(sym))
#     print("++++++++++++++++++++++++++")
