valor = 0


def saludo(n):
    print("Hola", n)
    return n


saludo("Jorge")  # Hola Jorge


def sumar(number1, number2):
    print(number1 + number2)


sumar(10, 15)  # 25


# En esta funcion le asignamos al nuber2 el valor de 20,
# esto nos sirve para en caso de no asignarle un valor entonces seria 20 al final
def sumar(number1, number2=20):
    print(number1 + number2)


sumar(10, 15)  # si le doy un nuevo valor al number2 se sobreescribe y ya no valdria 20 si no que 15
sumar(10)  # 30
sumar(number2=15, number1=10)


def suma_lista(listas):
    resultado = 0
    for lista in listas:
        resultado += lista
    print(resultado)


suma_lista([3, 10, 20, 45])


# PRIMERA OPCION PARA DICCIONARIOS
# Aqui obtenemos un Diccionario y al poner al principio solo dos ** con esto podremos
# meter varios parametros sin tener que indicarlos todos
def sumar_diccionario(**numbers):
    print(numbers)  # Datos que imprimirá son: {'number1' : 10, 'number2' : 20}
    print(numbers['number1'] + numbers['number2'] + numbers['number3'])


# Llamamos el metodo y como se puso dos ** podemos darle varios datos al diccionario
sumar_diccionario(number1=10, number2=20, number3=20) # 30


# SEGUNDA OPCION PARA TUBLAS O LISTAS DINAMICAS
def indeterminados_posicion(*datos):
    for dato in datos:
        print(dato)


print(4, "Hola Mundo", [1, 2, 3, 4, 5])


# OPCION3 MEZCLANDO LAS DOS ANTERIORES
# Podemos meter el parametro para meter varios parametros * para una lista y tambien el prarametro **
# que funciona para el diccionario y podamos meter la cantidad de parametrps que querramos
def super_funcion(*args,**kwargs):
     total = 0
     for arg in args:
         total += arg
     print("sumatorio => ", total)
     for kwarg in kwargs:
         print(kwarg, "=>", kwargs[kwarg])


# Aqui ya solo es meter el los parametros que querramos y el mismo python detectara cual es para
# la listas o tuplas y cuales son para el diccionario a tra ves de poner ejemplo: cms="Plone" el cual
# es para los diccionarios o poner ejemplo: 1, "Hola",... el cual sirv para listas o tuplas
super_funcion(50, -1, 1.56, 10, 20, 300, cms="Plone", edad=38)


def sumar_por_return(a, b):

    return a + b


print(sumar_por_return(2, 4))


def sumar_condicion(a=None, b=None):

    if a is None or b is None:
        print("Error, no ha ingresado ningun valor a los parametros asignados")
        return # nos retornara un None

    return a + b


print(sumar_condicion())
print(sumar_condicion(2, 4))


def no_hace_nada(dato): pass  # no pasa nada


print(no_hace_nada(1))  # no imprime nada con esta sentencia pass en la funcion anterior
