'''
Controle de carrinho utilizando SQLite

* Adição de produtos - Ok 
* Remoção de produtos
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
import sqlite3 as sql

conexao = sql.connect('cart.db')
cursor = conexao.cursor()

## criar taela 
def cria_table():
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS carrinho (id_prod INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço REAL NOT NULL, Quantidade INTEGER NOT NULL, Descrição TEXT NOT NULL)') 
        print("Tabela criada com sucesso!")
    except sql.Error as erro:
        print("Tabela ja cadastrada:", erro) 
        conexao.close()
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
def remove_prod():
    try:
        cursor.execute("DELETE from carrinho WHERE id_prod = '2' ")
        conexao.commit()
        resultado = cursor.execute("select * from carrinho")
        for linha in resultado:
            print(linha)
            print("ITEM EXCLUIDO COM SUCESSO!")
        conexao.close()

    except sql.Error as erro:
        print("Erro ao excluir o produto:", erro) 
        conexao.close()
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