
from flask import Flask, Blueprint
from routes.route import routs_blueprint

app = Flask(__name__)

app.register_blueprint(routs_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
    