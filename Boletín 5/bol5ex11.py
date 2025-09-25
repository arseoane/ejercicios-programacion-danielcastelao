''' 11. Codifica un programa que solicite un número e visualice a táboa de multiplicar dese número.
O programa seguirá pedindo números ata que o usuario pulse o número cero.'''

n = int(input("Ingresa un número: "))

while n != 0:
    for multi in range(0, 11):
        print(f"{n} x {multi} = {n * multi}")
    n = int(input("Ingresa un número: "))

print("Apagando programa...")