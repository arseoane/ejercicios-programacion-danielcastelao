''' 12. Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o
número deles que ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a porcentaxe de traballadores
que ganan menos de 1000 €. Tendo en conta que non se coñece con antelación o numero de traballadores
da empresa e non se admiten os soldos negativos (utiliza como condición de fin un soldo 0).'''

traballadores = []
soldo_normal = 0
soldo_escaso = 0

elemento = int(input("Ingresa soldo (0 para deter): "))

while elemento > 0:
    traballadores.append(elemento)
    elemento = int(input("Ingresa soldo (0 para deter): "))


for traballador in traballadores:
    if traballador > 1000 and traballador < 1750:
        soldo_normal += 1
    if traballador < 1000:
        soldo_escaso += 1

print("Soldos entre 1000 € e 1750 €: ", soldo_normal)
print("Porcentaxe de soldos menores de 1000 €: ", (soldo_escaso * 100)/len(traballadores), " %.")
