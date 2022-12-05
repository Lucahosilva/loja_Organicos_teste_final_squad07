
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


@routs_blueprint.route('/sales')  
def get_vendas():
    return controller.return_vendas(), 200

@routs_blueprint.route('/best_sellers')
def get_top_selling():
    return controller.return_top_selling(),200

@routs_blueprint.route('/amount_sales')
def get_amount_sales():
    return controller.amount_sales(), 200

@routs_blueprint.route('/top_ten')
def get_top_ten():
    return controller.top_ten(), 200

@routs_blueprint.route('/less_sold')
def get_less_sold():
    return controller.less_sold(), 200

@routs_blueprint.route('/get_iten/<name>')
def get_iten(name):
    return controller.get_iten(name), 200

@routs_blueprint.route('/create_table')
def create_table():
    return controller.create_table()

@routs_blueprint.route('/clean_table')
def clean_table():
    controller.clean_table()
    return {"Mensagem": "item table cleared successfully"}, 200

@routs_blueprint.route('/popular_table')
def popular_table():
    return controller.popular_table(), 200