class Deportista:
    def __init__(self, nombre, deporte):
        self.nombre = nombre
        self.deporte = deporte
        print("DEPORTE")
        print(f"Nombre: {self.nombre}")
        print(f"Deporte: {self.deporte}")

class Futbolista(Deportista):
    def __init__(self, nombre, deporte, posicion):
        super().__init__(nombre, deporte)
        self.posicion = posicion
        print("FUTBOLISTA")
        print(f"Posición: {self.posicion}")

jugador = Futbolista("Luis", "Fútbol", "Delantero")