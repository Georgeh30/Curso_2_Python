

class Electrico:
    def __init__(self, asientos, movimiento):
        self.asientos = asientos
        self.movimiento = movimiento
        self.cilindros = 8

    def __str__(self):
        return f"Asientos: {self.asientos}\nMovimiento: {self.movimiento}\nCilindros: {self.cilindros}"
