class Electrodomestico:
    def __init__(self, marca):
        self.__marca = marca

    def encender(self):
        print("El electrodoméstico se ha encendido")

class Televisor(Electrodomestico):
    def encender(self):
        print("El televisor muestra imágenes en pantalla")

class Refrigeradora(Electrodomestico):
    def encender(self):
        print("La refrigeradora comienza a enfriar")

tv = Televisor("LG")
refri = Refrigeradora("Indurama")

tv.encender()
refri.encender()