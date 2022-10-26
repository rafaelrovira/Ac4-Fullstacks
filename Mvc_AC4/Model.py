from flask import Flask, request, jsonify, make_response


texto = "Seja bem vindo a tela inicial"



class Welcome():

    def hello_world():
        return texto