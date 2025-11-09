'''11. Pregado de un texto. Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas de como máximo esa
lonxitude. As líñas deben cortarse correctamente nos espazos (sen cortar as palabras).
'''


def listacar(texto, lon):
    lista = []
    i = 0
    for car in texto:
        lista.append(car)
        i += 1
        if i >= lon:
            break
    return lista


print(listacar("Hola buenas señores", 10))
