'''9. Escribir unha función empaquetar para unha lista, onde empaquetar significa indicar a repetición de valores consecutivos mediante
unha tupla (valor, cantidade de repeticións). Por exemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devoltar
[(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].
'''

def empaquetar(lista):
    listeo = lista
    empaquetado = []
    for n in lista:
        empaquetado.append((n, listeo.count(n)))
        for i in lista:
            if i == n:
                listeo.remove(i)
                
    return empaquetado

print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]))