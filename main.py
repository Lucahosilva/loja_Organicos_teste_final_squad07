import sqlite3 as sql
import pandas as pd
import datetime
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

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

# ROTAS

@app.route('/')
def method_name():

    pass

@app.route('/route_name')
def method_name():
    pass

@app.route('/route_name')
def method_name():
    pass

@app.route('/route_name')
def method_name():
    pass

@app.route('/consulta/<id>')
def consulta_id():
    try:
        resultado = cursor.execute("select * from carrinho where id_prod ='2' ")
        for linha in resultado:
            print()
            print("Produto selecionado:")
            print(linha)
    except sql.Error as erro:
        print("Banco de dados vazio:", erro) 
        conn.close()
    pass

if __name__ == "__main__":
    app.run(debug=True)