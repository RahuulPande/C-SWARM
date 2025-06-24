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

def audit_id():
    return f"AUD{random.randint(10000,99999)}"

@app.route('/audit/log', methods=['POST'])
def create_log():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Log creation failed'}), 500
    data = request.json
    return jsonify({'audit_id': audit_id(), 'status': 'logged'})

@app.route('/audit/trail', methods=['GET'])
def get_trail():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Trail unavailable'}), 503
    trail = [
        {'id': audit_id(), 'action': random.choice(['login', 'trade', 'payment'])}
        for _ in range(random.randint(2, 5))
    ]
    return jsonify({'trail': trail})

@app.route('/audit/search', methods=['POST'])
def search_logs():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Search failed'}), 500
    data = request.json
    return jsonify({'results': [audit_id() for _ in range(random.randint(1, 3))]})

@app.route('/audit/report', methods=['GET'])
def audit_report():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Audit report unavailable'}), 503
    return jsonify({'report_id': f'AUDREP{random.randint(1000,9999)}', 'status': 'generated'})

if __name__ == '__main__':
    app.run(port=5012) 