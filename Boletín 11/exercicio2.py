# Ler un ficheiro de texto e contar cantas veces aparece cada palabra.
# Solicita ao usuario o nome dun ficheiro .txt.
#
#
# Mostra a frecuencia de cada palabra (ignorando maiúsculas/minúsculas e signos de puntuación).
#
#
# Gárdase un resumo nun novo ficheiro resumo_palabras.txt.

nomeficheiro = input("Nome do ficheiro a ler: ")

with open(nomeficheiro, "r") as ficheiro:
    for linea in ficheiro:
        linea = linea.lower()
        for c in ",.!?":
            linea = linea.replace(c, "")

        palabras = linea.split()
        frecuencia = {}

with open("resumo_palabras.txt", "a") as ficheiro:
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    ficheiro.write(str(frecuencia))