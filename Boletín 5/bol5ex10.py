''' 10. Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado.
Asegúrate que estes valores sexan positivos, para eso valida os datos.
'''

base = int(input("Ingresa a base: "))
altura = int(input("Ingresa a altura: "))

def area(base, altura):
    area = base * altura
    return area

print(area(base, altura))

