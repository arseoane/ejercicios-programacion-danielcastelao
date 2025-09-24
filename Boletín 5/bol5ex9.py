# 9. Calcula a cantidade de números negativos, positivos e ceros que hai nun grupo de 10 números enteiros.

enteiros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
positivos = 0
negativos = 0
ceros = 0

for i in range(0, len(enteiros)):
    enteiros[i] = int(input(f"Valor de slot {i}: "))

for i in range(0, len(enteiros)):
    if enteiros[i] > 0:
        positivos += 1
    elif enteiros[i] < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")