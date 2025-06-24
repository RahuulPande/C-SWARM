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

def customer_segment():
    return random.choice(['retail', 'wealth', 'institutional'])

def products():
    return random.sample(['account', 'loan', 'card', 'fx', 'investment'], k=random.randint(1,3))

@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify({'id': id, 'name': f'Customer {id}', 'segment': customer_segment()})

@app.route('/customers/kyc', methods=['POST'])
def kyc_verification():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'KYC failed'}), 400
    data = request.json
    return jsonify({'customer_id': data.get('customer_id', 'unknown'), 'kyc_status': random.choice(['verified', 'pending', 'failed'])})

@app.route('/customers/<id>/products', methods=['GET'])
def get_products(id):
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Products unavailable'}), 503
    return jsonify({'customer_id': id, 'products': products()})

@app.route('/customers/onboard', methods=['POST'])
def onboard_customer():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Onboarding failed'}), 500
    data = request.json
    return jsonify({'customer_id': f'CUST{random.randint(1000,9999)}', 'status': 'onboarded'})

if __name__ == '__main__':
    app.run(port=5006) 