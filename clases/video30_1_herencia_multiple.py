from clases.video29_0_herencia import Vehiculos
from clases.video30_0_herencia_multiple import Electrico


# HERENCIA MULTIPLE DE DOS CLASES
class Camioneta(Vehiculos, Electrico):
    pass # No se pone nada dentro por ahora


Suburban = Camioneta("Suburban", "SED547")  # Solo obtenemos el init de la primera clase puesta en la herencia

print(Suburban)  # Imprimimos los datos dentro de la primera clase puesta en la hrencia de ellas
