'''1. Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordeados de menor a maior ou non.'''

tupla = (tuple(input('Elementos de tupla separados por ",": ').split(",")))

iguales = 0
transtupla = []

for elemento in tupla:
    transtupla.append(elemento)

transtupla = transtupla.sort()

for elemento, elemento2 in transtupla, tupla:
    if elemento == elemento2:
        iguales += 1

if iguales == len(tupla):
    print("A tupla está ordeada.")
else:
    print("A tupla non está ordeada.")