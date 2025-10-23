'''Dada unha lista onde están os importes das distintas caixas. Primer campo identificador, o resto son tuplas onde
se dice o valor de billete/moneda e o número.

Facer funcións:

-cálculo importe por caixa

-importe total

-impresion contido caixa

-impresion contido total

'''

efectivo = [[1,(50,5),(20,5),(10,3),(0.50,3)],
            [2, (0.50,1),(0.20,1)]]

def calc_impo(caixa, calc_total = False):
    if calc_total == False:
        total = 0
        efect = efectivo[caixa - 1]
        for elemento in efect:
            if type(efect[caixa]) == tuple:
                total += efect[caixa][0] * efect[caixa][1]
        return float(total)
    else:
        total = 0
        for caixas in range(0,len(efectivo)):
            efect = efectivo[caixas]
            for elemento in efect:
                if type(efect[caixa]) == tuple:
                    total += efect[caixa][0] * efect[caixa][1]
            return float(total)

def impresion(caixa,impresion_total = False):
    if impresion_total == False:
        print(efectivo[caixa-1])
    else:
        for caixas in efectivo:
            print(caixas)

print(calc_impo(2), False)
print(impresion(1,False))