class Equipo(object):
    def __init__(self, nome):
        self.__nome = nome
        self.__ganhados = 0
        self.__perdidos = 0
        self.__empates = 0

    def get_nome(self):
        return self.__nome

    def get_ganhados(self):
        return self.__ganhados

    def get_perdidos(self):
        return self.__perdidos

    def get_empates(self):
        return self.__empates

    def add_victoria(self):
        self.__ganhados += 1

    def add_perdido(self):
        self.__perdidos += 1

    def add_empate(self):
        self.__empates += 1

    def get_puntos(self):
        return (self.__ganhados * 3) + self.__empates

    def get_encontros_xogados(self):
        return self.__ganhados + self.__empates + self.__perdidos

    def __str__(self):
        return f"{self.__nome} - V:{self.__ganhados} E:{self.__empates} D:{self.__perdidos} (Puntos: {self.get_puntos()})"

