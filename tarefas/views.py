from flask import Blueprint, jsonify, request
from tarefas.models import exibirLista, adicionar

tarefas = Blueprint("tarefas", __name__)

@tarefas.route("/tarefas", methods=['GET'])
def listar():
    return jsonify(exibirLista()), 200

@tarefas.route("/tarefas", methods=['POST'])
def incluir():
    try:
        valor = request.json['nome']
        adicionar(valor)
        return jsonify({"sucesso": True}), 200
    except:
        return jsonify({"sucesso": False}), 400