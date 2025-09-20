dni = int(input("Introduce DNI sen letra: "))

tabla = [
    "T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"
    ]

numletra = dni % 23

letra = tabla[numletra]

print(f"O DNI completo é: {dni}{letra}")