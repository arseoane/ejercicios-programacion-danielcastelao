# Crea unha axenda de contactos onde cada contacto teña varios teléfonos e un correo. A axenda ten que estar gardada nun ficheiro en formato json.
# O programa debe permitir engadir novos contactos a unha lista de dicionarios.
# Ao saír, debe gardar toda a lista en axenda.json.
# Ao volver abrir o programa, debe cargar os datos existentes para non perdelos

import json

class Contacto:
    def __init__(self, nome, telefonos, email):
        self.nome = nome
        if type(telefonos) == list:
            self.telefonos = telefonos
        self.email = email

    def __str__(self):
        return f"{self.nome};{self.telefonos};{self.email}"

while True:
    try:
        print("1. Engadir contacto.")
        print("2. Listar contactos.")
        print("0. Saír.")

        opcion = int(input("\nOpción: "))
        if opcion == 0:
            break

        elif opcion == 1:
            nome = input("Nome: ")
            telefonos = []
            while True:
                telefono = input("Teléfono (escribe 'cancel' para cancelar): ")
                if telefono != "cancel":
                    telefonos.append(telefono)
                else:
                    break
            email = input("Email: ")
            contacto = str(Contacto(nome, telefonos, email))
            with open("axenda.json","a") as contactos:
                datoconjunto = contacto.split(';')
                datosdict = {'nome': datoconjunto[0], 'telefonos': datoconjunto[1], 'email': datoconjunto[2]}
                json.dump(datosdict, contactos)

        elif opcion == 2:
            with open("axenda.json","r") as contactos:
                print(json.load(contactos))

        else:
            print("Opción inválida.")

    except FileNotFoundError:
        print("Ficheiro 'axenda.json' non atopado.")

    except Exception as error:
        print("Error: " + error)