import requests
import socket
import time

class ServiceDiscoveryAgent:
    def __init__(self, base_ports=range(5001, 5013)):
        self.base_ports = base_ports
        self.services = {}
        self.mesh = {}

    def discover_services(self):
        discovered = {}
        for port in self.base_ports:
            try:
                url = f'http://localhost:{port}'
                # Try a common endpoint for each service
                resp = requests.get(url, timeout=0.5)
            except Exception:
                # Try to guess endpoints
                endpoints = [
                    '/accounts/1', '/payments/limits', '/risk/var', '/compliance/sanctions',
                    '/trades/positions', '/customers/1', '/ledger/balance', '/notifications/status',
                    '/fx/rates', '/reports/templates', '/auth/permissions', '/audit/trail'
                ]
                found = False
                for ep in endpoints:
                    try:
                        resp = requests.get(url + ep, timeout=0.5)
                        if resp.status_code < 500:
                            discovered[port] = {'endpoint': ep, 'status': 'up'}
                            found = True
                            break
                    except Exception:
                        continue
                if not found:
                    discovered[port] = {'endpoint': None, 'status': 'down'}
            else:
                discovered[port] = {'endpoint': '/', 'status': 'up'}
        self.services = discovered
        # Build mesh data (stub)
        self.mesh = {'nodes': list(discovered.keys()), 'edges': []}
        return self.mesh

    def map_dependencies(self):
        # Stub: In a real system, analyze logs or traces
        # Here, just create a random interaction matrix
        import random
        nodes = list(self.services.keys())
        edges = []
        for src in nodes:
            for dst in nodes:
                if src != dst and random.random() < 0.2:
                    edges.append({'from': src, 'to': dst, 'traffic': random.randint(1, 100)})
        self.mesh['edges'] = edges
        return self.mesh 