'''2. Escribir unha función que indique si duas fichas de dominó encaixan ou non. As fichas son recibidas en duas tuplas, por exemplo: (3,4) e
(5,4). A función devolta un booleano co resultado do encaixe.'''

def encaixan(ficha1, ficha2):
    return ficha1[0] in ficha2 or ficha1[1] in ficha2

print("[?] Introduce as dúas fichas de dominó:\n")

a1 = int(input("[?] Primeiro número da primeira ficha: "))
a2 = int(input("[?] Segundo número da primeira ficha: "))
b1 = int(input("[?] Primeiro número da segunda ficha: "))
b2 = int(input("[?] Segundo número da segunda ficha: "))

ficha1 = (a1, a2)
ficha2 = (b1, b2)

if encaixan(ficha1, ficha2):
    print(f"\n[+] As fichas {ficha1} e {ficha2} encaixan!")
else:
    print(f"\n[+] As fichas {ficha1} e {ficha2} non encaixan!")
