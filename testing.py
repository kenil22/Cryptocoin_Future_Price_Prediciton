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
x = float(x)
print(type(x))
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




# dataframe_with_information['Date'] = dataframe_with_information['Date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%m/%d"))

# print(last_60_days_tail)
# print(f"{Cryptocoin_Symbol} price for {Date} is {Result}")
# print(dataframe_with_information.columns)

# fig = go.Figure(data=go.Scatter(x=dataframe_with_information['Date'], y=dataframe_with_information['Close'], mode='lines'))
# fig.update_layout(
#     title='Bitcoin Closing Prices',
#     xaxis=dict(title='Date'),
#     yaxis=dict(title='Closing Price'),
#     hovermode='closest',
#     width=800,  # Convert inches to pixels (1 inch = 96 pixels)
#     height=400
# )

# Add custom hover labels using the 'text' attribute
# fig.update_traces(text=dataframe_with_information['Date'] + '<br>' + dataframe_with_information['Close'].astype(str),
#                   hovertemplate='%{text}')

# Save the figure as HTML file
# fig.write_html('graph.html')



# plt.figure(figsize=(10, 6)) 
# plt.plot(dataframe_with_information['Date'], dataframe_with_information['Close'])
# plt.title('Bitcoin Closing Prices')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')
# # Enable hover functionality with tooltips
# def hover(event):
#     if event.inaxes == plt.gca():
#         index = int(event.xdata)
#         date = dataframe_with_information['Date'].iloc[index]
#         closing_price = dataframe_with_information['Close'].iloc[index]
#         plt.gca().set_title(f"Date: {date}\nClosing Price: {closing_price}", fontsize=10)
#         plt.gcf().canvas.draw_idle()

# plt.gcf().canvas.mpl_connect('motion_notify_event', hover)
# plt.savefig('graph.png')
# plt.show()




