from flask import Flask, render_template, request, jsonify
from final_predicting import get_future_price, historical_data_func
import json
import yfinance as yf


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home_page():
    return render_template('index.html')

@app.route('/process_selection', methods=['GET','POST'])
def process_selection():
    timeframe = request.form.get("timeframe")
    cryptocoin = request.form.get("crypto")
    date = request.form.get("date")
        
    print(timeframe)
    print(cryptocoin)
    print(date)
    if timeframe == 'None':
        predicted_price, dates, prices=get_future_price(Input_Date=str(date), tickers=cryptocoin)
    else:
        dates, prices = historical_data_func(tickers=cryptocoin, period_tag=timeframe)
    response_data = {
        'dates': dates,
        'prices': prices
    }

    json_data = json.dumps(response_data)

    return jsonify(json_data)

@app.route('/calculate_profit_loss', methods=['POST'])
def calculate_profit_loss():
    btc = request.form.get('btc')
    buying_price = request.form.get('price')
    crypto = request.form.get('crypto_selection')
    cryptocoin_dict = {'DOGE':'DOGE-GBP', 'BNB':'BNB-GBP', 'BTC':'BTC-GBP', 'ETH':'ETH-GBP', 'USDT':'USDT-GBP'}

    data = yf.download([cryptocoin_dict[crypto]], period='1mo')
    data.drop("Adj Close", inplace=True, axis=1)
    data.drop("Volume", inplace=True, axis=1)
    data.drop("Open", inplace=True, axis=1)
    data.drop("High", inplace=True, axis=1)
    data.drop("Low", inplace=True, axis=1)
    data.reset_index(inplace=True)
    current_price = float(data['Close'].iloc[-1])

    buying_price = float(buying_price)
    btc = float(btc)
    Profit = (current_price - buying_price)*btc 
    if Profit < 0:
       response_data={
            'profit':Profit
            }
       json_data = json.dumps(response_data)
       return jsonify(json_data)
    else:
        response_data={
            'profit': abs(Profit)
            }
        json_data = json.dumps(response_data)
        return jsonify(json_data)

    # return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)