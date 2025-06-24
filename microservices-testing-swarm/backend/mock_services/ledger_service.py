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

def chf_amount():
    return round(random.uniform(100.0, 100000.0), 2)

def transaction_id():
    return f"TXN{random.randint(100000,999999)}"

@app.route('/ledger/entry', methods=['POST'])
def create_entry():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Entry creation failed'}), 500
    data = request.json
    return jsonify({'entry_id': transaction_id(), 'status': 'created', 'amount': data.get('amount', chf_amount())})

@app.route('/ledger/balance', methods=['GET'])
def get_balance():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Balance unavailable'}), 503
    return jsonify({'balance': chf_amount(), 'currency': 'CHF'})

@app.route('/ledger/reconcile', methods=['POST'])
def reconcile_accounts():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Reconciliation failed'}), 500
    return jsonify({'status': 'reconciled'})

@app.route('/ledger/transactions', methods=['GET'])
def get_transactions():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Transactions unavailable'}), 503
    txns = [
        {'id': transaction_id(), 'amount': chf_amount(), 'currency': 'CHF'}
        for _ in range(random.randint(2, 5))
    ]
    return jsonify({'transactions': txns})

if __name__ == '__main__':
    app.run(port=5007) 