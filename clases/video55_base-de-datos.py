import sqlite3

# Realizamos la conexion con una archivo de base de datos que se creara con el nombre "PrimeraBase"
miConexion = sqlite3.connect("../base/PrimeraBase")

miCursor = miConexion.cursor()

# GUARDAR O INSERTAR DATOS DENTRO DE UNA TABLA
# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# CREACION DE UNA LISTA CON TUPLAS PARA INSERTARLAS DENTRO DE LA BASE DE DATOS SQLITE
"""variosProductos = [

    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")

]

# GUARDA VARIOS REGISTROS DE UNA LIST
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", variosProductos)"""

# CONSULTA DE DATOS DENTRO DE UNA TABLA DE LA BASE DE DATOS
miCursor.execute("SELECT * FROM PRODUCTOS")

# DEVUELVE LOS DATOS DE LA CONSULTA A LA BASE DE DATOS REALIZADA ARRIBA
variosProductos = miCursor.fetchall()
print(variosProductos)

# IMPRIME CADA FILA DE LOS DATOS GUARDADOS DENTRO DE LA TABLA
for productos in variosProductos:
    for u in range(1):
        print(f"Articulo: {productos[0]} ,Precio: {productos[1]} ,Seccion: {productos[2]}")

# CONFIRMA PARA ENVIAR LA COMUNICACION CON LA BASE
miConexion.commit()


miConexion.close()
