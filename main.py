import sqlite3 as sql
from json import dumps
from fastapi import FastAPI

# Rodar API - uvicorn main:app
# http://127.0.0.1:8000/doc
# http://127.0.0.1:8000/redoc

# cliente thunder raio

banco = "cart.db"
#
# Comandos SQL
# contagem = "SELECT COUNT(*) FROM Carrinho;"
criar_table = "CREATE TABLE IF NOT EXISTS Carrinho (id_prod INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço REAL NOT NULL, Quantidade INTEGER NOT NULL, Descrição TEXT NOT NULL);"
select_todos = "SELECT * FROM Carrinho;"
truncate = "DELETE FROM Carrinho;" #"TRUNCATE TABLE carrinho;"
#select_id = "SELECT * FROM Carrinho WHERE id_prod like ?;"
#delete_id = "DELETE FROM Carrinho WHERE id_prod = ?;"
#inserir_prod = "INSERT INTO Carrinho VALUES (:id,:Nome,:Preco,:Quantidade,:Descrição,);"
atualiza_prod = "UPDATE carrinho SET quantidade = [valor] WHERE id_prod = [id_produto];" 


def abrir_conexao(banco):
    conn = sql.connect(banco) #connection to db
    cursor = conn.cursor() #create a cursor
    return conn, cursor

def fechar_conexao(conn):
    conn.commit()
    conn.close()

app= FastAPI()

@app.get('/') # FUNCIONANDO
async def criar_tabela(): 
    return ("SEJA BEM VINDO(A) A API ORGANICOS ")

@app.post('/criar_tabela') # FUNCIONADO
async def criar_tabela(): 
    conn, cursor = abrir_conexao(banco)
    resultado = cursor.execute(criar_table)
    fechar_conexao(conn)
    return {'Tabela': f'{resultado} criada.'}

@app.get('/consulta') # FUNCIONANDO
def consulta_tabela():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_todos).fetchall() 
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}

@app.put('/update/{id_prod}/{Quantidade}') # testando - ERROR 404 - Validation Error
def update_prod_id(id_prod,Quantidade):
    try:
        conn, cursor = abrir_conexao(banco)
        cursor.execute('UPDATE carrinho SET Quantidade = [Quantidade] WHERE id_prod = [id_prod]')
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conn)
        return (f'Erro ao adicionar produto(s), verificar parametros {resultado}')

@app.delete('/deleta') # FUNCIONANDO
def deleta_tabela():
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Carrinho apagado!'}

# EXTRA ADICONAR DADOS

@app.post('/alimentar') # FUNCIONANDO
def alimentar_tabela():
    try:
        conn, cursor = abrir_conexao(banco)
        data = [
        (1,'Cacau',12.5,3,'Do Brasil'),
        (2,'Arroz',10,2,'Do Brasil'),
        (3,'Feijão',8,5,'Do Brasil'),
        (4,'Batata',11,10,'Do Brasil'),
        (5,'Café',8,5,'Do Brasil'),
        (6,'Vinho',15,2,'Da Argentina'),
        ]
        cursor.executemany('INSERT INTO Carrinho VALUES(?,?,?,?,?)', data)
        resultado = cursor.execute(select_todos)
        print(resultado)
        fechar_conexao(conn)
        return("Cadastrado")
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conn)
        return (f'Erro ao adicionar produto(s), verificar parametros {erro}')

if __name__ == '__main__':
    import uvicorn
    uvicorn.rum("main:app", host="127.0.0.1", port=8000,log_level="info", reload=True )
# rodar API direto com Python - python main.py