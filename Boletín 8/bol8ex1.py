'''1. Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordeados de menor a maior ou non.'''

lista = input('Elementos de tupla separados por ",": ').split(",")

tupla = (tuple(lista))

iguales = 0
transtupla = []

for elemento in tupla:
    transtupla.append(elemento)

transtupla = transtupla.sort()

for elemento, elemento2 in zip(lista, tupla):
    if elemento == elemento2:
        iguales += 1

if iguales == len(lista):
    print("A tupla está ordeada.")
else:
    print("A tupla non está ordeada.")