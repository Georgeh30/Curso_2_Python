import sqlite3

miConexion = sqlite3.connect("../base/GestionProductos")

miCursor = miConexion.cursor()

"""------------------------------------------CREATE-------------------------------------------"""

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
        CODIGO_ARTICULO     VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO     VARCHAR(50),
        PRECIO              INTEGER,
        SECCION             VARCHAR(20)
    )
''')

"""------------------------------------------READ-------------------------------------------"""

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")

productos = miCursor.fetchall()
print(productos)

"""------------------------------------------UPDATE-------------------------------------------"""

miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota'")

"""------------------------------------------DELETE-------------------------------------------"""

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")

miConexion.commit()

miConexion.close()
