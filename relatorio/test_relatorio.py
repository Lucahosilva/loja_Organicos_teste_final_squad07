from relatorio.main import app
import pytest

@pytest.fixture()
def client():
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200