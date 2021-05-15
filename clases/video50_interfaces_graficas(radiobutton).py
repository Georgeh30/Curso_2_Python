# NOTA IMPORTANTE: NO se creo el Frame por eso se empaqueta (pack) cada objeto dentro de root

from tkinter import *

root = Tk()

# Inicializacion de variables
varOpcion = IntVar()


# Funcion para imprimir en consola el value del radiobutton seleccionado
def imprimir():
    # Obtenemos el valorde la variable ligada a los radiobutton y ...
    # con la asignacion de meter dentro de la variable el value 1 o el 2
    print(varOpcion.get())

    # Forma para mostrar la opcion seleccionada dentro de una etiqueta label
    if varOpcion.get() == 1:
        etiqueta.config(text="Has elegido Masculino")
    elif varOpcion.get() == 2:
        etiqueta.config(text="Has elegido Femenino")
    else:
        etiqueta.config(text="Otras Opciones")


# Otra forma de crear un label_text
Label(root, text="Género:").pack()

# Otra forma de crear un radiobutton
Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

# Otra forma de crear un radiobutton
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

Radiobutton(root, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

# Segunda forma de crear un label_text
etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
