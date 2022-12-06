from pymongo import MongoClient
from flask import Flask, request
import configuracao

conexao = MongoClient(configuracao.conexaoMongo)
db = conexao['Catalogo']

app = Flask(__name__)


@app.route('/consulta_cadastro', methods=["GET"])
def consulta_catalogo():
    cursor = db['Produtos'].find()
    resultado_db = list(cursor)
    for item in resultado_db:
        item.pop('_id')

    if resultado_db:
        return {'successful': True, 'status': 200, 'resultado': resultado_db}
    else:
        return {'successful': False, 'status': 404, 'erro': "Falha na consulta"}


@app.route('/cadastro', methods=['POST'])
def cadastro():
    if request.get_json(silent=True):
        padrao = ["id", "nome", "valor", "descricao"]
        parametros = request.json
        if set(padrao).issubset(set(parametros.keys())): 
            db["Produtos"].insert_one(parametros)
            return {'successful': True, 'status': 200, 'resultado': 'Produto cadastrado com sucesso'}
        else:
            return {'successful': False, 'status': 400, 'resultado': "Parâmetros insuficientes, para cadastro os seguintes itens são obrigatórios:  {'id': x, 'nome': x, 'valor': x, 'descricao': x}"}

    else:
        return {'successful': False, 'status': 400, 'erro': 'Esperava receber um json no corpo da requisição'}   


def alterar_produto_pelo_nome(parametros):
    if not parametros:
        return "Parâmetros insuficientes, para cadastro os seguintes itens são obrigatórios:  {'nome': x, 'Campo alterado': 'Alteração'}"
    elif "nome" not in parametros:
        return "Parametros insuficientes, chave: 'nome' não encontrada!"
    else:
        for chave, valor in parametros.items():
            db['Produtos'].update_one(
                {'nome': parametros['nome']},
                {'$set':
                    {chave: valor}
                }
            )
    return "Produto alterado com sucesso!"


@app.route('/deletar', methods=['delete'])
def deletar_produto():
    if request.get_json(silent=True):
        parametros = request.json
        if 'nome' not in parametros:
            return {'successful': False, 'status': 404, 'error': "Keyerror chave 'nome' não encontrada"}
        else:
            produto = db['Produtos'].find_one({'nome': parametros['nome']})
            if produto: 
                db['Produtos'].delete_one({'nome': parametros['nome']})
                return {'successful': True, 'status': 200, 'message': 'Produto deletado com sucesso'}
            else: 
                return {'successful': False, 'status': 404, 'error': 'Produto não encontrado'}
    else:
        return {'successful': False, 'status': 400, 'error': 'Esperava receber um json no corpo da requisição'}

if __name__ == "__main__":
    app.run(debug=True)