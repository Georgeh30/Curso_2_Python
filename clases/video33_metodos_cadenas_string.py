# ALGUNOS POCOS METODOS PARA TIPO DE CADENAS (STRING)

cadena_de_texto = input("Introducir una cadena de texto: ")

print("Cambio de minuscula a MAYUSCULA: {0}".format(cadena_de_texto.upper()))
print("Cambio de MAYUSCULA a minuscula: {0}".format(cadena_de_texto.lower()))
print("Cambia la 1° letra de la 1° palabra a MAYUSCULA: {0}".format(cadena_de_texto.capitalize()))

cadena_de_texto2 = input("Introducir su Edad: ")

print("Validacion TRUE = edad o FALSE = no es una edad --> {0}".format(cadena_de_texto2.isdigit()))

while not cadena_de_texto2.isdigit():
    print("Por Favor, Introduzca un valor Numerico")
    cadena_de_texto2 = input("Introducir su Edad: ")

if int(cadena_de_texto2) < 18:
    print("No es mayor de edad")
else:
    print("Es mayor de edad")


