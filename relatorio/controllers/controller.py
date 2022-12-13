"""
    Relatório de vendas utilizando MySQL --
    Registro de vendas realizadas --
    Relatório de vendas por produto (mais vendidos) --
    Total de vendas realizadas com quantidade e valor
    Rank de produtos mais vendidos (Top 10)
    Limpar tabela de vendas
    Consulta de vendas
    Crie pelo menos 2 testes para cada rota.

"""

from configs.db_config import Server_connect
from flask import request

group_itens = ("""
                INSERT INTO table_vendas (produto, quant, valor) VALUES
                ('Abóbora',1,2.63),
                ('Abobrinha',9,4.34),
                ('Acelga',5,5.66),
                ('Agrião',2,3.10),
                ('Alcachofra',20,5.86),
                ('Alface',3,7.46),
                ('Alfafa',1,7.24),
                ('Alho-poró',17,4.54),
                ('Almeirão',13,6.89),
                ('Aspargo',16,6.47),
                ('Azeitona',19,3.16),
                ('Batata',11,2.56),
                ('Berinjela',9,2.48),
                ('Bardana',20,7.86),
                ('Beterraba',14,5.73),
                ('Brócolis',10,6.77),
                ('Broto',4,3.55),
                ('Cará',14,6.06),
                ('Cebola',12,5.36),
                ('Cebolinha',8,3.40),
                ('Cenoura',3,6.43),
                ('Chuchu',14,7.87),
                ('Cogumelo',7,4.55),
                ('Couve',3,6.69),
                ('Couve-flor',5,4.84),
                ('Espinafre',11,3.45),
                ('Mandioca',4,5.68),
                ('Mandioquinha',7,2.79),
                ('Nabo',17,7.26),
                ('Palmito',10,5.75),
                ('Pepino',7,3.58),
                ('Picles',8,3.76),
                ('Pimentão',4,2.37),
                ('Quiabo',5,4.50),
                ('Rabanete',11,5.77),
                ('Repolho',9,2.91),
                ('Rúcula',7,7.81),
                ('Seleta',7,4.89),
                ('Salada',10,6.20),
                ('Tomate',13,2.45),
                ('Vagem',18,2.15) ;
            """)

def create_table():
    conexao, cursor = Server_connect()
    #----Criar tabela de vendas----------------------------------- total    REAL NOT NULL,
    cursor.execute('DROP TABLE IF EXISTS table_vendas;')
    cursor.execute( """CREATE TABLE table_vendas(
                        id       INT AUTO_INCREMENT,
                        produto  VARCHAR(50) NOT NULL,
                        quant    INTEGER  NOT NULL,
                        valor    REAL NOT NULL,
                        primary key (id));
                    );
                    """)
    return {"Menssage": "Created reporting table!!!"}


def popular_table():
    #----Popular itens na tabela--------------------------------------
    conexao, cursor = Server_connect()
    cursor.execute(group_itens)
    conexao.commit()
    cursor.close()
    return {"Menssage": "items successfully created!!!"}


def return_vendas():
    #-----retornar todas a vendas----------------------------------------
    conexao, cursor = Server_connect()
    cursor.execute('SELECT produto, quant, valor FROM table_vendas;')
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def return_top_selling():
    #---Retorna os produto por ondem de mais vendidos---------------------
    conexao, cursor = Server_connect()
    cursor.execute("""
                    SELECT produto, quant FROM table_vendas
                    order by quant DESC;
                    """)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def amount_sales():
    #---Total de vendas realizadas com quantidade e valor------------------
    conexao, cursor = Server_connect()
    cursor.execute("""
                    SELECT produto, quant, valor, SUM(quant * valor) AS total 
                    FROM table_vendas group by produto, quant, valor;
                """)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def top_ten():
    #---Rank de produtos mais vendidos (Top 10)----------------------------
    conexao, cursor = Server_connect()
    cursor.execute("""
                    SELECT produto, quant, valor, SUM(quant * valor) AS total 
                    FROM  table_vendas 
                    GROUP BY produto, quant, valor 
                    ORDER BY total DESC LIMIT 10;
                """)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def less_sold():
    #---Rank de produtos menos vendidos (Top 10)----------------------------
    conexao, cursor = Server_connect()
    cursor.execute("""
                    SELECT produto, quant, valor, SUM(quant * valor) AS total 
                    FROM  table_vendas 
                    GROUP BY produto, quant, valor 
                    ORDER BY total ASC LIMIT 10;
                """)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def get_iten(name):
    #---Consulta de vendas----------------------------
    conexao, cursor = Server_connect()
    cursor.execute(f"SELECT produto, quant, valor FROM table_vendas WHERE produto LIKE '%{name}%';")
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def clean_table():
#----Limpar tabela de vendas-----------------
    conexao, cursor = Server_connect()
    cursor.execute("TRUNCATE TABLE table_vendas;")
    cursor.close()
    return {"Menssage": "successfully cleared table!!!"}