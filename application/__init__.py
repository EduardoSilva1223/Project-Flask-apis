from flask import Flask
from flask_restful import Api
from .db import ini_db
from .Main import User, Users


def create_app(config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config)
    ini_db(app)

    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')
    return app
