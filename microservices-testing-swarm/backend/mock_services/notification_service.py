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

def notification_id():
    return f"NTF{random.randint(10000,99999)}"

def templates():
    return ['Payment Confirmation', 'Account Alert', 'KYC Reminder']

@app.route('/notifications/send', methods=['POST'])
def send_notification():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Notification failed'}), 500
    data = request.json
    return jsonify({'notification_id': notification_id(), 'status': 'sent', 'template': data.get('template', 'Payment Confirmation')})

@app.route('/notifications/templates', methods=['GET'])
def get_templates():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Templates unavailable'}), 503
    return jsonify({'templates': templates()})

@app.route('/notifications/batch', methods=['POST'])
def batch_send():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Batch send failed'}), 500
    data = request.json
    count = len(data.get('recipients', []))
    return jsonify({'sent': count, 'status': 'batch_sent'})

@app.route('/notifications/status', methods=['GET'])
def check_status():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Status unavailable'}), 503
    return jsonify({'status': random.choice(['delivered', 'pending', 'failed'])})

if __name__ == '__main__':
    app.run(port=5008) 