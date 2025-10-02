''' 5. Escribir un programa que almacene o abecedario nunha lista, e cree outra lista a partir dela, onde non aparezan as letras que ocupen posicións múltiplos de 3, 
e mostre por pantalla a lista resultante.
'''

abecedario = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

nova_lista = [letra for i, letra in enumerate(abecedario, 1) if i % 3 != 0]

print("Lista sen as letras en posicións múltiplos de 3:")
for letra in nova_lista:
    print(letra)


