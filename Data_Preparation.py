#########################
#### Python 3.10.11 #####
#########################

import yfinance as yf
import pandas as pd

# def get_name(symbol):
#     url = f'https://min-api.cryptocompare.com/data/coin/generalinfo?fsyms={symbol}&tsym=USD'
#     response = requests.get(url)
#     data = response.json()
#     name = data['Data'][0]['CoinInfo']['FullName']
#     return name

df = pd.read_csv('sym.csv', index_col=None)
x =  df['Symbol'].tolist()
# print(x)
# df = pd.DataFrame()

# count = 1
# len_df = 0
for Symbol in x:
    # print("Count :- ",count)
    print(Symbol)
    tickers = [f'{Symbol}-GBP']
    data = yf.download(tickers, period='max')
    data.drop("Adj Close", inplace=True, axis=1)
    data.drop("Volume", inplace=True, axis=1)
    # data['Symbol'] = Symbol
    # data['Cryptocurrency Name'] = get_name(Symbol)
    # len_df  += len(data)
    # df = df.append(data)
    # df = pd.concat([df, data], axis=0)
    # count += 1
    data.to_csv(f"{Symbol}_GBP.csv")
# print(len_df)
# df.to_csv("all_data.csv")
