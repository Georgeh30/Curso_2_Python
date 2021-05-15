# SINTAXIS DE LA EXCEPCION RAISE PARA CREAR NUESTRAS PROPIAS EXCEPCIONES PARA LAS CLASES, HERENCIAS, ETC...


def evaluarEdad(edad):

    if edad < 0:
        raise TypeError("No se permite edades negativas")  # Para lanzar una excepcion propia

    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."


try:
    print(evaluarEdad((-70)))
except TypeError as mensaje:  # Obtenemos el mesaje de esta excepcion propia
    print(mensaje)  # Y la imprimimos en caso de que sea menor a 0 el valor ingresado
