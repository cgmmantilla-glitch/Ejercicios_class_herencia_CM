class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("DATOS PERSONALES")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        print("DATOS DEL EMPLEADO")
        print(f"Sueldo: {self.sueldo}")

trabajador = Empleado("Carlos", 25, 500)