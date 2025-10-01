''' 3. Escribir un programa que almacene nunha lista os números do 1 o 10 e os mostre por pantalla en orden inverso separados por comas.'''

lista = []
for i in range(1, 11):
    lista.append(i)

for i in range(9, -1, -1):
    print(lista[i], end=',')
