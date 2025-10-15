'''6. Dada unha lista de números enteiros, escribir unha función que:
● Devolte unha lista con tódolos que sexan primos.
● Devolte o sumatorio e o promedio dos valores.
● Devolte unha lista co factorial de cada un de eses números.'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    for mult in range(n-1, 0, -1):
        n *= mult
    return n

print("Primos: ", end=' ')
for n in lista:
    if es_primo(n):
        print(n, end=' ')
print()

print("Sumatorio: ", sum(lista))
print("Promedio: ", sum(lista)/len(lista))

print("Factoriais: ", end=" ")
for n in lista:
    print(factorial(n), end=" ")