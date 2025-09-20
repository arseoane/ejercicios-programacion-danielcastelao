import math

while True:
    print('''Selecciona unha opción:

        [1] Cadrado.
        [2] Triángulo.
        [3] Círculo.''')

    o = int(input("\n [+] Opción: "))
    if o == 1:
        lado = int(input("\n [+] Lado: "))
        area = lado * lado
        print("\n [+] Área do cadrado: " + str(area))
    elif o == 2:
        base = int(input("\n [+] Base: "))
        altura = int(input("\n [+] Altura: "))
        area = base * altura / 2
        print("\n [+] Área do triángulo: " + str(area))
    elif o == 3:
        radio = int(input("\n [+] Radio: "))
        area = math.pi * radio ** 2
        print("\n [+] Área do círculo: " + str(area))
    else:
        print("\n [x] Opción incorrecta!")
