import pytest
import requests
from main import app

@pytest.fixture()
def client():
    return app.test_client()


#Rotas para Home
def test_home_status_code(client):
    resultado = client.get('/')
    assert resultado.status_code == 200

def test_home_text_content(client):
    resultado = client.get('/')
    assert resultado.text == 'SEJA BEM VINDO(A) A API ORGANICOS '

#Rotas para criar tabela
def test_criar_tabela_status_code(client):
    resultado = client.post('/criar_tabela')
    assert resultado.status_code == 201

def test_criar_tabela_return_content(client):
    resultado = client.post('/criar_tabela')
    assert resultado.json == {'Tabela':'criada'}

#Rotas para consulta tabela
def test_consulta_tabela_status_code(client):
    resultado = client.get('/consulta')
    assert resultado.status_code == 200

def test_consulta_tabela_(client): # TESTE TABELA VAZIO
    resultado = client.get('/consulta')
    assert resultado.status_code == 200 # No Content

#Rotas para consulta por ID
def test_consulta_id_status_code(client):
    resultado = client.get('/consulta/<-1>')
    assert resultado.status_code == 200

def test_consulta_id_return_null(client):
    resultado = client.get('/consulta/<-1>')
    assert resultado.json == {'Produtos': '[]'}

#Rotas para alimentar_
def test_alimentar_status_code(client):
    resultado = client.post('/alimentar/1/Carro/10.50/1/automatico')
    assert resultado.status_code == 202

def test_alimentar_(client):
    resultado = client.post('/alimentar/2/Banana/5.5/1/Da Jamaica')
    assert resultado.text == ("Banana Cadastrado com sucesso")

#Rotas para deletar por ID
def test_delete_id_status_code(client):
    resultado = client.delete('deletar/1')
    assert resultado.status_code == 200

def test_delete_id_status_code(client):
    resultado = client.delete('deletar/2')
    assert resultado.json == {'Mensagem': f'Produto ID 2 deletado com sucesso'}

#Rotas para Truncate 
def test_truncate_status_code(client):
    resultado = client.delete('/deletar')  
    assert resultado.status_code == 200
     
def test_truncate_message(client):
    resultado = client.delete('/deletar')  
    assert resultado.json == {'message': 'Carrinho apagado!'}

