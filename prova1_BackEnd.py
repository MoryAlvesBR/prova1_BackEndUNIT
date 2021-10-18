from flask import Flask, request
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

receitinhas = [
    {
        "name": "Coxinha de Frango",
        "ingredients": [
            "Farinha de trigo",
            "Água",
            "Margarina",
            "Cebola",
            "Caldo de carne",
            "Leite",
            "Farinha de rosca",
            "Frango"
        ],
        "preparation": [
            "Cozinhar tudo",
            "montar as coxinhas",
            "Fritar elas",
            "Ser feliz comendo as coxinhas!"
        ],
        "yield": ["10 porções"]
    },
    {
        "name": "Coxinha de Frango com Catupiry",
        "ingredients": [
            "Farinha de trigo",
            "Água",
            "Margarina",
            "Cebola",
            "Caldo de carne",
            "Leite",
            "Farinha de rosca",
            "Frango",
            "Queijo Catupiry"
        ],
        "preparation": [
            "Cozinhar tudo",
            "montar as coxinhas",
            "Fritar elas",
            "Ser feliz comendo as coxinhas!"
        ],
        "yield": ["10 porções"]
    },
    {
        "name": "Coxinha de Camarão com Catupiry",
        "ingredients": [
            "Farinha de trigo",
            "Água",
            "Margarina",
            "Cebola",
            "Caldo de carne",
            "Leite",
            "Farinha de rosca",
            "Camarão",
            "Queijo Catupiry"
        ],
        "preparation": [
            "Cozinhar tudo",
            "montar as coxinhas",
            "Fritar elas",
            "Ser feliz comendo as coxinhas!"
        ],
        "yield": ["10 porções"]
    },
    {
        "name": "Coxinha de Charque com Catupiry",
        "ingredients": [
            "Farinha de trigo",
            "Água",
            "Margarina",
            "Cebola",
            "Caldo de carne",
            "Leite",
            "Farinha de rosca",
            "Charque",
            "Queijo Catupiry"
        ],
        "preparation": [
            "Cozinhar tudo",
            "montar as coxinhas",
            "Fritar elas",
            "Ser feliz comendo as coxinhas!"
        ],
        "yield": ["10 porções"]
    },
    {
        "name": "Coxinha de Bacalhau com Catupiry",
        "ingredients": [
            "Farinha de trigo",
            "Água",
            "Margarina",
            "Cebola",
            "Caldo de carne",
            "Leite",
            "Farinha de rosca",
            "Bacalhau",
            "Queijo Catupiry"
        ],
        "preparation": [
            "Cozinhar tudo",
            "montar as coxinhas",
            "Fritar elas",
            "Ser feliz comendo as coxinhas!"
        ],
        "yield": ["10 porções"]
    },
]

class Receitas(Resource):
    def get(self):
        return {"status" : 200, "Data" : receitinhas}

    def post(self):
        new_receitas = json.loads(request.data)
        receitinhas.append(new_receitas)
        return {
            "message": "Criada uma nova receitinha!",
            "newValue": new_receitas
        }

class Receita(Resource):
    def get(self, indice):
        try:
            return receitinhas[indice]
        except IndexError:
            mensagem = "O índice informado {} não foi encontrado!".format(indice)
            return {
                "status": "Erro não sei",
                "message": mensagem,
            }
        except:
            mensagem = "Conheço esse erro não boy, tenta outra coisa aí"
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }

    def put(self, indice):
        newValue = json.loads(request.data)
        receitinhas[indice] = newValue
        return {
            "message": "Receitinha atualizada!",
            "newValue": newValue
        }

    def delete(self, indice):
        receitinhas.pop(indice)
        return {
            "message": "Receitinha deletada!",
            "arrayAtual": receitinhas
        }

api.add_resource(Receitas, '/receitas/')
api.add_resource(Receita, '/receita/<int:indice>')

if __name__ == '__main__':
    app.run(debug=True)
