# Crea a aplicación que permita gardar e recuperar os datos dos clientes dunha empresa. Para o cal, defina a clase Cliente, que teña os atributos:
# id, identificador de cliente
# nome
# teléfono

class Cliente():
    idcount = 0
    def __init__(self, nome, telefono):
        self.id = Cliente.idcount
        self.nome = nome
        self.telefono = telefono

        Cliente.idcount += 1

    def __str__(self):
        return f"{self.id},{self.nome},{self.telefono}\n"

print('''
1. Gardar cliente.

2. Listar clientes.
''')

opcion = input("Ingrese una opción: ")

if opcion == "1":
    cliente = Cliente(input("Nome: "),input("Teléfono: "))
    with open("clientes.txt","a") as f:
        f.write(str(cliente))

elif opcion == "2":
    with open("clientes.txt","r") as f:
        print(f.readlines())