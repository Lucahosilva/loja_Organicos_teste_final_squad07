from pymongo import MongoClient
from flask import Flask, request
import configuracao

conexao = MongoClient(configuracao.conexaoMongo)
db = conexao['Catalogo']

app = Flask(__name__)

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


@app.route('/consulta_catalogo', methods=["GET"])
def consulta_catalogo():
    cursor = db['Produtos'].find()
    resultado_db = list(cursor)
    for item in resultado_db:
        item.pop('_id')

    if resultado_db:
        return {'successful': True, 'status': 200, 'resultado': resultado_db}, 200
    else:
        return {'successful': False, 'status': 404, 'erro': "Falha na consulta"}, 404

@app.route('/consulta_produto', methods=["GET"])
def consulta_produto():
    parametros = request.args.to_dict()
    if not parametros:
        return {'successful': False, 'status': 400, 'message': "Nenhum parâmetro recebido"}, 400
    else:
        chave = list(parametros.keys())[0]
        valor = parametros.get(list(parametros.keys())[0])
        if valor.isnumeric():
            valor = int(valor)
        elif is_number(valor):
            valor = float(valor)
        
        if len(parametros) > 1:
            return {'successful': False, 'status': 400, 'message': "Somente um parâmetro será aceito na consulta"}, 400
        else:
            produto = db['Produtos'].find({chave: valor})
            produto = list(produto)
            if produto:
                produto[0].pop('_id')
                return {'successful': True, 'status': 200, 'produto': produto}, 200
            else:
                return {'successful': False, 'status': 404, 'error': 'Produto não encontrado'}, 404



@app.route('/cadastro', methods=['POST'])
def cadastro():
    if request.get_json(silent=True):
        padrao = ["id", "nome", "valor", "descricao"]
        parametros = request.json
        if set(padrao).issubset(set(parametros.keys())): 
            db["Produtos"].insert_one(parametros)
            return {'successful': True, 'status': 200, 'resultado': 'Produto cadastrado com sucesso'}, 200
        else:
            return {'successful': False, 'status': 400, 'resultado': "Parâmetros insuficientes, para cadastro os seguintes itens são obrigatórios:  {'id': x, 'nome': x, 'valor': x, 'descricao': x}"}, 400

    else:
        return {'successful': False, 'status': 400, 'erro': 'Esperava receber um json no corpo da requisição'}, 400   


@app.route('/alterar_produto', methods=['PUT'])
def alterar_produto():
    if request.get_json(silent=True):
        parametros = request.json
        if "nome" not in parametros:
            return {'successful': False, 'status': 404, 'error': "Keyerror chave 'nome' não encontrada"}, 404
        else:
            for chave, valor in parametros.items():
                db['Produtos'].update_one(
                    {'nome': parametros['nome']},
                    {'$set':
                        {chave: valor}
                    }
                )
        return {'successful': True, 'status': 200, 'message': 'Produto alterado com sucesso'}, 200
    else:
        return {'successful': False, 'status': 400, 'error': "Parâmetros insuficientes, para alteração os seguintes itens são obrigatórios:  {'nome': x, 'Campo alterado': 'Alteração'}"}, 400


@app.route('/deletar', methods=['DELETE'])
def deletar_produto():
    if request.get_json(silent=True):
        parametros = request.json
        if 'nome' not in parametros:
            return {'successful': False, 'status': 404, 'error': "Keyerror chave 'nome' não encontrada"}, 404
        else:
            produto = db['Produtos'].find_one({'nome': parametros['nome']})
            if produto: 
                db['Produtos'].delete_one({'nome': parametros['nome']})
                return {'successful': True, 'status': 200, 'message': 'Produto deletado com sucesso'}, 200
            else: 
                return {'successful': False, 'status': 404, 'error': 'Produto não encontrado'}, 404
    else:
        return {'successful': False, 'status': 400, 'error': 'Esperava receber um json no corpo da requisição'}, 400

if __name__ == "__main__":
    app.run(debug=True)