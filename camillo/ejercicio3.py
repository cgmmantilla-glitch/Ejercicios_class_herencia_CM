class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        print("DATOS DEL ANIMAL")
        print(f"Nombre: {self.nombre}")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        print("DATOS DEL PERRO")
        print(f"Raza: {self.raza}")

mascota = Perro("Rocky", "Pitbull")