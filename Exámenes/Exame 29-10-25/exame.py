# 29-10-25

temps_medias = []
dias = ['Luns', 'Martes', 'Mércores', 'Xoves', 'Venres', 'Sábado','Domingo']

for dia in dias:
    temperatura_media = int(input(f"    [?] Introduce a temperatura media do {dia}: "))
    temps_medias.append(temperatura_media)

def media_temps(temperaturas):
    media = 0
    for temp in temperaturas:
        media += temp
    media /= 7
    return media

def superior_media(temperaturas):
    media = sum(temperaturas) / len(temperaturas)
    superiores = 0
    for temp in temperaturas:
        if temp > media:
            superiores += 1
    return superiores

def superior_valor(temperaturas):
    parametro = int(input(f"\n    [?] Inserta o valor do parámetro: "))
    print(f"\n    [-] Días con temperaturas superiores a {parametro}: ")
    for indice in range(0,len(temperaturas)):
        if temperaturas[indice] > parametro:
            print(f"        [+] {dias[indice]}: {temperaturas[indice]}")


print(f"\n    [+] Media de temperaturas da semana: {media_temps(temps_medias)}.")
print(f"    [+] Temperaturas superiores á media: {superior_media(temps_medias)}.")
superior_valor(temps_medias)