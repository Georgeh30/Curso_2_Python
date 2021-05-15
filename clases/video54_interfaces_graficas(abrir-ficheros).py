from tkinter import *
from tkinter import filedialog

root = Tk()


def abreFichero():
    # Creamor un Boton para abrir fichero e indicamos la ruta que abrira el fichero ...
    # y el tipo de documentos que puede filtrar
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:/Users/johnc/Downloads",
                                         filetypes=(("Ficheros de Excel", "*.xlsx"),
                                                    ("Ficheros de Texto", "*.docx"),
                                                    ("Tdosos los Ficheros", "*.*")))

    print(fichero)  # Imprime la ruta obtenida


Button(root, text="Abrir Fichero", command=abreFichero).pack()

root.mainloop()
