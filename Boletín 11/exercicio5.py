# Realizar un programa para a xestión de Inventario. O programa ten que facer as seguintes operacións sobre un ficheiro CSV:
# Calculo do valor total do inventario: Dado un ficheiro produtos.csv (con columnas: id, nome, prezo, stock), o programa ten realizar o cálculo (prezo × stock).
# Existencias baixas: Crea un novo ficheiro baixo_stock.csv que conteña só os produtos cun número de existencias inferior a 5 unidades.

try:
    baixo_stock = []
    with open("produtos.csv","r") as f:
        next(f)
        for linea in f.readlines():
            lineadividida = linea.split(',')
            print(f"{lineadividida[1]}: {int(lineadividida[2]) * int(lineadividida[3])}")
            baixo_stock.append(linea + "\n")

    with open("baixo_stock.csv","w") as f:
        for line in baixo_stock:
            f.write(line)

except FileNotFoundError:
    print("Ficheiro produtos.csv non atopado.")