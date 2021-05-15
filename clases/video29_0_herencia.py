

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo}" \
               f"\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenado: {self.frena}"

