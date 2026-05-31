class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def mostrar(self):
        print("Información del producto")

class Laptop(Producto):
    def mostrar(self):
        print("Laptop para uso profesional")

class Celular(Producto):
    def mostrar(self):
        print("Celular para comunicación")

p1 = Laptop("Lenovo", 800)
p2 = Celular("Samsung", 500)

p1.mostrar()
p2.mostrar()