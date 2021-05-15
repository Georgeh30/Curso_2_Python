from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")
# raiz.resizable(True, False)
# raiz.geometry("650x350")
raiz.config(
    bg="blue"
)
raiz.iconbitmap("../img/icono.ico")
# FIN DE LA RAIZ O ROOT

# INICIO DEL FRAME O CUADRO
miFrame = Frame(raiz, width=650, height=350)

# Para que se expanda el frame junto a la ventana raiz o root
miFrame.pack(
    fill="both",
    expand="True"
)
miFrame.config(
    # bd=35,  # Tamaño borde del cuadro
    # relief="sunken",  # Tipo de borde
    # bg="red",
    # width="650",  # Ancho del cuadro
    # height="350",  # Alto del cuadro
    # cursor="pirate"
)
# FIN DEL FRAME O CUADRO

# Etiqueta para mostrar imagen
miImagen = PhotoImage(file="../img/img.png")
miLabel_img = Label(miFrame, image=miImagen, width=200, height=200)
miLabel_img.place(x=450, y=150)  # Posicion dentro del frame o cuadro

# Etiqueta para mostrar texto
miLabel_txt = Label(miFrame, text="etiqueta de texto", fg="white", bg="red", font=("Comic Sans MS", 18))
miLabel_txt.place(x=250, y=310)  # Posicion dentro del frame o cuadro

# Etiqueta para mostrar texto
label_nombre = Label(miFrame, text="Nombre:")
# label_nombre.grid(row=0, column=0)  # Posicion por fila y columna
label_nombre.place(x=215, y=10)  # Posicion dentro del frame o cuadro

# Cuadro de texto
cuadro_txt = Entry(miFrame)
cuadro_txt.place(x=270, y=10)  # Posicion dentro del frame o cuadro


raiz.mainloop()
