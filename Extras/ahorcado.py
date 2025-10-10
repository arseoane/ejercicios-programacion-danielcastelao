#ahorcado
from random import randint

adivino = False
palabras = ["zapato", "castelo", "ordenador", "deporte"]
palabra = palabras[randint(0, len(palabras)-1)]
palabrac = []
for car in palabra:
    palabrac.append(car)

adivinar = ""
for car in palabra:
    adivinar += "_"

while not adivino:
    print(adivinar)
    letra = input("\nIngresa unha letra: ")
    if letra in palabrac:
        adivinar[palabrac.find(letra)] = letra

