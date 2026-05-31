class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def sonido(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau Miau")

p = Perro("Firulais")
g = Gato("Michi")

p.sonido()
g.sonido()