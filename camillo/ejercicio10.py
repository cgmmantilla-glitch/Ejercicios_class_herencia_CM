class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print("CUENTA")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

class Ahorro(Cuenta):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes = interes
        print("CUENTA DE AHORRO")
        print(f"Interés: {self.interes}%")

cliente = Ahorro("Ana", 1000, 5)