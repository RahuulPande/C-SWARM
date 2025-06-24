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

def permissions():
    return ['read', 'write', 'trade', 'admin']

@app.route('/auth/login', methods=['POST'])
def login():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Login failed'}), 401
    data = request.json
    return jsonify({'token': f'TOKEN{random.randint(10000,99999)}', 'user': data.get('user', 'guest')})

@app.route('/auth/validate', methods=['POST'])
def validate_token():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Token invalid'}), 403
    data = request.json
    return jsonify({'valid': True, 'user': data.get('user', 'guest')})

@app.route('/auth/permissions', methods=['GET'])
def get_permissions():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'Permissions unavailable'}), 503
    return jsonify({'permissions': random.sample(permissions(), k=random.randint(1,4))})

@app.route('/auth/mfa', methods=['POST'])
def mfa():
    random_delay()
    if maybe_fail():
        return jsonify({'error': 'MFA failed'}), 401
    return jsonify({'mfa': 'success'})

if __name__ == '__main__':
    app.run(port=5011) 