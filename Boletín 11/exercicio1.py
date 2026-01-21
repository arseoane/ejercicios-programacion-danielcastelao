# Crear un programa xestor de notas persoais, que permita ao usuario gardar e consultar notas.
# O usuario pode engadir unha nova nota (texto libre).
#
#
# As notas gárdanse nun ficheiro de texto (notas.txt), unha por liña.
#
#
# O programa pode listar todas as notas gardadas.
#
#
# O usuario pode buscar notas que conteñan unha palabra clave.

while True:
    print('''
Xestor de notas

1) Engadir nova nota.

2) Listar notas gardadas.

3) Buscar notas por palabra clave.

4) Pechar programa.

    ''')

    opcion = input("Ingrese unha opción: ")

    try:
        if opcion == "4":
            exit()

        elif opcion == "1":
            with open("notas.txt", "a+") as notas:
                notas.write(str(input("Ingrese nota: ")) + "\n")

        elif opcion == "2":
            print("Notas gardadas: ")
            with open("notas.txt", "r") as notas:
                notaslist = notas.read()
                for linea in notaslist.split("\n"):
                    print(linea)

        elif opcion == "3":
            query = input("Ingresa palabra clave: ")
            with open("notas.txt", "r") as notas:
                notaslist = notas.read()
                for linea in notaslist.split("\n"):
                    if query in linea:
                        print(linea)

    except FileNotFoundError:
        with open("notas.txt", "w") as notas:
            notas.write("")

    except Exception as e:
        print("Error:", e)