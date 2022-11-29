from pymongo import MongoClient
import configuração

conexao = MongoClient(configuração.conexaoMongo)
db = conexao['Catalogo']

teste = {"teste": "testando"}
db['Produtos'].insert_one(teste)

cursor = db['Produtos'].find()
resultado_db = list(cursor)
print(resultado_db)

