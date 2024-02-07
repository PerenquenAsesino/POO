class CuentaBancaria:
    def __init__(self, titular, num_cuenta, saldo_inicial = 0):
        self.titular = titular
        self.num_cuenta = num_cuenta
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo


    def retirar(self, cantidad): #asegurarse que el saldo no sea negativo
        if self.saldo < cantidad:
            return "Fondos insuficientes"
        else:
            self.saldo -= cantidad
        return self.saldo


    def mostrar_saldo(self):
        return self.saldo