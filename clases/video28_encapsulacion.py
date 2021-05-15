# EJEMPLO DE ENCAPSULACION DE VARIABLE Y DE METODOS
# 1. EN LA VARIABLE --> SIRVE PARA QUE NO SE PUEDA SER CAMBIADO O PARA DAR MANEJAR SOLO UNA MANERA DE CAMBIARLA
# 2. EN EL METODO --> SIRVE PARA SOLO PODER LLAMARLO EN ESTA CLASE


class Cliente():

    def __init__(self):

        # VARIABLES ENCAPSULADAS CON SOLO PONER __ ANTES DEL NOMBRE DE LA VARIABLE
        self.puertas = "cerradas"
        self.aceite = "mal"
        self.gasolina = "ok"
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    # Metodo que sirve para editar el dato dentro de la variable encapsulada (__enmarcha)
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            chequeo = self.__chequeo()

        if self.__enmarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enmarcha and chequeo == False:
            return "Algo ha ido mal en el chequeo, no se puede arrancar!!"
        else:
            return "El coche esta parado"

    # Metodo encapsulado usando dos __ antes del nombre que le asignemos para que solo sea usado dentro de la clase
    def __chequeo(self):
        print("realizando chequeo interno")

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

    def __str__(self):
        return f"El coche tiene {str(self.__ruedas)} ruedas, un ancho de {str(self.__anchoChasis)} y un largo de {str(self.__largoChasis)}"


Ferrari = Cliente()

print(Ferrari.arrancar(True))  # CAMBIAMOS EL VALOR DE LA VARIABLE ENCAPSULADA E IMPRIMIMOS EL MENSAJE CORRESPONDIENTE

print(Ferrari)  # IMPRIMIMOS LOS DATOS DEL OBJETO CON EL METODO STR CON SOLO EL NOMBRE DEL OBJETO (Ferrari)

print("Segundo Objeto********************")

Laborghini = Cliente()

print(Laborghini.arrancar(False))  # CAMBIAMOS EL VALOR DE LA VARIABLE ENCAPSULADA E IMPRIMIMOS EL MENSAJE CORRESPONDIENTE

print(Laborghini)  # IMPRIMIMOS LOS DATOS DEL OBJETO CON EL METODO STR CON SOLO EL NOMBRE DEL OBJETO (Ferrari)
