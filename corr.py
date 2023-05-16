import yfinance as yf
import pandas as pd

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


