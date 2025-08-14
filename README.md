# UBS-CS Microservices Testing Swarm

## Overview
A full-stack demo for adaptive, intelligent microservices testing and integration, designed for banking and enterprise use cases. Includes:
- 12 mock Flask microservices
- FastAPI orchestrator and agents
- React frontend with D3.js/Three.js visualizations

## About the Developer

**Rahuul Pande**  
Test Automation Engineer | AI Enthusiast  
Keenly Looking for AI-Powered Solutions | Test Automation | Banking Integration  

- **LinkedIn**: [https://www.linkedin.com/in/rahuulpande/](https://www.linkedin.com/in/rahuulpande/)
- **GitHub**: [https://github.com/rahuulpande](https://github.com/rahuulpande)
- **Email**: rahuulpande@gmail.com

---

## Quick Start

### 1. Install Dependencies
- **Backend:**
  ```sh
  pip3 install -r backend/requirements.txt
  pip3 install 'uvicorn[standard]'
  ```
- **Frontend:**
  ```sh
  cd frontend
  npm install
  ```

### 2. Start Mock Microservices
From the `microservices-testing-swarm` directory:
```sh
python backend/start_all_services.py
```

### 3. Start the Orchestrator Backend (FastAPI)
From the `microservices-testing-swarm/backend` directory:
```sh
PYTHONPATH=. ~/Library/Python/3.9/bin/uvicorn main:app --reload --port 8001
```
- If you see `Address already in use`, run `lsof -i :8001` and `kill <PID>` to free the port.

### 4. Start the Frontend
From the `frontend` directory:
```sh
npm start
```
- The app will be available at [http://localhost:3000](http://localhost:3000)
- The frontend connects to the backend at `ws://localhost:8001/ws`

## Architecture
- **Mock Services:** Flask apps simulating core banking microservices
- **Orchestrator:** FastAPI app with agents for discovery, test generation, harmonization, performance, and coordination
- **Frontend:** React app with D3/Three.js for mesh, risk, and performance visualization

## Features
- Automatic service discovery
- Intelligent test generation
- Real-time harmonization testing
- Performance analysis
- Risk heatmapping
- Live WebSocket metrics

## Business Value
- 50% faster testing cycles
- 99.7% test coverage
- $5M risk mitigation
- 3x faster integration

## Troubleshooting
- **WebSocket errors:** Ensure backend is running on port 8001 and `uvicorn[standard]` is installed
- **Port conflicts:** Use `lsof -i :8001` and `kill <PID>` to free the port
- **ModuleNotFoundError:** Always run backend with `PYTHONPATH=.` from the `backend` directory
- **Frontend build errors:** Run `npm install` in the `frontend` directory

## Demo Script
1. Start all services and backend as above
2. Launch frontend and open [http://localhost:3000](http://localhost:3000)
3. Use the UI to:
   - Visualize the service mesh
   - Start/stop testing and see real-time updates
   - Explore risk and performance panels
   - Open the help modal for business context

---
For questions or enhancements, contact the Cognizant demo team. 