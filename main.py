import sqlite3 as sql
import pandas as pd
import datetime


#----- topico 3. carrinho 
#connection to db
conn = sql.connect('cart.db')

#create a cursor
cursor = conn.cursor()

teste =cursor.execute('''
SELECT * FROM carrinho

''')
teste = cursor.fetchall()
print(teste)

#close connection 
conn.close()
