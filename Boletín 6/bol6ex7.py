''' 7. Escribir un programa que pida o usuario unha palabra e mostre por pantalla o número de veces que conten cada vogal.'''

palabra = input("Ingrese unha palabra: ")
vogais = ["a", "e", "i", "o", "u"]

for vogal in vogais:
    if vogal in palabra:
        print(f"{vogal}: {palabra.count(vogal)}")
