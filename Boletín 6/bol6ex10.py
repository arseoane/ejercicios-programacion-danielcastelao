''' 10. Escribir un programa que almacene as matrices

a =	 (1,2,3)  				b = 	(-1,0)
   	 	(4,5,6)					(0,1)
								(1,1)
nunha lista e mostre por pantalla o seu produto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila nunha tupla.'''

a = [(1,2,3),(4,5,6)]
b = [(-1,0),(0,1),(1,1)]

filas_a = len(a)
cols_a = len(a[0])
filas_b = len(b)
cols_b = len(b[0])

if cols_a != filas_b:
    print("Non se poden multiplicar.")
else:
    resultado = [[0 for _ in range(cols_b)] for _ in range(filas_a)]

    for i in range(filas_a):
        for j in range(cols_b):
            for k in range(cols_a):
                resultado[i][j] += a[i][k] * b[k][j]

    print("Produto: ")
    for fila in resultado:
        print(fila)
