class Vehiculo:
    def __init__(self, marca):
        self.__marca = marca

    def mover(self):
        print("El vehículo se mueve")

class Auto(Vehiculo):
    def mover(self):
        print("El auto circula por carretera")

class Moto(Vehiculo):
    def mover(self):
        print("La moto avanza rápidamente")

a = Auto("Toyota")
m = Moto("Yamaha")

a.mover()
m.mover()