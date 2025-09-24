# 8. Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.

n = int(input("Número máximo da ficha: "))
print("Imprimindo fichas: ")
for f in range(0, n+1):
    print(f"[{f}]")
