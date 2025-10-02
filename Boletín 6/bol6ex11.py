import math
'''11. Escribir un programa que pregunte por unha mostra de números, separados por comas, os garde nunha lista e mostre por pantalla a súa media e desviación típica.'''

numeros = []

pedir = int(input("Números a pedir: "))
for i in range(pedir, 0, -1):
    numeros.append(int(input("Número: ")))
media = sum(numeros) / len(numeros)

print(f"Media: {media}")
varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
desviacion = math.sqrt(varianza)

print(f"Desviación estándar: {desviacion}")


