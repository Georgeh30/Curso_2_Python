from tkinter import *

root = Tk()

root.title("Ejemplo")

# Inicializando variables
playa = IntVar()
montana = IntVar()
turismoRural = IntVar()


# Funcion para indicar cuales se han seleccionado
def opcionesViaje():
    opcionesEscogida = ""

    if playa.get() == 1:
        opcionesEscogida += " playa"

    if montana.get() == 1:
        opcionesEscogida += " montaña"

    if turismoRural.get() == 1:
        opcionesEscogida += " turismo rural"

    textoFinal.config(text=opcionesEscogida)


# Obteniendo una imagen desde la ruta indicada
foto = PhotoImage(file="../img/cerdo.png")
# Insertando Imagen dentro del label_text y empaquetandolo dentro del root
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige Destinos", width=50).pack()

"""
FUNCION DE CADA ATRIBUTO DENTRO DE LOS CHECKBUTTONS:
    1. frame --> indica que debe de estar dentro del frame
    2. text --> para mostrar el texto dentro del checkbutton
    3. variable --> enlaza variable inicializada hasta arriba del codigo con el checkbutton ...
                    para guardar el valor que obtenga de "onvalue" y "offvalue".
    4. onvalue --> manda el valor "1" a la variable "playa" indicando que esta seleccionada
    5. offvalue --> manda el valor "0" a la variable "playa" indicando que NO esta seleccionada
    6. command --> para mandar a llamar la funcion
    7. .pack() --> empaqueta el objeto checkbutton dentro del frame 
"""

# Creando y empaquetando varios checkbutton dentro de root
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

# LabelText para mostrar las opciones seleccionadas
textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
