from flask import Flask, request, jsonify, make_response
import json


class Cliente:

    #construtor
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def get_cliente_data(self):
        data = [
            {
                'nome': self.nome,
                'telefone': self.telefone,
                'cpf': self.cpf
            }
        ]
        data_json = json.dumps(data)
        return data_json