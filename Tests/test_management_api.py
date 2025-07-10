import pytest

pytestmark = pytest.mark.asyncio

async def test_unauthorized_access(test_client):
    response = await test_client.get("/api/v1/config")
    assert response.status_code == 403

    response = await test_client.post("/api/v1/config", json={})
    assert response.status_code == 403

async def test_create_and_get_mock(test_client, valid_api_key_header):
    mock_payload = {
        "method": "GET",
        "path": "/api/v1/telco-devices/router-01",
        "scenarios": {
            "default": {"status_code": 200, "body": {"status": "OK"}},
            "maintenance": {"status_code": 503, "body": {"status": "MAINTENANCE"}}
        }
    }

    #Create
    response = await test_client.post("/api/v1/config", json=mock_payload, headers=valid_api_key_header)
    assert response.status_code == 201
    created_mock = response.json()
    assert "mock_id" in created_mock
    mock_id = created_mock["mock_id"]

    #Get by ID
    response = await test_client.get(f"/api/v1/config/{mock_id}", headers=valid_api_key_header)
    assert response.status_code == 200
    retrieved_mock = response.json()
    assert retrieved_mock["path"] == "/api/v1/telco-devices/router-01"
    assert "maintenance" in retrieved_mock["scenarios"]

async def test_delete_mock(test_client, valid_api_key_header):
    mock_payload = {
        "method": "DELETE",
        "path": "/api/v1/telco-sessions/session-123",
        "scenarios": {"default": {"status_code": 204}}
    }

    #Create
    response = await test_client.post("/api/v1/config", json=mock_payload, headers=valid_api_key_header)
    assert response.status_code == 201
    mock_id = response.json()["mock_id"]

    #Delete
    response = await test_client.delete(f"/api/v1/config/{mock_id}", headers=valid_api_key_header)
    assert response.status_code == 204

    "Verify deleiton"
    response = await test_client.get(f"/api/v1/config/{mock_id}", headers=valid_api_key_header)
    assert response.status_code == 404