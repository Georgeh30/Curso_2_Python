from tkinter import *
from tkinter import messagebox

root = Tk()

"""*****************************************VENTANAS EMERGENTES****************************************"""


def infoAdicional():
    messagebox.showinfo("Hecho Por Georgio", "Prueba de pantalla emergente")


def avisionLicencia():
    messagebox.showwarning("Titulo", "Datos dentro de la ventana")


def salirAplicacion():
    # valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")

    """if valor == "yes":
        root.destroy()  # Metodo dentro de root para salir de la aplicacion"""
    if valor:
        root.destroy()  # Metodo dentro de root para salir de la aplicacion


def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar, Documento bloqueado")
    if not valor:
        root.destroy()  # Metodo dentro de root para salir de la aplicacion


"""*****************************************BARRA MENU****************************************"""

# Creacion de la Barra Menu Principal
barraMenu = Menu(root)

# Configuraciones de la ventana
root.config(
    menu=barraMenu,  # Indicamos que va a tener una barra menu en la ventana root
    width=300,
    height=300
)

"""*****************************************MENU ARCHIVOS****************************************"""

# Creamos un Menu agregandola dentro de la barra menu principal
archivoMenu = Menu(barraMenu, tearoff=0)  # el atributo "tearoff" es para quitar una linea que aparecia
# Creamos los Submenus agregandolos dentro del Menu Archivo
archivoMenu.add_command(label="Nuevo", command=avisionLicencia)  # Submenu dentro del Menu Archivo
archivoMenu.add_command(label="Abrir")  # Submenu dentro del Menu Archivo
archivoMenu.add_separator()  # Separador de submenus
archivoMenu.add_command(label="Cerrar Documento", command=cerrarDocumento)  # Submenu dentro del Menu Archivo
archivoMenu.add_separator()  # Separador de submenus
archivoMenu.add_command(label="Pegar")  # Submenu dentro del Menu Archivo
archivoMenu.add_command(label="Salir", command=salirAplicacion)  # Submenu dentro del Menu Archivo
# Agregamos el Menu dentro de la barra menu y le indicamos el menu al que agregaremos un nuevo nombre
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

"""*****************************************MENU EDICION****************************************"""

# Creamos un Menu agregandola dentro de la barra menu principal
archivoEdicion = Menu(barraMenu, tearoff=0)
# Creamos los Submenus agregandolos dentro del Menu Edicion
archivoEdicion.add_command(label="Comprimir")  # Submenu dentro del Menu Edicion
archivoEdicion.add_command(label="Editar")  # Submenu dentro del Menu Edicion
# Agregamos el Menu dentro de la barra menu y le indicamos el menu al que agregaremos un nuevo nombre
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

"""**************************************MENU HERRAMIENTAS****************************************"""

# Creamos un Menu agregandola dentro de la barra menu principal
archivoHerramientas = Menu(barraMenu, tearoff=0)
# Creamos los Submenus agregandolos dentro del Menu Herramientas
archivoHerramientas.add_command(label="Rapeando")  # Submenu dentro del Menu Herramientas
archivoHerramientas.add_command(label="Configurar")  # Submenu dentro del Menu Herramientas
# Agregamos el Menu dentro de la barra menu y le indicamos el menu al que agregaremos un nuevo nombre
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

"""*****************************************MENU AYUDA****************************************"""

# Creamos un Menu agregandola dentro de la barra menu principal
archivoAyuda = Menu(barraMenu, tearoff=0)
# Creamos los Submenus agregandolos dentro del Menu Ayuda
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)  # Submenu dentro del Menu Ayuda
archivoAyuda.add_command(label="Autor")  # Submenu dentro del Menu Ayuda
# Agregamos el Menu dentro de la barra menu y le indicamos el menu al que agregaremos un nuevo nombre
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
