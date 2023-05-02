import pytest
from fastapi.testclient import TestClient
from app.app import app
from database import create_db

@pytest.fixture(autouse=True)
def setup_app():
    create_db()

client = TestClient(app)

def test_shorten_url():
    response = client.post("/v1/shorten", json={"url": "https://example.com"})
    print(response.json())
    assert response.status_code == 200
    assert "short_url" in response.json()
