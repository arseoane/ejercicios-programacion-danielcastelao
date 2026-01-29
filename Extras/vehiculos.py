class Vehiculo(object):
    def __init__(self, matricula, velocidadeMaxima,autonomia):
        self.matricula = matricula
        self.velocidadeMaxima = velocidadeMaxima
        self.autonomia = autonomia

    @property
    def matricula(self):
        return self.matricula

    @matricula.setter
    def matricula(self,matricula):
        self._matricula = matricula

    @property
    def velocidadeMaxima(self):
        return self.velocidadeMaxima

    @velocidadeMaxima.setter
    def velocidadeMaxima(self,velocidadeMaxima):
        self._velocidadeMaxima = velocidadeMaxima

    @property
    def autonomia(self):
        return self.autonomia

    @autonomia.setter
    def autonomia(self,autonomia):
        self._autonomia = autonomia

    def arrincar(self):
        print("Arrincamos")

    def deter(self):
        print("Nos detemos")

    def mostrarDatos(self):
        return f"{self.matricula}, {self.velocidadeMaxima}, {self.autonomia}"