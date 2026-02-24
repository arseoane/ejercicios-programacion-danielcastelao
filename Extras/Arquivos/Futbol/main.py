with open("puntuacions.txt","r") as arquivo:
    contido = arquivo.read()
    contido = contido.split("\n")
    puntuacions_divididas = []

    for linea in contido:
        puntuacions_divididas.append(linea.split(" "))

    for partida in puntuacions_divididas:
        print("===================")
        print(f"{partida[0]} - {partida[1]}")
        print(f"Puntuación: {partida[2].replace('(', '').replace(')', '')}")