class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("VEHÍCULO")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        
class Moto(Vehiculo):
    def __init__(self, marca, color, cilindrada):
        super().__init__(marca, color)
        self.cilindrada = cilindrada
        print("MOTO")
        print(f"Cilindrada: {self.cilindrada}")

moto1 = Moto("Yamaha", "Negro", 150)