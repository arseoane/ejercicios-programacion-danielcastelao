#Xerar contrasinal de 6-12 caracteres con letras minúsculas e maiúsculas, símbolos e números.
from random import randint

contador = 0
caracteres = randint(6, 12)
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maiusculas = []
for letra in minusculas:
    maiusculas.append(letra.upper())

simbolos = ['#', '@', '/', '?', '*', '!']
numeros = range(1, 9)

for n in range(1, caracteres):
    if randint(0, 3) == 0:
        print(minusculas[randint(0, len(minusculas) - 1)], end='')
    elif randint(0, 3) == 1:
        print(maiusculas[randint(0, len(maiusculas) - 1)], end='')
    elif randint(0, 3) == 2:
        print(numeros[randint(0, len(numeros) - 1)], end='')
    elif randint(0, 3) == 3:
        print(simbolos[randint(0, len(simbolos) - 1)], end='')
