from tkinter import *

# INTERFAZ GRAFICA INICIALIZADA
raiz = Tk()

# FRAME O CUADRO INICIALIZADO ENCAPSULANDOLO EN LA RAIZ O ROOT
miFrame = Frame(raiz)
miFrame.pack()  # Empaquetamiento del Frame, es el que ajusta este frame dentro de la raiz

# VARIABLES INICIALIZADAS
operacion = ""
reset_pantalla = False
resultado = 0

"""------------------------------PANTALLA RESULTADOS-------------------------------"""

# Inicilizamos varible indicando que es de tipo StringVar()
numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)  # Inicializamos dentro de Frame insertando variable anterior
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)  # Opcion para ajustes de este objeto cuadro de texto
pantalla.config(background="black", fg="#FFFFFF", justify="right")  # Estilo del cuadro de texto

"""------------------------------PULSACIONES TECLADO-----------------------------"""


def numeroPulsado(num):
    # Declaramos que ya existen fuera de la funcion y que son globales
    global operacion
    global reset_pantalla

    # SÍ es True esta variable entonces entraria
    if reset_pantalla:
        numeroPantalla.set(num)  # Ingresamos lo que contenga num
        reset_pantalla = False  # Reseteamos el booleano
    else:
        # Insertamos el numero obtenido del boton y lo vamos guardando con el anterior guardado en la misma variable
        numeroPantalla.set(numeroPantalla.get() + num)


"""----------------------------------FUNCION SUMA---------------------------------"""


def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroPantalla.set(resultado)


"""----------------------------------FUNCION RESTAR---------------------------------"""

num1 = 0
contador_resta = 0


def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True


"""---------------------------------FUNCION MULTIPLICACION--------------------------------"""

contador_multi = 0


def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_multi = contador_multi + 1
    operacion = "multiplicacion"
    reset_pantalla = True


"""----------------------------------FUNCION DIVIDIR---------------------------------"""

contador_divi = 0


def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_divi = contador_divi + 1
    operacion = "division"
    reset_pantalla = True


"""----------------------------------FUNCION EL RESULTADO---------------------------------"""


def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi

    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numeroPantalla.set(int(resultado) / int(numeroPantalla.get()))
        resultado = 0
        contador_divi = 0


"""------------------------------------FILA 1------------------------------------"""

# COMMAND sirve para mandar a llamar funciones cuando se oprima el respectivo boton, ...
# PEROOO!! al declarar los parentesis --> ( ) python llama la funcion sin la necesidad de ...
# apretar el boton, por ello se debe de guardar primero esta funcion dentro de lambda para ...
# que no la mande a llamar sin autorizacion

boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3, command=lambda: divide(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)

"""------------------------------------FILA 2------------------------------------"""

boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="X", width=3, command=lambda: multiplica(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

"""------------------------------------FILA 3------------------------------------"""

boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3, command=lambda: resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

"""------------------------------------FILA 4------------------------------------"""

boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=".", width=3, command=lambda: numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()
