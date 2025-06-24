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

def risk_score():
    score = random.randint(0, 100)
    category = (
        'Low' if score < 30 else
        'Medium' if score < 70 else
        'High'
    )
    return {'score': score, 'category': category}

def chf_amount():
    return round(random.uniform(1000.0, 1000000.0), 2)

@app.route('/risk/calculate', methods=['POST'])
def calculate_risk():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Risk calculation failed'}), 500
    data = request.json
    return jsonify({'account_id': data.get('account_id', 'unknown'), **risk_score()})

@app.route('/risk/exposure/<account_id>', methods=['GET'])
def get_exposure(account_id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Exposure unavailable'}), 503
    return jsonify({'account_id': account_id, 'exposure': chf_amount(), 'currency': 'CHF'})

@app.route('/risk/derivatives/price', methods=['POST'])
def price_derivatives():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Pricing failed'}), 500
    data = request.json
    price = chf_amount()
    return jsonify({'instrument': data.get('instrument', 'swap'), 'price': price, 'currency': 'CHF'})

@app.route('/risk/var', methods=['GET'])
def value_at_risk():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'VaR unavailable'}), 503
    return jsonify({'var': chf_amount(), 'confidence': '99.7%'})

if __name__ == '__main__':
    app.run(port=5003) 