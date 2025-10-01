''' (Incompleto) 10. Escribir un programa que almacene as matrices

a =	 (1,2,3)  				b = 	(-1,0)
   	 	(4,5,6)					(0,1)
								(1,1)
nunha lista e mostre por pantalla o seu produto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila nunha tupla.'''

a = [(1,2,3),(4,5,6)]
b = [(-1,0),(0,1),(1,1)]
multi = 1

for numa in a:
    for numb in b:
        multi *= numa * numb

print(f"Produto: {multi}")
