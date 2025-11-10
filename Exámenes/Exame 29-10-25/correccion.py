def almacenarTemperaturas():
    temperaturas = []
    dias = ["luns","martes","mércores","xoves","venres","sábado","domingo"]
    for dia in dias:
        temperatura = float(input(f"Introduce a temperatura media diaria do día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas
