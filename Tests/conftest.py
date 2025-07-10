import pytest
from httpx import AsyncClient
from Backend.App.main import app
from Backend.App.Core.security import MASTER_API_KEY

@pytest.fixture(scope="module")
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module")
def valid_api_key_header():
    return {"X-API-key":MASTER_API_KEY}