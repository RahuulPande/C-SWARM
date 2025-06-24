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

def swiss_iban():
    return f"CH{random.randint(10,99)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(100,999)} {random.randint(0,9)}"

def chf_amount():
    return round(random.uniform(10.0, 100000.0), 2)

@app.route('/payments/initiate', methods=['POST'])
def initiate_payment():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Payment initiation failed'}), 500
    data = request.json
    payment_id = f"PAY{random.randint(100000,999999)}"
    return jsonify({'payment_id': payment_id, 'status': 'initiated', 'amount': data.get('amount', chf_amount()), 'currency': 'CHF'})

@app.route('/payments/<id>/status', methods=['GET'])
def payment_status(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Status unavailable'}), 503
    return jsonify({'payment_id': id, 'status': random.choice(['pending', 'completed', 'failed'])})

@app.route('/payments/validate-iban', methods=['POST'])
def validate_iban():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'IBAN validation failed'}), 400
    data = request.json
    iban = data.get('iban', '')
    valid = iban.startswith('CH') and len(iban.replace(' ', '')) >= 15
    return jsonify({'valid': valid})

@app.route('/payments/limits', methods=['GET'])
def payment_limits():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Limits unavailable'}), 503
    return jsonify({'daily_limit': 100000, 'single_limit': 25000, 'currency': 'CHF'})

if __name__ == '__main__':
    app.run(port=5002) 