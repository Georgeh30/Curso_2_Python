# POLIMORFISMO --> Sirve para comunicarse con clases diferentes
#                  y dependiendo de la clase, su comportamiento sera diferente


# CLASE 1
class Coche:
    def desplazamientos(self):
        print("Me desplazo utilizando 4 ruedas")


# CLASE 2
class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")


# CLASE 3
class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


# Creacion de una Funcion fuera de todas las clases
def desplazaminetoVehiculo(vehiculo):  # en el parametro podemos meter cualquiera de las clases
    # Aun no existe este metodo desplazamiento pero mandaria a llamar
    # el metodo de la clase que insertemos en el parametro de arriba
    vehiculo.desplazamiento()


# Inicializamos la clase Camion y lo guardamos en objeto miVehiculo
miVehiculo = Camion()

# Mandamos a llamar la funcion y ponemos en el parametro el objeto anterior...
# para mandar a llamar el metodo desplaamiento haciendo uso del polimorfismo
desplazaminetoVehiculo(miVehiculo)
