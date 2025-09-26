"""14. Codificar o programa que solicite 10 números por consola e calcule a súa suma.
Si o usuario introduce en calquera momento o número 999, deixa de solicitar máis números e presenta o valor da súma acadada ata ese momento."""

i = 0
n = int(input("Número: "))
suma = [n]
while i != 9:
     n = int(input("Número: "))
     suma.append(n)
     i += 1
     if n == 999:
         break

print(sum(suma))