''' 10. Tenta escribir un método, que dado un obxecto da clase str conte diferentes tipos de caracteres.
En particular, o método deberá imprimir o número de letras, díxitos e espazos en branco da cadea.
Tenta facer un programa que escriba o cálculo da cadea: "Ola, son alumno de DAM1, e son programador desde o 2025".'''

def barras(string):
    for n in range(0, len(string)):
        print("-", end="-")
    print("-")


cadea = "Ola, son alumno de DAM1, e son programador desde o 2025"

barras(cadea)
print("Cadea: ", cadea)

letras = 0
numeros = 0
simbolos = 0
espazos = 0

for caracter in cadea:
    if caracter.isalpha():
        letras += 1
    elif caracter.isdigit() or caracter.isnumeric():
        numeros += 1
    elif caracter.isspace():
        espazos += 1
    else:
        simbolos += 1

barras(cadea)
print("Letras: ", letras)
print("Números: ", numeros)
print("Símbolos: ", simbolos)
print("Espazos: ", espazos)
print("---------------------")