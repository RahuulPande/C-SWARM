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

def trade_id():
    return f"TRD{random.randint(10000,99999)}"

def chf_amount():
    return round(random.uniform(1000.0, 1000000.0), 2)

@app.route('/trades/execute', methods=['POST'])
def execute_trade():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Trade execution failed'}), 500
    data = request.json
    return jsonify({'trade_id': trade_id(), 'status': 'executed', 'amount': data.get('amount', chf_amount()), 'instrument': data.get('instrument', 'bond')})

@app.route('/trades/<id>', methods=['GET'])
def get_trade(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Trade not found'}), 404
    return jsonify({'trade_id': id, 'status': random.choice(['executed', 'pending', 'failed']), 'amount': chf_amount(), 'instrument': random.choice(['bond', 'fx', 'derivative'])})

@app.route('/trades/validate', methods=['POST'])
def validate_trade():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Trade validation failed'}), 400
    data = request.json
    valid = data.get('amount', 0) > 0
    return jsonify({'valid': valid})

@app.route('/trades/positions', methods=['GET'])
def get_positions():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Positions unavailable'}), 503
    positions = [
        {'instrument': 'bond', 'amount': chf_amount()},
        {'instrument': 'fx', 'amount': chf_amount()},
        {'instrument': 'derivative', 'amount': chf_amount()}
    ]
    return jsonify({'positions': positions})

if __name__ == '__main__':
    app.run(port=5005) 