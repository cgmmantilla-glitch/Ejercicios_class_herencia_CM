class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        print("PRODUCTO")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")

class Factura(Producto):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio)
        self.cantidad = cantidad
        total = self.precio * self.cantidad
        print("FACTURA")
        print(f"Cantidad: {self.cantidad}")
        print(f"Total: {total}")

venta = Factura("Mouse", 15, 3)