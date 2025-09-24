''' 6. Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o
factorial e imprima o resultado xunto co número de orden correspondiente.
'''

m = int(input("Cantidade de valores a ingresar: "))

def factorial(n):
    for mult in range(n-1, 0, -1):
        n *= mult
    return n

for i in range(m+1):
    v = int(input(f"Valor {i}: "))
    print(f"Factorial: {factorial(v)}")