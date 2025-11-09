def eliminar_acentos(cadena):
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U")
    )
    for a, b in reemplazos:
        cadena = cadena.replace(a, b)
    return cadena

print(eliminar_acentos("Antón foi de viaxe a Ávila."))