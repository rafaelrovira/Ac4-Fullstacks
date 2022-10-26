from flask import Flask, redirect, render_template
from Model import Welcome
from Model_Cliente import Cliente




# Configs
app = Flask(__name__)


# Rotas
@app.route('/')
def home():
    return Welcome.hello_world()


@app.route('/cliente')
def cliente():
    cliente1 = Cliente('Rafael',41754025587,11968486524)
    return cliente1.get_cliente_data()


# Main
if __name__ == '__main__':
    app.run(debug=True,port= 5000)