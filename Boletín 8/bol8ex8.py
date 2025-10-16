'''8. Escribir unha función que reciba unha lista de tuplas (Apelido, Nome, Inicial_segundo_nome) e devolte unha
lista de cadenas onde cada unha conteña primero o nome, logo a inicial cun punto, e logo o apelido.'''

listatuplas = [
    ("Pérez", "Ignacio", "F"),
    ("Peláez", "María", "G") ]

def ordenar(lista):
    listaorden = []
    for tuplanum in range(0, len(lista)):
        cadea = lista[tuplanum][1] + " " + lista[tuplanum][2] + ". " + lista[tuplanum][0]
        listaorden.append(cadea)
    return listaorden

print(ordenar(listatuplas))