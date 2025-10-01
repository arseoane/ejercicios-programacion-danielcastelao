''' 6. Escribir un programa que pida o usuario unha palabra e mostre por pantalla si é un palíndromo.'''

palabra = input("Ingrese unha palabra: ")
palabra = palabra.lower()
contador = 0

for primera, ultima in zip(palabra, palabra[::-1]):
    if primera == ultima:
        contador += 1

if contador == len(palabra):
    print(f"A palabra '{palabra}' é un palíndromo.")
else:
    print(f"A palabra '{palabra}' non é un palíndromo.")
