''' 2. Escribir un programa que pregunte o usuario os números gañadores da lotería primitiva, os almacene nunha lista e os muestre por
pantalla ordenados de menor a maior.'''

print("Pon os números gañadores da lotería primitiva: ")
ganadores = []

for numero in range(1, 7):
    ganadores.append(int(input(f"[?] Número {numero}: ")))

print("\nNúmeros gañadores ordenados: ")
ganadores.sort()
for numero in ganadores:
    print(str(numero))
