from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List, Optional
import mysql.connector as sql

app = FastAPI()

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


def connect_db(dicionario=True):
    conexao = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "root",
        database = "db_relatorio"
    )
    cursor = conexao.cursor(dictionary=dicionario)
    return conexao, cursor

list_items = """select * from table_vendas;"""
    

@app.get('/items')
async def get_items():
    conexao, cursor = connect_db()
    cursor.execute(list_items)
    dados = cursor.fetchall()
    cursor.close()
    if dados != []:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get('/items/{item_name}')
async def get_item(item_name: str):
    print(item_name)
    conexao, cursor = connect_db()
    cursor.execute(f"SELECT produto, quant, valor FROM table_vendas WHERE produto LIKE '%{item_name}%';")
    dados = cursor.fetchall()
    cursor.close()
    if dados != []:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get('/best_sellers')
async def get_best_sellers():
    conexao, cursor = connect_db()
    cursor.execute(f"SELECT produto, quant FROM table_vendas order by quant DESC;")
    dados = cursor.fetchall()
    cursor.close()
    if dados != []:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get('/top_ten')
async def get_top_ten():
    conexao, cursor = connect_db()
    cursor.execute(f"SELECT produto, quant FROM table_vendas order by quant DESC LIMIT 10")
    dados = cursor.fetchall()
    cursor.close()
    if dados != []:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete('/clean_table')
async def delete_all_registers():
    conexao, cursor = connect_db()
    cursor.execute(f"TRUNCATE TABLE table_vendas")
    dados = cursor.fetchall()
    cursor.close()
    raise HTTPException(status_code=204, detail="No Content")

@app.post('/popular_table')
async def popular_table_registers():
    conexao, cursor = connect_db()
    cursor.execute(group_itens)
    conexao.commit()
    cursor.close()
    raise HTTPException(status_code=201, detail="Created")

@app.get('/less_sold')
async def get_less_sold():
    conexao, cursor = connect_db()
    cursor.execute(f"SELECT produto, quant FROM table_vendas order by quant ASC LIMIT 10")
    dados = cursor.fetchall()
    cursor.close()
    if dados != []:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get('/top_sales')
async def top_sales(init: int = 1, limit: int = 3):
    conexao, cursor = connect_db()
    cursor.execute(f"""
                    SELECT produto, quant, valor, SUM(quant * valor) AS total 
                    FROM  table_vendas 
                    GROUP BY produto, quant, valor 
                    ORDER BY total DESC LIMIT {init}, {limit};
                """)
    dados = cursor.fetchall()
    cursor.close()
    if dados != []:
        return dados
    else:
        raise HTTPException(status_code=404, detail="Item not found")




if __name__ =="__main__":
    import uvicorn

    uvicorn.run("main:app", log_level='info', reload=True)