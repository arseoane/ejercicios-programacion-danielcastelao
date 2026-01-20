import json

datos = {
    'a': 2,
    'b': 3,
    'c': 4,}

with open("exemplo.json", "w") as arquivo:
    json.dump(datos, arquivo)

with open("exemplo.json", "r") as arquivo:
    datoJson = json.load(arquivo)
    print(datoJson)
    print(type(datoJson))