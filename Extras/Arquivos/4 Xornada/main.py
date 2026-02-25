import csv

with open("resultados4xornada.csv", "r") as arquivo:
    datos = csv.reader(arquivo)
    for fila in datos:
        print(fila)