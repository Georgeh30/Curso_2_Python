# Generator nos sirve como su palabra lo dice para generar datos o valores
# de una mejor forma que la tradicional al poner yield en vez de return,
# para eso se muestra dos funciones la primera de la forma tradicional y
# la segunda de la forma mejorada con yield

# VENTAJAS: AHORRA ESPACIO EN MEMORIA YA QUE NO GENERA LOS DATOS COMPLETOS
# AL MOMENTO DE LLAMAR SOLO CIERTA PARTE DE LOS DATOS, ESTO SIRVE MAS CUANDO
# NECESITAMOS GENERAR VALORES INFINITOS
print("PRIMERA FORMA TRADICIONAL")


# PRIMERA OPCION, LA FORMA TRADICIONAL DE GENERAR EN ESTE CASO NUMEROS PARES
def generadorNumPares(limite):
    num = 1
    miLista = []

    while num < limite:
        miLista.append(num * 2)
        num += 1

    return miLista


print(generadorNumPares(10))

print("SEGUNDA FORMA CON YIELD")


# SEGUNDA OPCION, LA FORMA MEJORADA GENERANDO Y GUARDANDO LOS DATOS SIN LA NECESIDAD DE UNA LISTA
def generadorNumParesmejorado(limite):
    num = 1

    while num < limite:
        yield num * 2
        num += 1


obtengopares = generadorNumParesmejorado(10)  # Guardamos los datos que estan de tipo objeto (generator)

print(type(obtengopares))  # Mostramo el tipo objeto (generator) de la variable

"""print(next(obtengopares))  # Devuelve el primer valor, despues...
print(next(obtengopares))  # Devuelve el segundo valor y asi sucesivamente..."""

for i in obtengopares:  # Para mostrar los datos debemos de interar en ellos
    print(i)  # Imprimimos cada valor dentro de este generator
