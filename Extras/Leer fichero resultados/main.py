with open("fichero.txt","r") as fichero:
    contenido = fichero.read()
    i = 0
    for linea in contenido.split("\n"):
        print(f"Línea {i+1}: {linea}")
        i += 1

def importacion_resultado(self, filePath):
    try:
        with open(filePath,"r") as f:
            for i in f.readlines():
                self.__xogadores.append(i)
    except FileNotFoundError as e:
        print(f"File not found, errror: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

