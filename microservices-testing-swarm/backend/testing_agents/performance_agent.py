import requests
import time
import random

class PerformanceAgent:
    def run_load_test(self, service_url, concurrent_users=10):
        results = []
        for _ in range(concurrent_users):
            start = time.time()
            try:
                resp = requests.get(service_url, timeout=1)
                latency = (time.time() - start) * 1000
                results.append({'status': resp.status_code, 'latency_ms': latency})
            except Exception:
                latency = (time.time() - start) * 1000
                results.append({'status': 'fail', 'latency_ms': latency})
        error_rate = sum(1 for r in results if r['status'] != 200) / len(results)
        throughput = len(results) / (sum(r['latency_ms'] for r in results) / 1000)
        return {'results': results, 'error_rate': error_rate, 'throughput': throughput}

    def stress_test_system(self, service_urls, total_users=100):
        # Simulate multi-service load
        stats = {}
        for url in service_urls:
            stats[url] = self.run_load_test(url, concurrent_users=total_users // len(service_urls))
        # Find breaking points (highest error rate)
        bottleneck = max(stats, key=lambda u: stats[u]['error_rate'])
        return {'stats': stats, 'bottleneck': bottleneck} 