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

def compliance_flags():
    return random.sample(['PEP', 'Sanctions', 'None', 'Watchlist'], k=1)[0]

@app.route('/compliance/check', methods=['POST'])
def compliance_check():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Compliance check failed'}), 500
    data = request.json
    return jsonify({'result': 'pass' if random.random() > 0.1 else 'fail', 'flags': compliance_flags()})

@app.route('/compliance/rules/<jurisdiction>', methods=['GET'])
def get_rules(jurisdiction):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Rules unavailable'}), 503
    return jsonify({'jurisdiction': jurisdiction, 'rules': ['AML', 'KYC', 'Sanctions']})

@app.route('/compliance/report', methods=['POST'])
def generate_report():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Report generation failed'}), 500
    data = request.json
    return jsonify({'report_id': f'COMP{random.randint(1000,9999)}', 'status': 'generated'})

@app.route('/compliance/sanctions', methods=['GET'])
def sanctions_screening():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Sanctions screening unavailable'}), 503
    return jsonify({'sanctions': random.sample(['RU', 'IR', 'KP', 'None'], k=1)[0]})

if __name__ == '__main__':
    app.run(port=5004) 