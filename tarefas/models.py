lista = [
    {"id": 1, "nome": "Mateus"},
    {"id": 2, "nome": "Goku"},
    {"id": 3, "nome": "Picculo"}
]

def exibirLista():
    return lista

def adicionar(nome):
    id = len(lista) + 1
    pessoa = {"id": id, "nome": nome}
    lista.append(pessoa)