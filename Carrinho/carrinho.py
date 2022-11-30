'''
Controle de carrinho utilizando SQLite

* Adição de produtos
* Remoção de produtos
* Alteração de quantidade
* Consulta de itens

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

# criar taela 

cursor.execute('CREATE TABLE IF NOT EXISTS carrinho (id INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço int NOT NULL, Descrição TEXT NOT NULL)') 

# Adição de produtos

cursor.execute("INSERT INTO carrinho VALUES(2,'Mamão',15,'Mamão do Brasil')")

conexao.commit()

# Remoção de produtos

# Alteração de quantidade

# Consulta de itens

