#########################
#### Python 3.10.11 #####
#########################

import yfinance as yf
import pandas as pd

df = pd.read_csv('sym.csv', index_col=None)
x =  df['Symbol'].tolist()

for Symbol in x:
    tickers = [f'{Symbol}-GBP']
    data = yf.download(tickers, period='max')
    data.drop("Adj Close", inplace=True, axis=1)
    data.drop("Volume", inplace=True, axis=1)
    data.to_csv(f"{Symbol}_GBP.csv")
