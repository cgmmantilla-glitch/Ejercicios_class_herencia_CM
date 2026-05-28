class Computadora:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram
        print("COMPUTADORA")
        print(f"Marca: {self.marca}")
        print(f"RAM: {self.ram}")

class Laptop(Computadora):
    def __init__(self, marca, ram, bateria):
        super().__init__(marca, ram)
        self.bateria = bateria
        print("LAPTOP")
        print(f"Batería: {self.bateria}")

pc = Laptop("HP", "8GB", "5000mAh")