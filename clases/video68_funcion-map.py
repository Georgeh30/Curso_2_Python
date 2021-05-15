class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de ${self.salario}.00 °°"


listaEmpleados = [
    Empleado("Jorge", "Director", 9500),
    Empleado("Pedro", "Presidente", 8500),
    Empleado("Luis", "Seretario", 5500),
    Empleado("Maria", "Botones", 4800),
    Empleado("Luis", "Jefe", 1500)
]


def calculo_comision(empleado):
    if empleado.salario <= 3000:
        empleado.salario = empleado.salario * 1.03
    return empleado


# LLAMAMOS LA FUNCION MAP EL CUAL PIDE DOS PARAMETROS EL PRIMERO ES PARA
# LA FUNCION PARA CALCULAR LA COMISION Y EL SEGUNDO PARA DARLE EL PARAMETRO
# A LA FUNCION CALCULO_COMISION, EL CUAL EL MAP HACE LO QUE HARIA UN FOR PARA
# IR DE OBJETO EMPLEADO A OBJETO EMPLEADO E IR INGRESANDOLO EN LA FUNCION PARA CALCULAR
listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)
