import sqlite3 as sql
from json import dumps
from flask import Flask, make_response

app= Flask(__name__)
banco = "cart.db"
#
# Comandos SQL
# contagem = "SELECT COUNT(*) FROM Carrinho;"
criar_table = "CREATE TABLE IF NOT EXISTS Carrinho (id_prod INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço REAL NOT NULL, Quantidade INTEGER NOT NULL, Descrição TEXT NOT NULL);"
select_todos = "SELECT * FROM Carrinho;"
truncate = "DELETE FROM Carrinho;" #"TRUNCATE TABLE carrinho;"
select_id = "SELECT * FROM Carrinho WHERE id_prod like ?;"
delete_id = "DELETE FROM Carrinho WHERE id_prod = ?;"
#inserir_prod = "INSERT INTO Carrinho VALUES (:id,:Nome,:Preco,:Quantidade,:Descrição,);"
atualiza_prod = "UPDATE Carrinho SET Quantidade = ? WHERE id_prod like ?;" 


def abrir_conexao(banco):
    conn = sql.connect(banco) #connection to db
    cursor = conn.cursor() #create a cursor
    return conn, cursor

def fechar_conexao(conn):
    conn.commit()
    conn.close()

@app.get('/') # FUNCIONANDO
def home(): 
    return ("SEJA BEM VINDO(A) A API ORGANICOS "), 200

@app.post('/criar_tabela') # FUNCIONADO
def criar_tabela(): 
    conn, cursor = abrir_conexao(banco)
    resultado = cursor.execute(criar_table)
    fechar_conexao(conn)
    return {'Tabela': f'{resultado} criada.'}, 201

@app.get('/consulta') # FUNCIONANDO
def consulta_tabela():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_todos).fetchall() 
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}, 200

@app.get('/consulta/<id_prod>') #Funcionando 
def consulta_id(id_prod):
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_id, [id_prod]).fetchall() 
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}, 200

@app.put('/update/<id_prod>/<Quantidade>') # testando - Executa como se estivesse correto porem não altera o banco
def update_set_quantidade(id_prod,Quantidade):
    try:
        conn, cursor = abrir_conexao(banco)
        cursor.execute(atualiza_prod, [Quantidade, id_prod])
        return (f'id {id_prod} - Quantidade alterada para {Quantidade} com sucesso'), 202
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conn)
        return (f'Erro ao adicionar produto(s), verificar parametros {resultado}'), 400

@app.delete('/deleta') # FUNCIONANDO
def deleta_tabela():
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Carrinho apagado!'}, 204

@app.delete('/deleta_id/<id_prod>') # FUNCIONANDO, MAS A MANSAGEM DE RETURN NÃO VOLTA
def deleta_id(id_prod):
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(delete_id, [id_prod])
    fechar_conexao(conexao)
    return {'mensagem': 'produto deletado com sucesso'}, 204


@app.post('/alimentar/<id_prod>/<name>/<value>/<quantity>/<desc>') # FUNCIONANDO
def alimentar_tabela(id_prod, name, value, quantity, desc):
    try:
        conn, cursor = abrir_conexao(banco)
        data = [
        #(1,'Cacau',12.5,3,'Do Brasil'),
        (id_prod,name,value,quantity,desc)
        ]
        cursor.executemany('INSERT INTO Carrinho VALUES(?,?,?,?,?)', data)
        resultado = cursor.execute(select_todos)
        fechar_conexao(conn)
        return(f"{name} Cadastrado com sucesso") , 202
    except sql.Error as erro:
        resultado = erro
        fechar_conexao(conn)
        return (f'Erro ao adicionar produto(s), verificar parametros {erro}'), 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)