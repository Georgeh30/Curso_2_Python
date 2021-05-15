#


# OPCION 1
def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numero_par, numeros)))


# OPCION 2
print(list(filter(lambda numero_par1: numero_par1 % 2 == 0, numeros)))


# OPCION 3 FILTRAR OBJETOS


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de ${self.salario}.00 °°"


listaEmpleados = [
    Empleado("Jorge", "Director", 750000),
    Empleado("Pedro", "Presidente", 850000),
    Empleado("Luis", "Seretario", 550000),
    Empleado("Maria", "Botones", 4800),
    Empleado("Luis", "Jefe", 4500)
]

# filtra los empleados con un salario que sea mayor a 50000 la cual creamos dentro ...
# del primer parametros que pide la funcion filter
salarios_altos = filter(lambda empleado: empleado.salario > 50000, listaEmpleados)

# Interamos dentro de la lista para mostrar cada informacion de cada empleado
for empleado_salarios in salarios_altos:
    print(empleado_salarios)
