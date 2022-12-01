from pymongo import MongoClient
import configuracao

conexao = MongoClient(configuracao.conexaoMongo)
db = conexao['Catalogo']

def consulta_catalogo():
    cursor = db['Produtos'].find()
    resultado_db = list(cursor)
    print(resultado_db)
    return resultado_db

def cadastro(parametros):
    padrao = ["id", "nome", "valor", "descricao"]
    if set(padrao).issubset(set(parametros.keys())): 
        db["Produtos"].insert_one(parametros)
        print('Produto cadastrado com sucesso!')
    else:
        print("Parâmetros insuficientes, para cadastro os seguintes itens são obrigatórios:  {'id': x, 'nome': x, 'valor': x, 'descricao': x}")
        

def alterar_produto_pelo_nome(parametros):
    if not parametros:
        print("Parâmetros insuficientes, para cadastro os seguintes itens são obrigatórios:  {'nome': x, 'Campo alterado': 'Alteração'}")
    elif "nome" not in parametros:
        print("Parametros insuficientes, chave: 'nome' não encontrada!")
    else:
        for chave, valor in parametros.items():
            db['Produtos'].update_one(
                {'nome': parametros['nome']},
                {'$set':
                    {chave: valor}
                }
            )

def deletar_produto(parametros):
    produto = db['Produtos'].find_one({'nome': parametros['nome']})
    if produto: 
        db['Produtos'].delete_one({'nome': parametros['nome']})
        print("message: Produto deletado com sucesso!")
        return {'message': 'Produto deletado com sucesso!'}
    else: 
        print("error': 'Produto não encontrado!")
        return {'error': 'Produto não encontrado!'}
    
    

deletar_produto({'nome':'Banana'})