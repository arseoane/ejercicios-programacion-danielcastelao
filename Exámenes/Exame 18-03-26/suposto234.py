import csv


class Asento:
    def __init__(self, numero: str, clase: str) -> None:
        self.numero = numero
        self.clase = clase # "turista", "preferente", "business"
        self.ocupado = False
        self.pasaxeiro = None

    def ocupar(self,pasaxeiro):
        if self.ocupado != True:
            self.ocupado = True
            self.pasaxeiro = pasaxeiro


with open("asentos.csv", "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    asentos = []
    for row in reader:
        asento = Asento(row['Numero'], row['Clase'])
        asento.ocupado = row['Ocupado']
        asento.pasaxeiro = row['Pasaxeiro']
        asentos.append(asento)

while True:

    print("\n Suposto a visualizar:")
    print("1. Suposto 2")
    print("2. Suposto 3")
    print("3. Suposto 4")
    print("0. Saír")

    opcion = int(input("\t[?] Opción > "))
    match opcion:
        case 0:
             exit()

        case 1:
            for asento in asentos:
                if asento.ocupado == False:
                    print(f"Asento: {asento.numero} {asento.clase} libre")
                else:
                    print(f"Asento: {asento.numero} {asento.clase} {str(asento.pasaxeiro)}|{str(asento.ocupado)}")

        case 2:
            print("1. Crear asentos libres.")
            print("2. Primeiro asento libre dunha clase.")
            print("3. Ocupación de pasaxeiro de asento libre.")
            print("0. Saír")
            opcion = int(input("\t[?] Opcion > "))

            if opcion == 0:
                exit()

            elif opcion == 1:
                numero = int(input("\t[?] Numero de asentos a crear > "))
                numasentos = len(asentos)
                for num in range(0,numero):
                   if num != 13:
                        asento = Asento(str(num + numasentos), "turista")
                        asentos.append(asento)

            elif opcion == 2:
                clase = input("\t[?] Clase > ")
                for asento in asentos:
                    if asento.clase == clase:
                        if asento.pasaxeiro == "None":
                            print(f"Asento libre: {asento.numero}")
                            break

            elif opcion == 3:
                numasento = input("\t[?] Número do asento a ocupar > ")
                for asento in asentos:
                    if str(asento.numero) == numasento:
                        asento.ocupar(input("\t[?] Pasaxeiro > "))

        case 3:
            asentos_str = []
            for asento in asentos:
                if asento.ocupado == False:
                    asentos_str.append(f"Asento: {asento.numero} {asento.clase} libre")
                else:
                    asentos_str.append(f"Asento: {asento.numero} {asento.clase} {str(asento.pasaxeiro)}|{str(asento.ocupado)}")
