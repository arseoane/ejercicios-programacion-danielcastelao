import math


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

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto: X: {self.x}, Y: {self.y}"

    def distancia_al_origen(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        if radio < 0:
            raise ValueError("El radio no puede ser negativo")
        self.radio = radio

    def __str__(self):
        return f"Circulo: Radio: {self.radio}, X: {self.x}, Y: {self.y}"

    def calcularArea(self):
        return math.pi * self.radio * self.radio

    def calcularVolume(self):
        return 0.0


class Cilindro(Circulo):
    def __init__(self, x, y, radio, altura):
        super().__init__(x, y, radio)
        if altura < 0:
            raise ValueError("La altura no puede ser negativa")
        self.altura = altura

    def __str__(self):
        return f"Cilindro: Radio: {self.radio}, Altura: {self.altura}, X: {self.x}, Y: {self.y}"

    def calcularArea(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

    def calcularVolume(self):
        return math.pi * self.radio * self.radio * self.altura

punto = Punto(1, 2)
circulo = Circulo(1, 2, 2)
cilindro = Cilindro(1, 2, 2, 2)

print(punto)
print(circulo)
print(cilindro)