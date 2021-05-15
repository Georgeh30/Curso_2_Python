from clases.video29_0_herencia import Vehiculos


# HEREDAMOS DE LA CLASE VEHICULOS
class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}" \
               f"\nAcelerando: {self.acelera}\nFrenado: {self.frena}\n{self.hcaballito}"


moto1 = Moto("Honda", "CRED34")

moto1.caballito()

print(moto1)
