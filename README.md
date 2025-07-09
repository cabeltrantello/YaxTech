# YaxTech

This is the backend service for the YaxTech project. It provides dynamic, API-driven mock server designed to simulate telecommunication network components.

## Phase 1: Core Backend

This initial version includes:
- A management endpoint 'POST /api/v1/_config' to register mock configurations.
- A catch-all simulator endpoint '/api/v1/*' that serves the configured mocks.
- In-memory storage for mock configurations.
- Full containerization with Docker.

### Prerequisites

- Python 3.11+
- Poetry
- Docker

### How to Run Locally

1. **Install dependencies**
    ```bash
    cd backend
    poetry install
    ```

2. **Run the application**
    ```bash
    poetry run uvicorn backend.app.main:app --reload
    ```

    The `--reload` flag enables hot-reloading for development

3. **Access the API**
    - **Documentation (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **Alternative Docs (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## How to use

1. **Register a mock**
    Send a `POST` request to `http://127.0.0.1:8000/api/v1/_config` with a JSON body like this:

    ```json
    {
      "method": "GET",
      "path": "/api/v1/YaxTech/bbu-4/status",
      "response": {
        "status_code": 200,
        "headers": {
          "Content-Type": "application/json",
          "X-Simulated-By": "TNSP"
        },
        "body": {
          "serialNumber": "SN-BBU-004",
          "status": "operational",
          "activeCalls": 157,
          "cpuLoad": 0.43
        }
      }
    }
    ```

2. **Trigger the mock:**
    Send a `GET` request to the path you just configured:
    `http://127.0.0.1:8000/api/v1/YaxTech/bbu-4/status`

    You will receive the response you defined in the previous step.