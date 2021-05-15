# FUNCION ANONIMA, SIRVE PARA ABREVIAR O RESUMIR UNA FUNCION NORMAL


"""----------------------------------FUNCIONES NORMALES-----------------------------------"""


def area_triangulo1(base, altura):
    return base * altura / 2


print(area_triangulo1(5, 10))

"""-----------------------------FUNCIONES LAMBDA REDUCEN LINEAS DE CODIGO------------------------------"""

# FUNCION PARA CALCULAR EL AREA DE UN TRIANGULO
area_triangulo2 = lambda base, altura: (base * altura) / 2

print(area_triangulo2(5, 10))

# FUNCION PARA DARLE UN FORMATO A UN DATO
dar_formato = lambda numero: "${}.00 °°".format(numero)

el_numero = 1558

print(dar_formato(el_numero))
