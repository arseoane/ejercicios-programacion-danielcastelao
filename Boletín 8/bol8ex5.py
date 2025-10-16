'''Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo, deberán recibir unha tupla de tuplas,
contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.'''

tupla = (("Antón", "m"), ("José", "m"), ("María", "f"), ("Carla", "f"))

def saudar(tupla, p, n):
    for i in range(p, n+1):
        nome, xenero = tupla[i]
        if xenero == "m":
            print(f"Boas, don {nome}")
        elif xenero == "f":
            print(f"Boas, dona {nome}")

saudar(tupla, 1, 2)
