###
# importando bibliotecas
###
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


# definindo variaveis globais

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.StringField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.EmailField(required=True)
    birth_date = db.DateTimeField(requiered=True)


class Users(Resource):   # Definindo classes da api.
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def post(self):
        return {"message": "teste"}

    def get(self, cpf):
        return {"message": "CPF"}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
