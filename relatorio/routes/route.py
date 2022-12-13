
from flask import Blueprint, jsonify

#importar execuções de comandos sql
from controllers import controller
from configs.db_config import Server_connect


routs_blueprint = Blueprint('routs', __name__)

@routs_blueprint.route('/')
def index():
    return """  <a href='http://127.0.0.1:5000/sales'>Vendas realizadas</a> </br>
                <a href='http://127.0.0.1:5000/best_sellers'>Mais vendidos</a></br>
                <a href='http://127.0.0.1:5000/amount_sales'>Total de vendas</a></br>
                <a href='http://127.0.0.1:5000/top_ten'>Produtos mais vendidos</a></br>
                <a href='http://127.0.0.1:5000/less_sold'>Produtos menos vendidos</a></br>
                <a href='http://127.0.0.1:5000/get_iten/'>Buscar item</a></br>
                <a href='http://127.0.0.1:5000/clean_table'>Limpar Tabela</a></br>
                <a href='http://127.0.0.1:5000/create_table'>Criar Tabela</a></br>
                <a href='http://127.0.0.1:5000/popular_table'>Populat tabela</a></br>
        """


@routs_blueprint.route('/sales', methods=["GET"])  
def get_vendas():
    if controller. return_vendas() == []:
        return{"Menssage": "No items sold"}, 404
    else:
        return controller.return_vendas(), 200

@routs_blueprint.route('/best_sellers', methods=["GET"])
def get_top_selling():
    if controller.return_top_selling() == []:
        return{"Menssage": "No items sold"}, 404
    else:
        return controller.return_top_selling(),200

@routs_blueprint.route('/amount_sales', methods=["GET"])
def get_amount_sales():
    if controller.amount_sales() == []:
        return{"Menssage": "No items sold"}, 404
    else:
        return controller.amount_sales(), 200

@routs_blueprint.route('/top_ten', methods=["GET"])
def get_top_ten():
    if controller.top_ten() ==[]:
        return{"Menssage": "No items sold"}, 404
    else:
        return controller.top_ten(), 200

@routs_blueprint.route('/less_sold', methods=["GET"])
def get_less_sold():
    if controller.less_sold() == []:
        return{"Menssage": "No items sold"}, 404
    else:
        return controller.less_sold(), 200

@routs_blueprint.route('/get_iten/<name>', methods=["GET"])
def get_iten(name):
    if controller.get_iten(name) == []:
        return{"Menssage": "iten not found"}, 404
    return controller.get_iten(name), 200

@routs_blueprint.route('/create_table', methods=["POST"])
def create_table():
    if controller.create_table()["Menssage"] != "Created reporting table!!!":
        return{"Menssage": "Error creating table"}, 404
    else:
        return controller.create_table()

@routs_blueprint.route('/clean_table', methods=["DELETE"])
def clean_table():
    if controller.clean_table()["Menssage"] != "successfully cleared table!!!":
        return{"Menssage": "Error clearing table"}, 404
    else:
        return {"Menssage":"successfully cleared table!!!"}, 204

@routs_blueprint.route('/popular_table', methods=["POST"])
def popular_table():
    if controller.popular_table()["Menssage"] != "items successfully created!!!":
        return{"Menssage": "Error to popular table"}, 404
    else:
        return controller.popular_table(), 201