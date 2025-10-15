'''4. Escribir unha función que reciba unha tupla con nomes, unha posición de orixen p e unha cantidade n, e imprima a mensaxe anterior
(exercicio 3) para os n nombres que se encontran a partires da posición p.'''

tupla = ("Antón","José","María","Carla")

def saudar(tupla, p, n):
    for i in range(p, n+1):
        print(tupla[i])

saudar(tupla, 1, 2)