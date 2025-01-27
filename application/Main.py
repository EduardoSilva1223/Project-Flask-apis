###
# importando bibliotecas
###
from flask import jsonify
from flask_restful import Resource, reqparse
from mongoengine import NotUniqueError
from .model import UserModel
import re


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="o  Campo Nome não pode ser vazio"
                          )
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="o Nome não pode ser vazio"
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="o  Nome não pode ser vazio"
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="o Nome não pode ser vazio"
                          )
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="o Nome não pode ser vazio"
                          )


class Users(Resource):   # Definindo classes da api.
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def validate_cpf(self, cpf):  # Algoritimo de CPF

        # Has the correct mask?
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Grab only numbers
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Does it have 11 digits?
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validate first digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9],
                                                  range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validate second digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10],
                                                  range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def post(self):
        data = _user_parser.parse_args()
        if not self.validate_cpf(data["cpf"]):
            return {"message": "CPF is invalid"}, 400
        try:
            response = UserModel(**data).save()
            return {"message": "user %s  included" % response.id}
        except NotUniqueError:
            return {"message": "CPF alredy exists in mongo"}, 401

    def get(self, cpf):
        response = UserModel.objects(cpf=cpf)

        if response:
            return jsonify(response)
        return {"message": "CPF not exists in the base"}, 400
