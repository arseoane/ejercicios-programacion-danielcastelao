''' 9. Escribir un programa que almacene os vectores (1,2,3) e (-1,0,2) en duas listas e mostre por pantalla o seu producto escalar.'''

vectores1 = [1,2,3]
vectores2 = [-1,0,2]
total = 0

for v1, v2 in zip(vectores1, vectores2):
    total += v1 * v2

print(f"Resultado: {total}")
