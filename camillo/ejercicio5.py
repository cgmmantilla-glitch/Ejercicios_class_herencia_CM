class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        print("LIBRO")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

class Biblioteca(Libro):
    def __init__(self, titulo, autor, cantidad):
        super().__init__(titulo, autor)
        self.cantidad = cantidad
        print("BIBLIOTECA")
        print(f"Cantidad: {self.cantidad}")

libro1 = Biblioteca("Python Básico", "Juan Pérez", 10)