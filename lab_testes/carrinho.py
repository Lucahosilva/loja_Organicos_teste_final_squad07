'''
Controle de carrinho utilizando SQLite

* Adição de produtos - Ok 
* Remoção de produtos - OK
* Alteração de quantidade
* Consulta de itens - ok

# Cursor e Executando comandos
## Criando tabela
resultado = cursor.execute(create_table)
## Inserindo dados
cursor.execute(insert)
## Consultando dados
resultado = cursor.execute(select)
resultado.fetchone()
## Confirmando alterações
conexao.commit()
conexao.rollback()

'''

from flask import Flask, redirect, url_for, request, render_template
import sqlite3 as sql
banco = 'bcarrinho.db'

app = Flask(__name__)

def abrir_conexao(banco):
    conexao = sql.connect(banco)
    cursor = conexao.cursor()

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

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

## criar taela 
@app.route('/criar')
def cria_table():
    try:
        
        print("Tabela criada com sucesso!")
    except sql.Error as erro:
        print("Tabela ja cadastrada:", erro) 
        
#cria_table()

## insere produto 
def inser_prod():
    try:
        cursor.execute("INSERT INTO carrinho VALUES(5,'cacau',12,5,'Do Brasil')")
        conexao.commit()
    except sql.Error as erro:
        print("Erro ao adicionar produto, verificar parametros.", erro) 
        conexao.close()
#inser_prod()

## Adição de produtos
def inser_vprod():
    data = [
       (1,'Cacau',12.5,3,'Do Brasil'),
       (2,'Arroz',10,2,'Do Brasil'),
       (3,'Feijão',8,5,'Do Brasil'),
       (4,'Batata',11,10,'Do Brasil'),
       (5,'Café',8,5,'Do Brasil'),
       (6,'Vinho',15,2,'Da Argentina'),
    ]
    try:
        cursor.executemany('INSERT INTO carrinho VALUES(?,?,?,?,?)', data)
        conexao.commit()
        resultado = cursor.execute("select * from carrinho")
        for linha in resultado:
            print(linha)
    except sql.Error as erro:
        print("Erro ao adicionar produto'(s)', verificar parametros.", erro) 
        conexao.close()
#inser_vprod()

## Remoção de produtos
@app.route('/delete/<id_prod>')
def delete_name(id_prod):
    try:
        conexao, cursor = abrir_conexao(banco)
        resultado = cursor.execute(delete_id, [id_prod]).rowcount
        fechar_conexao(conexao)
    except sql.Error as erro:
        print("Erro ao excluir o produto:", erro) 
        conexao    
    return {'message': f'{resultado} aluno(s) foram removido(s)!'}

def remove_prod():
    try:
        cursor.execute("DELETE from carrinho WHERE id_prod = '2' ")
        conexao.commit()
        resultado = cursor.execute("select * from carrinho")
        for linha in resultado:
            print(linha)
            print("ITEM EXCLUIDO COM SUCESSO!")
        conexao.close()
    except:
        pass
   
#remove_prod()

## Alteração de quantidade
def mpreco():
    pass
#mpreco()

## Consulta de itens - pelo ID
def consulta():
    try:
        resultado = cursor.execute("select * from carrinho where id_prod ='2' ")
        for linha in resultado:
            print()
            print("Produto selecionado:")
            print(linha)
    except sql.Error as erro:
        print("Banco de dados vazio:", erro) 
        conexao.close()
#consulta()

if __name__ == "__main__":
    app.run(debug=True)