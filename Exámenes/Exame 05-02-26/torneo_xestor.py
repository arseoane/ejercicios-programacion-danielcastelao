from equipo import *
from torneo import *
from equipoNonExisteError import *

celta = Equipo("Celta")
torneo = Torneo("Torneo",celta,3,1)

try:
    while True:
        print("1. Rexistrar resultado dun partido")
        print("2. Mostrar clasificación")
        print("3. Consultar equipo")
        print("4. Estatísticas do torneo")
        print("0. Saír")

        opcion = input("Opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            torneo.rexistrar_encontro(input("Rexistrar (celta-madrid 1-0): "))
        elif opcion == "2":
            print(torneo.get_clasificacion())
        elif opcion == "3":
            print(torneo.get_equipo(input("Nome de equipo: ")))
        elif opcion == "4":
            print(torneo.get_equipos())

except Exception as e:
    print(f"Error: {e}")