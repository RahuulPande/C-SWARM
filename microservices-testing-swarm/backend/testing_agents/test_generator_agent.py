import random
import uuid

class TestGeneratorAgent:
    def generate_tests(self, service_spec):
        tests = []
        for endpoint in service_spec.get('endpoints', []):
            # Positive test
            tests.append({
                'test_id': str(uuid.uuid4()),
                'endpoint': endpoint,
                'data': self.mock_data(endpoint),
                'type': 'positive',
            })
            # Negative test
            tests.append({
                'test_id': str(uuid.uuid4()),
                'endpoint': endpoint,
                'data': self.mock_data(endpoint, negative=True),
                'type': 'negative',
            })
        return tests

    def mock_data(self, endpoint, negative=False):
        # Generate banking-specific test data
        if 'account' in endpoint:
            if negative:
                return {'account_number': 'INVALID'}
            return {'account_number': str(random.randint(1000000000, 9999999999))}
        if 'payment' in endpoint:
            if negative:
                return {'iban': 'XX00 0000 0000 0000 0000 0'}
            return {'iban': f'CH{random.randint(10,99)} 0076 2011 6238 5295 7', 'amount': round(random.uniform(10, 10000), 2)}
        # Add more as needed
        return {'field': 'value'}

    def generate_harmonization_tests(self):
        # Create CS->UBS transformation tests
        tests = []
        for _ in range(10):
            cs_data = {'cs_account': str(random.randint(1000000000000000, 9999999999999999))}
            ubs_format = {'ubs_account': str(random.randint(1000000000, 9999999999))}
            tests.append({'cs_data': cs_data, 'ubs_format': ubs_format, 'type': 'harmonization'})
        return tests 