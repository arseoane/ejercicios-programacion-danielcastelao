class FormatoDataError(Exception):
    """Excepción para datas fóra de rango ou parámetros incorrectos."""
    pass


class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        # A orde é importante para validar o día segundo o mes e o ano
        self.set_ano(ano)
        self.set_mes(mes)
        self.set_dia(dia)

    def _e_bisiesto(self) -> bool:
        """Verifica se o ano actual é bisesto"""
        return (self._ano % 4 == 0 and self._ano % 100 != 0) or (self._ano % 400 == 0)

    def set_ano(self, ano: int):
        # O número de ano entre 1970 e 2999
        if 1970 <= ano <= 2999:
            self._ano = ano
        else:
            raise FormatoDataError("O ano debe estar entre 1970 e 2999")

    def set_mes(self, mes: int):
        # O número do mes entre 1 e 12
        if 1 <= mes <= 12:
            self._mes = mes
        else:
            raise FormatoDataError("O mes debe estar entre 1 e 12")

    def set_dia(self, dia: int):
        # O número de día depende do mes e se é bisesto
        dias_por_mes = {
            1: 31, 2: 29 if self._e_bisiesto() else 28,
            3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }

        if 1 <= dia <= dias_por_mes.get(self._mes, 31):
            self._dia = dia
        else:
            raise FormatoDataError(f"Día {dia} non válido para o mes {self._mes}.")

    def mostrar_data(self):
        """Amosa a data por consola."""
        print(f"{self._dia:02d}/{self._mes:02d}/{self._ano}")

    def data_igual(self, outra_data: 'Data') -> bool:
        """Compara se dúas datas son iguais."""
        return (self._dia == outra_data._dia and
                self._mes == outra_data._mes and
                self._ano == outra_data._ano)