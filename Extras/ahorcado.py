#ahorcado
from random import randint
vidas = 5
adivino = False
palabras = ["zapato", "castelo", "ordenador", "deporte"]
palabra = palabras[randint(0, len(palabras)-1)]
def eliminar_acentos_replace(cadena):
    replacements = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U")
    )
    for a, b in replacements:
        cadena = cadena.replace(a, b)
    return cadena
palabra = eliminar_acentos_replace(palabra)
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
        print(f"A letra {letra} non está.")
        vidas -= 1
        print(f"Quédanche {vidas} intentos.")

    if vidas == 0:
        print("\nPerdiches!")
        print(f"A palabra era: {palabra}")
        break

    if "_" not in adivinar:
        adivino = True

if adivino:
    print("\nVitoria!")