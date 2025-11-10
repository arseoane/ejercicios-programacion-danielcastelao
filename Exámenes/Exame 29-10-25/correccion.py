def almacenarTemperaturas():
    temperaturas = []
    dias = ["luns","martes","mércores","xoves","venres","sábado","domingo"]
    for dia in dias:
        temperatura = float(input(f"Introduce a temperatura media diaria do día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcularMediaTemperaturas(temperaturas):
    totalTemperatura = 0
    for temperatura in temperaturas:
        totalTemperatura += temperatura
    return totalTemperatura/len(temperaturas)

def diasSuperanMediaTemperatura(temperaturas):
    dias = 0
    mediaTemperatura = calcularMediaTemperaturas(temperaturas)
    for temperatura in temperaturas:
        if temperatura > mediaTemperatura:
            dias += 1
    return dias

def mostraDiasSuperanTemperatura(temperaturas,temperaturaLimite):
    dias = ["luns","martes","mércores","xoves","venres","sábado","domingo"]
    for i, temperatura in enumerate(temperaturas):
        if temperatura > temperaturaLimite:
            print("0 dia"+ dias[i] + "superou o valor " + temperaturaLimite + " en " + temperatura + " graos.")

temperaturas = almacenarTemperaturas()
media = calcularMediaTemperaturas(temperaturas)
print("A media é " + media + ".")
numeroDias = diasSuperanMediaTemperatura(temperaturas)
print(str(numeroDias) + " dias que superan media de temperaturas. ")
print("Días que a temperatura supera a media: ")
mostraDiasSuperanTemperatura(temperaturas,media)