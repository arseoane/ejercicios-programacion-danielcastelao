n = int(input("Cantidade de números triangulares: "))
for i in range(1, n+1):
        t = i * (i + 1) // 2
        print(f"{i} - {t}")

