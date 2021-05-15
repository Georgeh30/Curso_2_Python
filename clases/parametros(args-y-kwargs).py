# PARAMETROS INDEFINIDOS


# 1. EL PARAMETRO *args SIRVE PARA QUE AL MOMENTO DE LLAMAR LA FUNCION PODAMOS
# AGREGAR UN NUMERO INDETERMINADO DE PARAMETROS SIMPLES

# 2. EL PARAMETRO **kwargs SIRVE PARA QUE AL MOMENTO DE LLAMAR LA FUNCION PODAMOS
# AGREGAR UN NUMERO INDETERMINADO DE PARAMETROS DE "CLAVE-VALOR" O UN GRUPO DE ESTE
# TIPO DE DATOS "CLAVE-VALOR" USANDO LE TIPO DE DATO "DICCIONARIO"


# EJEMPLO:
def ejemplo_args(*args, **kwargs):
    lista = args
    diccionario = kwargs
    print(diccionario)
    return lista


datos = ejemplo_args("hola", "soy", valor="jorge")

for valor in datos:
    print(valor)
