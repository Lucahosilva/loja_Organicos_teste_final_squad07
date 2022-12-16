from flask import Flask
from json import dumps
import sqlite3 as sql

app= Flask(__name__)
banco = "cart.db"
#
# Comandos SQL
criar_table = "CREATE TABLE IF NOT EXISTS carrinho (id_prod INTEGER PRIMARY KEY, nome TEXT NOT NULL, preco REAL NOT NULL, quantidade INTEGER NOT NULL, desc TEXT NOT NULL);"
select_todos = "SELECT * FROM carrinho;"
truncate = "DELETE FROM carrinho;" #"TRUNCATE 
select_id = "SELECT * FROM carrinho WHERE id_prod like ?;"
delete_id = "DELETE FROM carrinho WHERE id_prod = ?;"
atualiza_prod = "UPDATE carrinho SET quantidade = (quantidade) WHERE id_prod = (id_prod);" 

def abrir_conexao(banco):
    conexao = sql.connect(banco) #connection to db
    cursor = conexao.cursor() #create a cursor
    return conexao, cursor

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

@app.get('/') # FUNCIONANDO
def home(): 
    return ("SEJA BEM VINDO(A) A API ORGANICOS "), 200

@app.post('/criar_tabela') # FUNCIONADO
def criar_tabela(): 
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(criar_table)
    fechar_conexao(conexao)
    return {'Tabela':'criada'}, 201

@app.get('/listar') # FUNCIONANDO 
def listar_produtos():
    conexao, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_todos).fetchall() 
    fechar_conexao(conexao)
    return {'Produtos': f'{resultado}'}, 200

@app.get('/listar/<id_prod>') #Funcionando 
def listar_produto(id_prod):
    try:
        conexao, cursor = abrir_conexao(banco) # abertura do banco
        resultado = cursor.execute(select_id, [id_prod]).fetchall() 
        fechar_conexao(conexao)
        return {'Produtos': f'{resultado}'}, 200
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conexao)
        return {f'Erro ao consultar produto {id_prod}, verificar parametros {resultado}'}, 400

@app.put('/atualiza/<id_prod>/<quantidade>') #Funcionando
def update_quanti(id_prod,quantidade): # /atualiza/2/20
    try:
        conexao, cursor = abrir_conexao(banco)
        cursor.execute(f"UPDATE carrinho SET quantidade = {quantidade} WHERE id_prod = {id_prod}")   
        fechar_conexao(conexao)
        return {f'id {id_prod} - Quantidade alterada para {quantidade} com sucesso'}, 202
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conexao)
        return {f'Erro ao atulizar produto {id_prod}, verificar parametros {resultado}'}, 400

@app.delete('/deletar') # FUNCIONANDO 
def deleta_tabela():
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Carrinho apagado!'} , 200

@app.delete('/deletar/<id_prod>') # FUNCIONANDO
def deleta_id(id_prod):
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(delete_id, [id_prod])
    fechar_conexao(conexao)
    return {'Mensagem': f'Produto ID {id_prod} deletado com sucesso'}, 200
   
@app.post('/alimentar/<id_prod>/<name>/<value>/<quantity>/<desc>') # FUNCIONANDO 
def alimentar_tabela(id_prod, name, value, quantity, desc): # /alimentar/1/Carro/10.50/1/1.0 sem Ar
    try:
        conexao, cursor = abrir_conexao(banco)
        data = [
        (id_prod,name,value,quantity,desc)
        ]
        cursor.executemany('INSERT INTO carrinho VALUES(?,?,?,?,?)', data)
        resultado = cursor.execute(select_todos)
        fechar_conexao(conexao)
        return{f"{name} Cadastrado com sucesso"} , 202
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conexao)
        return {f'Erro ao adicionar produto(s), verificar parametros {resultado}'}, 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)
