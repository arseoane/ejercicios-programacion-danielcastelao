#ahorcado
from random import randint
vidas = 5
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
    indices = [i for i, c in enumerate(palabra) if c == letra]
    if letra in palabrac:
        for indice in indices:
            adivinar = adivinar[:indice] + letra + adivinar[indice+1:]


    else:
        print(f"La letra {letra} non está.")
        vidas -= 1
        print(f"Quédanche {vidas} intentos.")

    if vidas == 0:
        print("Perdiches!")
        print(f"A palabra era: {palabra}")
        break

if adivino:
    print("Vitoria!")