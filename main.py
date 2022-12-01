'''
* Adição de produtos -
* Remoção de produtos - 
* Alteração de quantidade -
* Consulta de itens - 
'''

import sqlite3 as sql
import pandas as pd
import datetime
from flask import Flask, redirect, url_for, request, render_template 
from json import dumps

banco = "cart.db"

# Comandos SQL
contagem = "SELECT COUNT(*) FROM carrinho;"
criar_table = "CREATE TABLE IF NOT EXISTS carrinho (id_prod INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço REAL NOT NULL, Quantidade INTEGER NOT NULL, Descrição TEXT NOT NULL);"
select_todos = "SELECT * FROM carrinho;"
truncate = "DELETE FROM carrinho;" #"TRUNCATE TABLE carrinho;"
select_id = "SELECT * FROM carrinho WHERE id_prod like ?"
delete_id = "DELETE FROM carrinho WHERE id_prod like ?"
insert = "INSERT INTO carrinho VALUES (:id,:Nome,:Preco,:Quantidade,:Descrição,)"
update = '''
UPDATE carrinho SET
    id_prod = :nome,
    Nome = :idade,
    Preço = :filhos,
    Quantidade = :estado,
    Descrição = :altura
WHERE id_prod like :nome  
'''

app = Flask(__name__)

#----- topico 3. carrinho 

def abrir_conexao(banco):
    conn = sql.connect(banco) #connection to db
    cursor = conn.cursor() #create a cursor
    return conn, cursor

def fechar_conexao(conn):
    conn.commit()
    conn.close()

# teste =cursor.execute('''
# SELECT * FROM carrinho

# ''')
# teste = cursor.fetchall()
# print(teste)

#close connection 
#conn.close()

# ROTAS

@app.route('/')
def main():
    return render_template("index.html") 
    
@app.route('/adc_m') # ADICONAR VARIOS ITENS
def inser_vprod():
    conn, cursor = abrir_conexao(banco)
    data = [
       (1,'Cacau',12.5,3,'Do Brasil'),
       (2,'Arroz',10,2,'Do Brasil'),
    ]
    cursor.executemany('INSERT INTO carrinho VALUES(?,?,?,?,?)', data)
    resultado = cursor.execute(select_todos)
    print(resultado)
    fechar_conexao(conn)
    return("Cadastrado, vide console.")

@app.route('/adc') # ADICIONAR 1 ITEM - OK
def inser_prod():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    cursor.execute("INSERT INTO carrinho VALUES(7,'Cerveja',1.50,50,'Do Brasil')")
    conn.commit()
    fechar_conexao(conn)
    print(banco)
    return("Cadastrado, vide console.")

@app.route('/modifir')
def modificar_prod():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE [condition];

    fechar_conexao(conn)
    pass

@app.route('/remover')
def remover_prod():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    #DELETE FROM COMPANY WHERE id_prod = 7;
    fechar_conexao(conn) # fecha o banco
    pass

@app.route('/consul_t') # CONULTAR TABLE POR ID_PROD - OK
def consulta_t():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_todos).fetchall() 
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}

@app.route('/consul') # CONULTAR TABLE POR ID_PROD - OK
def consulta_id():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute("select * from carrinho where id_prod ='3'").fetchall() 
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}

@app.route('/contar') # CONTAGEM DE PRODUTOS - OK
def prod_cont():
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(contagem).fetchone()
    fechar_conexao(conexao)
    return {'Produtos': f'{resultado[0]} Itens no carrinho'}
    
if __name__ == "__main__":
    app.run(debug=True)