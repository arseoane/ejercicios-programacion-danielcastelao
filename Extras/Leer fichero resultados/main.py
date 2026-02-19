with open("fichero.txt","r") as fichero:
    contenido = fichero.read()
    i = 0
    for linea in contenido.split("\n"):
        print(f"{i+1}. {linea}")
        i += 1