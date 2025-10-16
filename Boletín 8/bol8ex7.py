'''Dada unha lista de números enteiros e un enteiro k, escribir unha función que:
    * Devolte tres listas, unha cos menores, outra cos maiores e outra cos iguais a k.
    * Devolte unha lista con aqueles que son múltiplos de k.
'''
import random

def treslistas(lista, k):
    listamenores = []
    listamaiores = []
    listaiguais = []
    listamultiplos = []
    for n in lista:
        if n > k:
            listamaiores.append(n)
        elif n < k:
            listamenores.append(n)
        else:
            listaiguais.append(n)

    for n in lista:
        if k % n == 0:
            listamultiplos.append(n)

    return listamenores, listamaiores, listamultiplos, listaiguais

lista = []
for n in lista:
    lista.append(random.randint(0, 100))

print(treslistas(lista, 50))

