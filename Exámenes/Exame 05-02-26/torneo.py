from equipo import *
from equipoNonExisteError import *


class Torneo:
    def __init__(self, nome, equipos, num_max_equipos, num_equipos):
        self.__nome = nome
        self.__equipos = equipos
        self.__num_max_equipos = num_max_equipos
        self._equipos = []

        if num_equipos > self.__num_max_equipos:
            raise ValueError("O número de equipos non pode superar o máximo.")
        else:
            self.__num_equipos = num_equipos

        self._equipos.append(self.__equipos)

    def __str__(self):
        return str(self.__nome, self.__equipos, self.__num_equipos)

    def get_nome(self):
        return self.__nome

    def get_equipo(self,nome:str):
        for equipo in self._equipos:
            if equipo.get_nome() == nome:
                return f"Equipo | {equipo.get_nome()}"


    def add_equipo(self,equipo:Equipo):
        self._equipos.append(equipo)
        return self._equipos.index(equipo)

    def get_equipos(self):
        return self._equipos

    def rexistrar_encontro(self, encontro_resultado:str):
        return "En desarrollo"

    def get_clasificacion(self):
        clasificacion = []

        for equipo in self._equipos:
            clasificacion.append(str(equipo))

        clasificacion = clasificacion.sort()

        return clasificacion

    def numero_equipos(self):
        return len(self._equipos)
