import mysql.connector as sql

def Server_connect(dicionario=True):
    conexao = sql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="db_relatorio"
    )
    if conexao:
        cursor = conexao.cursor(dictionary=dicionario)
        return conexao, cursor 
    else:
        return {"Erro": "Falha de conexão com banco de dados"}