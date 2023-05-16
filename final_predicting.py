#Get the last 60 day closing price values and convert the datadrame to an array
# last_60_days = data[-60:].values

# def predict_close_price(tickers='DOGE-GBP', Input_Date='2023-05-15')
import datetime
from datetime import datetime, timedelta
import datetime as dt
import pandas as pd
import os
import matplotlib.pyplot as plt
# import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
scaler = MinMaxScaler(feature_range=(0,1))
import numpy as np
import plotly.graph_objects as go

#################################################################################
# !pip install yfinance
import yfinance as yf

# tickers='DOGE-GBP'
# Input_Date='2023-05-18'
# model_1 = load_model('models\\DOGE_GBP.h5', compile=False)
def get_future_price(tickers='ETH-GBP', Input_Date='2023-05-18'):

    cryptocoin_model_dict = {'DOGE':'DOGE_GBP.h5', 'BNB':'BNB_GBP.h5', 'BTC':'BTC_GBP.h5', 'ETH':'ETH_GBP.h5', 'USDT':'USDT_GBP.h5'}
    cryptocoin_dict = {'DOGE':'DOGE-GBP', 'BNB':'BNB-GBP', 'BTC':'BTC-GBP', 'ETH':'ETH-GBP', 'USDT':'USDT-GBP'}

    model_1 = load_model(f'models\\{cryptocoin_model_dict[tickers]}', compile=False)
    tickers = [ cryptocoin_dict[tickers]]
    data = yf.download(tickers, period='max')
    data.drop("Adj Close", inplace=True, axis=1)
    data.drop("Volume", inplace=True, axis=1)
    data.drop("Open", inplace=True, axis=1)
    data.drop("High", inplace=True, axis=1)
    data.drop("Low", inplace=True, axis=1)
    last_60_days_tail = data.tail(60)
    last_60_days_tail.reset_index(inplace=True)
    # print(last_60_days_tail)
    last_60_days = last_60_days_tail.filter(['Close'])
    #################################################################################
    data.reset_index(inplace=True)
    # print(data)
    # Input_Date = '2023-05-15'
    # print(last_60_days)

    # date_str = Input_Date
    # print(last_60_days.reset_index(inplace=True))
    # print(last_60_days['Date'].iloc[-1])
    # last_60_days = last_60_days.filter(['Close'])
    last_60_days_tail['Date'] = pd.to_datetime(last_60_days_tail['Date']).dt.strftime('%Y-%m-%d')

    date_str = str(last_60_days_tail['Date'].iloc[-1])
    # print(last_60_days_tail)
    # date_str = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').date()
    date_str = str(date_str)
    while(last_60_days_tail['Date'].iloc[-1] != Input_Date):
        date_str = str(last_60_days_tail['Date'].iloc[-1])
        # print(date_str)
        # date_str = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').date()
        date_str = str(date_str)
        # print(date_str)
        date = datetime.strptime(date_str, '%Y-%m-%d')
        new_date = date + timedelta(days=1)
        date_str = new_date.strftime('%Y-%m-%d')
        # print(last_60_days_tail)
        last_60_days_tail.reset_index(inplace=True)
        # print(last_60_days_tail)
        last_60_days = last_60_days_tail.filter(['Close'])
        # Scale the data to be values between 0 and 1
        scaler = MinMaxScaler(feature_range=(0,1))
        # print(last_60_days.shape)
        # print(last_60_days)
        last_60_days_scaled = scaler.fit_transform(last_60_days)
        # create an empty list
        new_X_test = []
        # Append the past 60 days
        new_X_test.append(last_60_days_scaled)
        # Convert the X_test data set to a numpy array
        new_X_test = np.array(new_X_test)
        # Reshape the data 
        new_X_test = np.reshape(new_X_test, (new_X_test.shape[0], new_X_test.shape[1], 1))
        # print(new_X_test.shape)
        # Get the predicted scaled price
        # model_1 = load_model('DOGE_GBP.h5')
        pred_price = model_1.predict(new_X_test)
        # Undo the scaling
        pred_price = scaler.inverse_transform(pred_price)

        ####################
        new_df = {'Date':date_str, 'Close':pred_price[0][0]}
        # print(new_df)
        # last_60_days_tail.reset_index(inplace=True, drop=True)
        last_60_days_tail.loc[len(last_60_days_tail)] = new_df
        last_60_days_tail = last_60_days_tail.drop(last_60_days_tail.index[0])
        # print(last_60_days_tail)
        last_60_days_tail['Date'].iloc[-1]
        last_60_days_tail.drop('index', axis=1, inplace=True)
        # last_60_days.reset_index(inplace=True)
    # print(last_60_days_tail)
    date_list = last_60_days_tail[-30:]['Date'].astype(str).tolist()
    closing_price_list = last_60_days_tail[-30:]['Close'].tolist()
    print(last_60_days_tail[-30:])
    return pred_price[0][0], date_list, closing_price_list

  ####################

# cryptocoin_dict = {'DOGE':'DOGE-GBP', 'BNB':'BNB-GBP', 'BTC':'BTC-GBP', 'ETH':'ETH-GBP', 'USDT':'USDT-GBP'}
# Cryptocoin_Symbol = 'DOGE'
# Date = '2023-05-18'
# Result, dataframe_with_information = get_future_price(Input_Date=Date, tickers=Cryptocoin_Symbol)

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

def get_corr(chosen_crypto = "BTC-GBP"):
    # chosen_crypto = "BTC-GBP"

    # Fetch historical price data for the chosen crypto coin
    chosen_crypto_data = yf.download(chosen_crypto, period="1mo", interval="1d")["Close"]

    # Define the ticker symbols of other cryptocurrencies
    other_cryptos = ["ETH-GBP", "USDT-GBP","USDC-GBP","DOGE-GBP","XRP-GBP","XTZ-GBP", "SOL-GBP","TUSD-GBP","BNB-GBP","BTC-GBP"]

    # Fetch historical price data for other cryptocurrencies
    other_cryptos_data = yf.download(other_cryptos, period="1mo", interval="1d")["Close"]

    # Combine the chosen crypto data and other crypto data into a single DataFrame
    all_crypto_data = pd.concat([chosen_crypto_data, other_cryptos_data], axis=1)

    # Calculate the correlation between the chosen crypto coin and other cryptocurrencies
    correlation_matrix = all_crypto_data.corr().abs()

    # Extract the top ten positive and negative correlated cryptocurrencies
    top_positive_correlated = correlation_matrix[chosen_crypto].sort_values(ascending=False)[1:11]
    top_negative_correlated = correlation_matrix[chosen_crypto].sort_values(ascending=True)[:10]

    # Distype(play) the results
    print("Top Ten Positive Correlated Cryptocurrencies:")
    pos_result_dict = {'Symbol': list(top_positive_correlated.index), 'Correlation': list(top_positive_correlated)}

    print("\nTop Ten Negative Correlated Cryptocurrencies:")
    neg_result_dict = {'Symbol': list(top_negative_correlated.index), 'Correlation': list(top_negative_correlated)}

    return pos_result_dict, neg_result_dict