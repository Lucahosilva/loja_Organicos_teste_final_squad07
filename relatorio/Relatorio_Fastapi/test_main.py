from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_itens():
    response = client.get('/items')
    assert response.status_code == 200
    assert  response.json()[0].get('produto') == 'Abóbora'

def test_get_item():
    response = client.get('/items/Batata')
    assert response.status_code == 200
    assert  response.json()[0].get('produto') == 'Batata'

def test_best_sellers():
    response = client.get('/best_sellers')
    assert response.status_code == 200
    assert  response.json() != []

def test_top_ten():
    response = client.get('/top_ten')
    assert response.status_code == 200
    assert  response.json() != []

def test_popular_tables():
    response = client.post('/popular_table')
    assert response.status_code == 201
    assert  response.json() == {'detail': 'Created'}

def test_less_sold():
    response = client.get('/less_sold')
    assert response.status_code == 200
    assert  response.json() != []

def test_top_sales():
    response = client.get('/top_sales')
    assert response.status_code == 200
    assert  response.json() != []
