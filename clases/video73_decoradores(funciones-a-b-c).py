

# ESTA FUNCION ES LA QUE VA A DECORAR A OTRAS FUNCION,
# LA CUAL TIENE DOS FUNCIONES MAS DENTRO DE ELLA
def funcion_decoradora(funcion_parametro):
    # SEGUNDA FUNCION
    def funcion_interior(*args, **kwargs):

        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

        # MANDAMOS A LLAMAR LA FUNCION DEL PARAMETRO LA CUAL ES LA TERCERA FUNCION
        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")
    return funcion_interior


# ESTA LINEA DE CODIGO SIRVE PARA AGREGARLE LA FUNCION DECORADORA A LA FUNCION SUMA
@funcion_decoradora
def suma(numero1, numero2):
    print(numero1 + numero2)


# ESTA LINEA DE CODIGO SIRVE PARA AGREGARLE LA FUNCION DECORADORA A LA FUNCION RESTA
@funcion_decoradora
def resta(numero1, numero2):
    print(numero1 - numero2)


# ESTA LINEA DE CODIGO SIRVE PARA AGREGARLE LA FUNCION DECORADORA A LA FUNCION POTENCIA
@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


# MANDAMOS A LLAMAR LAS FUNCIONES NORMALES YA CON LA FUNCION DECORADA AGREDA A ELLAS
suma(10, 10)
resta(41, 20)

# SOLO CUANDO SE PONE COMO PARAMETRO LA CLAVE --> base, Y EL VALOR --> 5
# ES CUANDO SE PONE **kwargs PARA PASAR UN INDETERMINADO NUMERO DE PARAMETROS
potencia(base=5, exponente=3)
