from pymongo import MongoClient
import configuração

conexao = MongoClient(configuração.conexaoMongo)
db = conexao['Catalogo']

def consulta_catalogo():
    cursor = db['Produtos'].find()
    resultado_db = list(cursor)
    return resultado_db
    