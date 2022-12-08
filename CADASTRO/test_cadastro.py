import pytest
from cadastroAPI import app

@pytest.fixture()
def client():
    return app.test_client()

def test_consulta_catalogo(client):
    response = client.get('/consulta_catalogo')
    assert response.status_code == 200
    assert response.json.get('resultado')

def test_falha_consulta_produto(client):
    response = client.get('/consulta_produto')
    assert response.status_code == 400

def test_consulta_produto(client):
    response = client.get('/consulta_produto?nome=Maça')
    assert response.status_code == 200
    assert response.json.get('produto')

def test_cadastro(client):
    exemplo = {'nome':'Cerveja', 'id':'6', 'valor':'2.50', 'descricao':'Itaipava'}
    response = client.post('/cadastro', json=exemplo)
    assert response.status_code == 200
    assert response.json.get('successful') == True

def test_alterar_produto(client):
    exemplo = {'nome':'Cerveja', 'valor':'3.00'}
    response = client.put('/alterar_produto', json=exemplo)
    assert response.status_code == 200
    assert response.json.get('message')
    
def test_falha_alterar_produto(client):
    exemplo = {'valor':'3.00'}
    response = client.put('/alterar_produto', json=exemplo)
    assert response.status_code == 404

def test_deletar(client):
    exemplo = {'nome':'Cerveja'}
    response = client.delete('/deletar', json=exemplo)
    assert response.status_code == 200
    assert response.json.get('message')
