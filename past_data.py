import yfinance as yf

# def get_future_price(tickers='ETH-GBP', period_tag='1M'):


# tickers = [ cryptocoin_dict[tickers]]
def historical_data_func(tickers='ETH-GBP', period_tag='1mo'):
    cryptocoin_dict = {'DOGE':'DOGE-GBP', 'BNB':'BNB-GBP', 'BTC':'BTC-GBP', 'ETH':'ETH-GBP', 'USDT':'USDT-GBP'}
    # tickers = ['DOGE-GBP']
    data = yf.download(cryptocoin_dict[tickers], period=period_tag)
    data.drop("Adj Close", inplace=True, axis=1)
    data.drop("Volume", inplace=True, axis=1)
    data.drop("Open", inplace=True, axis=1)
    data.drop("High", inplace=True, axis=1)
    data.drop("Low", inplace=True, axis=1)
    data.reset_index(inplace=True)
    date_list = data['Date'].astype(str).tolist()
    closing_price_list = data['Close'].tolist()

    return date_list, closing_price_list