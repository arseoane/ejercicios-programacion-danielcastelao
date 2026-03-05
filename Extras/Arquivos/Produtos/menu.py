import pickle
import csv


class Produto:
    def __init__(self, nome, cantidade, prezo):
        self.nome = nome
        self.cantidade = cantidade
        self.prezo = prezo

    def __str__(self):
        return f"Nome: {self.nome}\nCantidade: {self.cantidade}\nPrezo: {self.prezo}"

    def gardar_datos(self, ruta_csv):
        with open(ruta_csv, "w", newline='', encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["nome", "cantidade", "prezo"])
            for produto in self.produtos:
                escritor.writerow(
                    [produto.nome, produto.cantidade, produto.prezo]
                )

    def gardar_datos_binarios(self, ruta):
        with open(ruta, "wb") as f:
            pickle.dump(self.produtos, f)




while True:
    lsprods = []

    with open("produtos.csv", "r") as arquivo:
        next(arquivo)
        produtos = arquivo.readlines()
        for produto in produtos:
            prod = Produto(produto.split(",")[0], produto.split(",")[1], produto.split(",")[2])
            lsprods.append(prod)

    print('''================
1. Listar produtos.
2. Crear produto.
3. Buscar produtos.
0. Saír.
''')


    try:
        opcion = int(input("Opción: "))
        print("================")

        match opcion:
            case 0:
                exit()
            case 1:
                for prod in lsprods:
                    print(prod)

            case 2:
                prod = Produto(input("Nome: "), input("Cantidade: "), input("Prezo: "))
                with open("produtos.csv", "a") as arquivo:
                    arquivo.write(f"\n{prod.nome},{prod.cantidade},{prod.prezo}")

            case 3:
                query = input("Ingrese unha búsqueda: ")

                numresultados = 0
                for prod in lsprods:
                    if query.lower() in prod.nome.lower():
                        numresultados += 1

                if numresultados == 0:
                    print("Non se atoparon resultados.")

                elif numresultados == 1:
                    print(f"Hai {numresultados} resultado de '{query}':\n")
                    for prod in lsprods:
                        if query.lower() in prod.nome.lower():
                            print(prod)

                else:
                    print(f"Hai {numresultados} resultados de '{query}':\n")
                    for prod in lsprods:
                        if query.lower() in prod.nome.lower():
                            print(prod)

            case _:
                print("Opción inválida.")

    except ValueError:
        print("================")
        print("Opción inválida.")

    except Exception as e:
        print("================")
        print(f"Erro: '{e}'.")
