class Vehiculo(object):
    def __init__(self, matricula, velocidadeMaxima,autonomia):
        self.matricula = matricula
        self.velocidadeMaxima = velocidadeMaxima
        self.autonomia = autonomia

    def arrincar(self):
        print("Arrincamos")

    def deter(self):
        print("Nos detemos")

    def mostrarDatos(self):
        return f"{self.matricula}, {self.velocidadeMaxima}, {self.autonomia}"