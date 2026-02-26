import csv

with open("resultados4xornada.csv", "r") as arquivo:
    datos = csv.reader(arquivo)
    for fila in datos:
        print(fila)

with open("resultados4xornada.csv", "a") as arquivo:
    arquivo.write("\nBettis,Villareal,4,2\n")