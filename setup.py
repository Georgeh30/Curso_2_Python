from setuptools import setup  # Debemos importar este modulo para generar el empaquetado del o los modulos que deseamos

setup(

    name="paqueteprueba",  # Le damos un nombre
    version="1.0",  # Le damos una version
    description="Paquete de prueba",  # Le damos una pequeña descripcion
    author="Jorge",  # Le indicamos el nombre del autor del paquete a crear
    author_email="johncrotf2@hotmail.com",  # Le damos un correo electronico del autor
    url="",  # Una url que tenga el autor de alguna pagina web como contacto
    # Le indicamos la ruta donde esta el modulo a empaquetar,
    # el cual creamos dentro de: (Carpeta raiz = Curso-Completo-2, carpeta =  operaciones, sucarpeta =  basicas)
    # la cual ya puede estar eliminadas desde la carpeta = operacion.basicas
    packages=["operaciones", "operaciones.basicas"]

)
