# 7. Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

print("Fichas do dominó: ")
for d1 in range(0, 7):
    for d2 in range(0, d1+1):
            print([d1, d2])
