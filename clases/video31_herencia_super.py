# METODO SUPER EL CUAL NOS AYUDA A OBTENER LOS METODO DE LA CLASE HEREDADA PARA MANDAR
# A LLAMARLAS DENTRO DE LA CLASE DONDE SE HEREDO LA CLASE


# Clase 1
class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nResidencia: {self.lugar_residencia}"


# Clase 2
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        # EL METODO SUPER O LA CLASE PERSONA SE MANDA A LLAMAR EN SOLO UNA DE LAS DOS FORMAS
        # PARA LLAMAR EL CONSTRUCTOR DE LA CLASE QUE HEREDAMOS
        """ OPCION 1: """
        # Persona.__init__(self, nombre_empleado, edad_empleado, residencia_empleado)
        """ OPCION 2: """
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nResidencia: {self.lugar_residencia}" \
               f"\nSalario: {self.salario}\nAntiguedad: {self.antiguedad}"


# Instancia de la clase Empleado
manuel = Empleado(1500, 15, "Manuel", 55, "Mexico")

# Imprimimos el metodo str de la clase heredada pero se
# sobreescribe el metodo str de la clase en donde se hereda
print(manuel)

print("Verificacion1:", isinstance(manuel, Persona))  # Imprimer True o False para comprobar si es de una clase
print("Verificacion2:", isinstance(manuel, Empleado))

# Instancia de la clase
carlos = Persona("Carlos", 28, "Mexico")

# Imprime True o False si es tambien de este tipo de clase, pero False si no exite herencia desde esta clase
print("Verificacion3: {0}".format(isinstance(carlos, Empleado)))  # Otra forma de imprimir con (format)
