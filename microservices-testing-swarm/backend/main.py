from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import asyncio
import json

from testing_agents.service_discovery_agent import ServiceDiscoveryAgent
from testing_agents.test_generator_agent import TestGeneratorAgent
from testing_agents.harmonization_agent import HarmonizationAgent
from testing_agents.performance_agent import PerformanceAgent
from testing_agents.orchestrator_agent import OrchestratorAgent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

discovery_agent = ServiceDiscoveryAgent()
testgen_agent = TestGeneratorAgent()
harmonization_agent = HarmonizationAgent()
performance_agent = PerformanceAgent()
orchestrator_agent = OrchestratorAgent({
    'discovery': discovery_agent,
    'testgen': testgen_agent,
    'harmonization': harmonization_agent,
    'performance': performance_agent
})

@app.post('/api/discover')
async def api_discover():
    mesh = discovery_agent.discover_services()
    mesh = discovery_agent.map_dependencies()
    return JSONResponse(mesh)

@app.post('/api/generate-tests')
async def api_generate_tests(request: Request):
    body = await request.json()
    service_spec = body.get('service_spec', {'endpoints': ['/']})
    tests = testgen_agent.generate_tests(service_spec)
    return JSONResponse({'tests': tests})

@app.post('/api/run-tests')
async def api_run_tests():
    results = orchestrator_agent.coordinate_test_swarm()
    return JSONResponse({'results': results})

@app.post('/api/harmonization')
async def api_harmonization(request: Request):
    body = await request.json()
    cs_data = body.get('cs_data', {'cs_account': '1234567890123456'})
    ubs_format = body.get('ubs_format', {'ubs_account': '1234567890'})
    result = harmonization_agent.test_data_transformation(cs_data, ubs_format)
    return JSONResponse({'result': result})

@app.get('/api/metrics')
async def api_metrics():
    # Return mock metrics for now
    return JSONResponse({
        'test_coverage': 99.7,
        'tests_per_second': 1000,
        'success_rate': 0.995,
        'error_rate': 0.005,
        'latency_ms': 120
    })

@app.get('/api/service-mesh')
async def api_service_mesh():
    return JSONResponse(discovery_agent.mesh)

@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 0
    try:
        while True:
            await asyncio.sleep(1)
            msg = {
                'type': 'metric',
                'service': 'payment_service',
                'timestamp': '2024-01-15T10:30:00Z',
                'data': {
                    'test_id': f'test-{i}',
                    'result': 'pass',
                    'latency_ms': 127 + i,
                    'details': {}
                }
            }
            await websocket.send_text(json.dumps(msg))
            i += 1
    except Exception as e:
        print("WebSocket closed:", e)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000) 