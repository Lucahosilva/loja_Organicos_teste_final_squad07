import pytest
import requests
from main import app

@pytest.fixture()
def client():
    return app.test_client()

def test_home_status_code(client):
    resultado = client.get('/')
    assert resultado.status_code == 200

def test_home_text_content(client):
    resultado = client.get('/')
    assert resultado.text == 'SEJA BEM VINDO(A) A API ORGANICOS '

def test_criar_tabela_status_code(client):
    resultado = client.post('/criar_tabela')
    assert resultado.status_code == 201

def test_criar_tabela_return_content(client):
    resultado = client.post('/criar_tabela')
    assert resultado.json == {'Tabela':'criada'}

def test_consulta_tabela_status_code(client):
    resultado = client.get('/consulta')
    assert resultado.status_code == 200

def test_consulta_tabela_(client):
    resultado = client.get('/consulta')

    assert resultado.status_code == 200


