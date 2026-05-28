class Hospital:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        print("HOSPITAL")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")

class Paciente(Hospital):
    def __init__(self, nombre, direccion, paciente):
        super().__init__(nombre, direccion)
        self.paciente = paciente
        print("PACIENTE")
        print(f"Paciente: {self.paciente}")

dato = Paciente("Hospital Quito", "Centro", "María")