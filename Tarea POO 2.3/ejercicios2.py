class Empleado:
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo

    def informacion(self):
        print(f"Empleado: {self.__nombre}")

class Gerente(Empleado):
    def informacion(self):
        print("Soy un Gerente")

class Secretaria(Empleado):
    def informacion(self):
        print("Soy una Secretaria")

e1 = Gerente("Ana", 1500)
e2 = Secretaria("Maria", 900)

e1.informacion()
e2.informacion()