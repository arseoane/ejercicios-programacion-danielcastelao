'''3. Escribir unha función que reciba unha tupla con nomes e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’'''

lista = input('Nomes para tupla separados por ",": ').split(",")

tupla = (tuple(lista))

def saudar(t):
    for nombre in t:
        print(f"Estimad@ don/dona {nombre}.")

saudar(tupla)