import pytest

pytestmark = pytest.mark.asyncio

@pytest.fixture(autouse=True)
async def setup_test_mocks(test_client, valid_api_key_header):
    mock_payload = {
        "method": "GET",
        "path": "/api/v1/network-elements/bbu-5/health",
        "scenarios": {
            "default": {"status_code": 200, "body": {"health": "GOOD"}},
            "degraded": {"status_code": 200, "body": {"health": "DEGRADED"}},
        }
    }
    await test_client.post("/api/v1/config", json=mock_payload, headers=valid_api_key_header)
    yield
    # Teardown logic could go here if needed, but the in-memory DB is reset per test run

async def test_simulate_default_scenario(test_client):
    response = await test_client.get("/api/v1/network-elements/bbu-5/health")
    assert response.status_code == 200
    assert response.json() == {"health": "GOOD"}

async def test_simulate_named_scenario(test_client):
    response = await test_client.get("/api/v1/network-elements/bbu-5/health?scenario=degraded")
    assert response.status_code == 200
    assert response.json() == {"health": "DEGRADED"}

async def test_simulate_nonexistent_scenario_falls_back_to_default(test_client):
    response = await test_client.get("/api/v1/network-elements/bbu-5/health?scenario=nonexistent")
    assert response.status_code == 200
    assert response.json() == {"health": "GOOD"}

async def test_simulate_nonexistent_mock_returns_404(test_client):
    """Test that requesting a path that has no mock definition returns 404."""
    response = await test_client.get("/api/v1/this/path/does/not/exist")
    assert response.status_code == 404

