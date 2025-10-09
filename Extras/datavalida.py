#Verificar data formato dd/mm/aaaa - booleano
#lonxitude total: dd, mm, aaaa
#dd mm aaaa caracteres numéricos
#verificar dia/mes - booleano
# / nas posicións correctas
#evitar espazos inicio-fin


valida = False
dias31 = 1, 3, 5, 7, 8, 10, 12
dias30 = 4, 6, 9, 11

data = input("[?] Pon unha data de formato dd/mm/aaaa (ex: 02/01/1998): ")

if len(data) == 10:
    if "/" in data[2] and "/" in data[5]:
        dividir = data.split("/")
        dia = int(dividir[0])
        mes = int(dividir[1])
        ano = int(dividir[2])
        if mes > 12:
            print("[!] Mes inválido!")
        else:
            if mes == 2:
                if ano % 400 == 0 and dia <= 29:
                    print("[+] Data válida!")
                else:
                    print("[!] Día inválido!")
            elif mes in dias31 and dia > 31:
                print("[!] Día inválido!")
            elif mes in dias30 and dia > 30:
                print("[!] Día inválido!")
            else:
                print("[+] Data válida!")

    else:
        print("[!] Formato inválido!")
else:
    print("[!] Lonxitude inválida!")

