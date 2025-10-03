''' 6. Divide a cadea de texto “ www. phytonparatodos. com” en duas partes “ www. phyton”
e “paratodos. com”. Para posteriormente concaténalas e mostralas de novo.'''

cadea = " www. pythonparatodos .com"

parte1 = cadea[0:cadea.index("n")+1]
parte2 = cadea[cadea.index("n")+1:]

print("Parte1: ", parte1)
print("Parte2: ", parte2)

print("Cadea orixinal: ", cadea)