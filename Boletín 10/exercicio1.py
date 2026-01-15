import re

class DniNonValido(Exception):
    pass

class Persoa:
    def __init__(self, nome="", direccion="", dni=""):
        self._nome = nome
        self._direccion = direccion
        self._dni = None
        if dni:
            self.setDni(dni)

    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getDireccion(self):
        return self._direccion

    def setDni(self, dni):
        if not re.match(r"^[0-9]{8}[A-Z]$", dni):
            [cite_start]raise DniNonValido("DNI non válido") [cite: 3]
        self._dni = dni

    def getDni(self):
        return self._dni

class Deportista(Persoa):
    def __init__(self, nome="", direccion="", dni="", deporte="", clube="", licencia=""):
        super().__init__(nome, direccion, dni)
        self._deporte = deporte
        self._clube = clube
        self._licencia = None
        if licencia:
            self.setLicencia(licencia)

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getDeporte(self):
        return self._deporte

    def setClube(self, clube):
        self._clube = clube

    def getClube(self):
        return self._clube

    def setLicencia(self, licencia):
        [cite_start]patron = r"^[0-9]{4}[a-z]{3}[0-9]{6}$" [cite: 5, 6, 7]
        if not re.match(patron, licencia):
            [cite_start]raise ValueError("Formato de licencia incorrecto") [cite: 4]
        self._licencia = licencia

    def getLicencia(self):
        return self._licencia
