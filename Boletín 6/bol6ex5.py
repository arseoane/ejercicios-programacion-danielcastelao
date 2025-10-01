''' 5. Escribir un programa que almacene o abecedario nunha lista, e cree outra lista a partir dela, onde non aparezan as letras que ocupen posicións múltiplos de 3, 
e mostre por pantalla a lista resultante.
'''

abecedario = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

for valor in range(0, len(abecedario), 3):
    if abecedario.count(valor) % 3 == 0:
        abecedario.remove(valor)

for letter in abecedario:
    print(letter)
