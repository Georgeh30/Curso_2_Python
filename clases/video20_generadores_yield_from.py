
def devuelve_ciudades(*ciudades):

    # MANERA DE INGRESAR A UNA LISTA BIDIMENSIONAL SIN USAR FOR ANIDADO
    for elemento in ciudades:
        yield from elemento  # Guarda los elementos por subvalor dentro de (elemento)


ciudades_devueltas = devuelve_ciudades("Mexico", "Durango", "Monterrey", "Guanajuato")

print(next(ciudades_devueltas))  # Muestra el primer subvalor del primer valor
print(next(ciudades_devueltas))  # Muestra el segundo subvalor del primer valor
