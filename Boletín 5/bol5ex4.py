# 4. Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.

principio = int(input("Número inicial: "))
final = int(input("Número final: "))

for i in range(principio, final + 1, 2):
    print(i)
