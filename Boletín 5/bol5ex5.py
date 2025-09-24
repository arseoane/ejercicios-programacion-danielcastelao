""" 5. Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice. 
Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n. 
É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
"""

n = int(input("Cantidade de números triangulares: "))
for i in range(1, n+1):
        t = i * (i + 1) // 2
        print(f"{i} - {t}")

