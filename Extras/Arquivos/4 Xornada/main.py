import csv

with open("resultados4xornada.csv", "r") as arquivo:
    datos = csv.reader(arquivo)
    for fila in datos:
        print(fila)

with open("resultados4xornada.csv", "w") as arquivo:
    arquivo.write("Bettis,Villareal,4,2")