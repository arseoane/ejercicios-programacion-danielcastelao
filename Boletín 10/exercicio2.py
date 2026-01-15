class FormatoDataError(Exception):
    pass

class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)

    def getDia(self):
        return self._dia

    def setDia(self, dia):
        max_dias = self._dias_no_mes(self._mes, self._ano)
        [cite_start]if not (1 <= dia <= max_dias): [cite: 31]
            [cite_start]raise FormatoDataError(f"Día non válido para o mes {self._mes}") [cite: 29]
        self._dia = dia

    def getMes(self):
        return self._mes

    def setMes(self, mes):
        [cite_start]if not (1 <= mes <= 12): [cite: 33]
            [cite_start]raise FormatoDataError("O mes debe estar entre 1 e 12") [cite: 29]
        self._mes = mes

    def getAno(self):
        return self._ano

    def setAno(self, ano):
        [cite_start]if not (1970 <= ano <= 2999): [cite: 34]
            [cite_start]raise FormatoDataError("O ano debe estar entre 1970 e 2999") [cite: 29]
        self._ano = ano

    def _eBisiesto(self):
        [cite_start]return (self._ano % 4 == 0 and self._ano % 100 != 0) or (self._ano % 400 == 0) [cite: 32, 51]

    def _dias_no_mes(self, m, a):
        if m in [4, 6, 9, 11]:
            return 30
        if m == 2:
            [cite_start]return 29 if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0) else 28 [cite: 31, 32]
        return 31

    def incrementarDia(self):
        max_d = self._dias_no_mes(self._mes, self._ano)
        if self._dia < max_d:
            self._dia += 1
        else:
            self._dia = 1
            self.incrementarMes()

    def incrementarMes(self):
        if self._mes < 12:
            self._mes += 1
        else:
            self._mes = 1
            self.incrementarAno()

    def incrementarAno(self):
        self.setAno(self._ano + 1)

    def dataIgual(self, outraData):
        return self._dia == outraData.getDia() and \
               self._mes == outraData.getMes() and \
               self._ano == outraData.getAno()

    def mostrarData(self):
        [cite_start]print(f"{self._dia:02d}/{self._mes:02d}/{self._ano}") [cite: 50]
