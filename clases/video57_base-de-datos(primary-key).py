import sqlite3

miConexion = sqlite3.connect("../base/GestionProductos")

miCursor = miConexion.cursor()

# CREACION DE UNA TABLA UTILIZANDO EL CODIGO EXCUTE Y DANDOLE FORMATO PARA QUE SE ENTIENDA MEJOR
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        CODIGO_ARTICULO     VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO     VARCHAR(50),
        PRECIO              INTEGER,
        SECCION             VARCHAR(20)
    )
''')

# CREACION DE UNA LIST CON VARIAS TUPLAS PARA INSERTAR MAS ADELANTE LOS DATOS DE UN SOLO JALON
productos = [
    ("AR01", "pelota", 20, "jugueteria"),
    ("AR02", "pantalon", 15, "confección"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarrón", 45, "cerámica")
]

# CREAMOS EL CODIGO PARA INSERTAR LOS DATOS DE LA LIST ANTERIOR DENTRO DE LA TABLA DE LA BASE DE DATOS
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?, ?)", productos)

miConexion.commit()

miConexion.close()
