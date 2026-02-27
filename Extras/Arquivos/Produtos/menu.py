class Producto:
    def __init__(self, nome, cantidade, prezo):
        self.nome = nome
        self.cantidade = cantidade
        self.prezo = prezo

    def __str__(self):
        return f"Nome: {self.nome}\nCantidade: {self.cantidade}\nPrezo: {self.prezo}"

while True:
    lsprods = []

    with open("produtos.csv", "r") as arquivo:
        next(arquivo)
        produtos = arquivo.readlines()
        for produto in produtos:
            prod = Producto(produto.split(",")[0], produto.split(",")[1], produto.split(",")[2])
            lsprods.append(prod)

    print('''1. Listar productos.
2. Crear productos.
99. Saír.
    ''')

    opcion = int(input("Opción: "))

    match opcion:
        case 99:
            exit()
        case 1:
            for prod in lsprods:
                print(prod)

        case 2:
            prod = Producto(input("Nome: "), input("Cantidade: "), input("Prezo: "))
            with open("produtos.csv", "a") as arquivo:
                arquivo.write(f"\n{prod.nome},{prod.cantidade},{prod.prezo}")

        case _:
            print("Opción inválida.")