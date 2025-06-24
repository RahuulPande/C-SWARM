import subprocess
import os
import sys
import time

SERVICES = [
    'account_service.py',
    'payment_service.py',
    'risk_service.py',
    'compliance_service.py',
    'trading_service.py',
    'customer_service.py',
    'ledger_service.py',
    'notification_service.py',
    'fx_service.py',
    'reporting_service.py',
    'auth_service.py',
    'audit_service.py',
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_DIR = os.path.join(BASE_DIR, 'mock_services')

processes = []

for service in SERVICES:
    path = os.path.join(SERVICE_DIR, service)
    print(f'Starting {service}...')
    proc = subprocess.Popen([sys.executable, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes.append(proc)
    time.sleep(0.2)  # Stagger startup

print('All mock services started.')
print('Press Ctrl+C to stop all services.')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Stopping all services...')
    for proc in processes:
        proc.terminate()
    print('All services stopped.') 