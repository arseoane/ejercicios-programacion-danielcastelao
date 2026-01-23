#Verificar data formato dd/mm/aaaa - booleano
#lonxitude total: dd, mm, aaaa
#dd mm aaaa caracteres numéricos
#verificar dia/mes - booleano
# / nas posicións correctas
#evitar espazos inicio-fin

class ValoresIncompletos(Exception):
    def __init__(self, mensaje):
        super().__init__()
        self.__mensaje = mensaje

    def __str__(self):
        return f"Error: {self.__mensaje}"

class DateMatch:
    def __init__(self, day, month=None, year=None):
        match day:
            case int():
                if month is not None and year is not None:
                    self.setDay(day)
                    self.setMonth(month)
                    self.setYear(year)
                else:
                    raise ValoresIncompletos("En el caso del primer valor ser int se debe especificar los otros 3")
            case str():
                separados = self.__separarStr(day)
                self.setDay(separados[0])
                self.setMonth(separados[1])
                self.setYear(separados[2])

            case list() | tuple():
                if len(day) == 3:
                    self.setDay(day[0])
                    self.setMonth(day[1])
                    self.setYear(day[2])
                else:
                    raise ValueError("Formato incorrecto dd/mm/yyyy")

            case _:
                raise TypeError("Error de tipo")

    def __separarStr(self, day):
        if day.count("/") != 2 or day.count("-") != 2:
            raise ValueError("La cadena debe contener 2 separadores ('/' o '-')")
        else:
            if day.count("-") == 2:
                tipoSeparador = "-"
            else:
                tipoSeparador = "/"

            values = day.split(tipoSeparador)

            if len(values) != 3:
                raise ValueError("Debe contener 3 campos dd/mm/aaaa")
            else:
                return values
                '''
                    if len(values[0]) != 2 and len(values[1]) != 2 and len(values[2]) != 4:
                        raise ValueError("Formato incorrecto: dd/mm/yyyyy")
                    else:
                        if values[0].isdigit() and values[1].isdigit() and values[2].isdigit():
                            self.__d = values[0]
                            self.__m = values[1]
                            self.__y = values[2]
                '''
    def setDay(self,day):
        match day:
            case int():
                if day < 1 or day > 31:
                    raise ValueError("Día inexistente")
                else:
                    if self.__month in [4, 6, 9, 11]:
                        if day > 30:
                            raise ValueError("Número de día inexistente no mes")
                        else:
                            self.__day = int(day)
                    elif self.__month in [1, 3, 5, 7, 8, 10, 12]:
                        self.__day = int(day)


def bisiesto(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

valida = False
dias31 = 1, 3, 5, 7, 8, 10, 12
dias30 = 4, 6, 9, 11

data = input("[?] Pon unha data de formato dd/mm/aaaa (ex: 02/01/1998): ")

if len(data) == 10:
    if "/" in data[2] and "/" in data[5]:
        dividir = data.split("/")
        if dividir[0].isdigit() and dividir[1].isdigit() and dividir[2].isdigit():
            dia = int(dividir[0])
            mes = int(dividir[1])
            ano = int(dividir[2])
            if mes > 12:
                print("[!] Mes inválido!")
            else:
                if mes == 2:
                    if bisiesto(ano) == True and dia <= 29:
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
            print("[!] Caracteres inválidos!")

    else:
        print("[!] Formato inválido!")
else:
    print("[!] Lonxitude inválida!")

