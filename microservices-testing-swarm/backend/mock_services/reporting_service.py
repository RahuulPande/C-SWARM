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

def report_id():
    return f"REP{random.randint(10000,99999)}"

def templates():
    return ['Balance Sheet', 'Regulatory', 'Risk', 'Performance']

@app.route('/reports/generate', methods=['POST'])
def generate_report():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Report generation failed'}), 500
    data = request.json
    return jsonify({'report_id': report_id(), 'status': 'generated', 'type': data.get('type', 'Balance Sheet')})

@app.route('/reports/templates', methods=['GET'])
def get_templates():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Templates unavailable'}), 503
    return jsonify({'templates': templates()})

@app.route('/reports/regulatory', methods=['POST'])
def regulatory_report():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Regulatory report failed'}), 500
    return jsonify({'report_id': report_id(), 'status': 'regulatory_generated'})

@app.route('/reports/<id>', methods=['GET'])
def get_report(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Report not found'}), 404
    return jsonify({'report_id': id, 'status': random.choice(['generated', 'pending', 'failed'])})

if __name__ == '__main__':
    app.run(port=5010) 