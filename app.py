from flask import Flask, render_template, request, jsonify
from final_predicting import get_future_price, historical_data_func
import json


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)