import random
import time
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Helper functions for mock data
def random_delay():
    time.sleep(random.uniform(0.05, 0.5))

def maybe_fail():
    if random.random() < 0.05:
        return True
    return False

def swiss_iban():
    return f"CH{random.randint(10,99)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(100,999)} {random.randint(0,9)}"

def cs_account():
    return str(random.randint(1000000000000000, 9999999999999999))

def ubs_account():
    return str(random.randint(1000000000, 9999999999))

def chf_amount():
    return round(random.uniform(100.0, 100000.0), 2)

@app.route('/accounts/<id>', methods=['GET'])
def get_account(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Service unavailable'}), 503
    fmt = random.choice(['CS', 'UBS'])
    if fmt == 'CS':
        account = cs_account()
    else:
        account = ubs_account()
    return jsonify({
        'id': id,
        'format': fmt,
        'account_number': account,
        'iban': swiss_iban(),
        'bank': random.choice(['Credit Suisse', 'UBS'])
    })

@app.route('/accounts/validate', methods=['POST'])
def validate_account():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Validation failed'}), 400
    data = request.json
    valid = bool(data and 'account_number' in data and len(str(data['account_number'])) in [10, 16])
    return jsonify({'valid': valid})

@app.route('/accounts/<id>/balance', methods=['GET'])
def get_balance(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Balance unavailable'}), 503
    return jsonify({'id': id, 'balance': chf_amount(), 'currency': 'CHF'})

@app.route('/accounts/transform', methods=['POST'])
def transform_account():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Transformation failed'}), 500
    data = request.json
    # Simulate CS to UBS transformation
    cs = data.get('cs_account')
    ubs = ubs_account()
    return jsonify({'cs_account': cs, 'ubs_account': ubs, 'iban': swiss_iban()})

if __name__ == '__main__':
    app.run(port=5001) 