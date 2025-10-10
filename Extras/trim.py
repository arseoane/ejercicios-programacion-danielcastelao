#quitar espacios ao final e ao principio de cadea

cadea = " unha cadea calquera "

print(cadea)
if cadea[0].isspace():
    cadea = cadea.removeprefix(' ')

if cadea[-1].isspace():
    cadea = cadea.removesuffix(' ')

print(cadea)