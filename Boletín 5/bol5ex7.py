# 7. Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

print("Fichas do dominó: ")
for l1 in range(1, 7):
    for l2 in range(1, 7):
        print(f"[{l1} | {l2}]")
