from tkinter import *

raiz = Tk()

myFrame = Frame(raiz, width=1200, height=600)
myFrame.pack()

etiqueta_nombre = Label(myFrame, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, sticky="e", padx=10, pady=10)

etiqueta_apellido = Label(myFrame, text="Apellido:")
etiqueta_apellido.grid(row=1, column=0, sticky="e", padx=10, pady=10)

etiqueta_direccion = Label(myFrame, text="Direccion:")
etiqueta_direccion.grid(row=2, column=0, sticky="e", padx=10, pady=10)

etiqueta_password = Label(myFrame, text="Contraseña:")
etiqueta_password.grid(row=3, column=0, sticky="e", padx=10, pady=10)

etiqueta_comentarios = Label(myFrame, text="Comentarios:")
etiqueta_comentarios.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Cuadro de Texto para el campo Nombre
nombre = StringVar()  # Indicamos el tipo de variable
cuadro_nombre = Entry(myFrame, textvariable=nombre)  # Asociamos la variable nombre con el cuadro de texto nombre
cuadro_nombre.grid(row=0, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="blue", justify="center")  # config sirve para modificar el contenido del cuadro de texto

cuadro_apellido = Entry(myFrame)
cuadro_apellido.grid(row=1, column=1, padx=10, pady=10)
cuadro_apellido.config(fg="blue", justify="right")

cuadro_direccion = Entry(myFrame)
cuadro_direccion.grid(row=2, column=1, padx=10, pady=10)
cuadro_direccion.config(fg="blue", justify="left")

cuadro_password = Entry(myFrame)
cuadro_password.grid(row=3, column=1, padx=10, pady=10)
cuadro_password.config(show="*", fg="blue", justify="center")

cuadro_comentarios = Text(myFrame, width=16, height=5)
cuadro_comentarios.grid(row=4, column=1, padx=10, pady=10)
scroll_vertical = Scrollbar(myFrame, command=cuadro_comentarios.yview)
scroll_vertical.grid(row=4, column=2, sticky="nsew")
cuadro_comentarios.config(fg="red", yscrollcommand=scroll_vertical.set)


# Creamos la Funcion para realizar una accion en el boton
def accionBotonEnviar():
    # nombre.set("Jorge")  # Insertamos el texto dentro de la variable nombre
    variable_nombre = cuadro_nombre.get()  # Obtenemos el dato ingresado
    print(variable_nombre)
    nombre.set("")  # Borrar dentro del cuadro de texto asociado a esta variable


# Boton Enviar
boton_enviar = Button(raiz, text="Enviar", command=accionBotonEnviar)  # asignamos la funcion al boton
boton_enviar.pack()

raiz.mainloop()
