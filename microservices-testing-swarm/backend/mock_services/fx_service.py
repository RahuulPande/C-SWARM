import random
import time
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def random_delay():
    time.sleep(random.uniform(0.05, 0.5))

def maybe_fail():
    return random.random() < 0.05

def fx_pairs():
    return ['CHF/EUR', 'CHF/USD', 'CHF/GBP', 'EUR/USD']

def fx_rates():
    return {pair: round(random.uniform(0.8, 1.2), 4) for pair in fx_pairs()}

@app.route('/fx/rates', methods=['GET'])
def get_rates():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Rates unavailable'}), 503
    return jsonify({'rates': fx_rates()})

@app.route('/fx/convert', methods=['POST'])
def convert_currency():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Conversion failed'}), 500
    data = request.json
    pair = data.get('pair', 'CHF/EUR')
    amount = data.get('amount', 100)
    rate = fx_rates().get(pair, 1.0)
    return jsonify({'pair': pair, 'amount': amount, 'converted': round(amount * rate, 2), 'rate': rate})

@app.route('/fx/pairs', methods=['GET'])
def get_pairs():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Pairs unavailable'}), 503
    return jsonify({'pairs': fx_pairs()})

@app.route('/fx/hedge', methods=['POST'])
def create_hedge():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Hedge creation failed'}), 500
    data = request.json
    return jsonify({'hedge_id': f'HEDGE{random.randint(1000,9999)}', 'status': 'created'})

if __name__ == '__main__':
    app.run(port=5009) 