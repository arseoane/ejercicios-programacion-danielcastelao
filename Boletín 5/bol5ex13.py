''' 13. Solicita o usuario un número n e debuxa un triángulo de base e altura n. Si o usuario teclea o
número 4 o triángulo sería da seguinte forma:
   *
  * *
 * * *
* * * *
'''


n = int(input("Ingresa a base: "))
limit = n
asterisco = "* "
espacio = " " * limit

for i in range(0, limit):
    print(espacio + asterisco)
    asterisco += "* "
    espacio = espacio[:-1]
