from flask import Flask, jsonify, request
from random_data import data
import funcoes

app = Flask(__name__)

@app.route("/", methods=("GET", ))
def index():
    return jsonify({"status":200, "message": "API do Marcos Felipe Mendes Rocha"})

@app.route("/aleatorios", methods=("GET", ))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a })

@app.route("/argumentos/<string:nome>", methods=("GET", ))
def argumento(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos", methods=("GET", ))
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@app.route("/idades", methods=("GET", ))
def idades():
    num = funcoes.maiores(data)
    return jsonify({"status": 200, "data": num})

@app.route("/salario", methods=("GET", ))
def salario():
    salario = funcoes.salario(data)
    return jsonify({"status": 200,"data": salario})

@app.route("/maior_salario", methods=("GET", ))
def max():
    max = funcoes.maxsalarios(data)
    return jsonify({"status": 200, "data": max})

@app.route("/profissoes", methods=("GET", ))
def profissoes():
    profissoes = funcoes.media_profissao(data)
    return jsonify({"status": 200, "data":profissoes})

@app.route("/idade/<string:tipo>")
def sexos(tipo: str):
    
    sexo = funcoes.sexoidade(data)
    cout = sexo[0]
    coutm = sexo[1]
    inter = sexo[2] , sexo[3]
    
    if tipo == "f":
        return jsonify({"status":200, "data":cout})
    elif tipo == "m":
        return jsonify({"status":200, "data":coutm})
    elif tipo == "intervalo":
        return jsonify({"status":200, "data":inter})
