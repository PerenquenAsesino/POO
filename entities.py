class Cuenta_bancaria:

    def __init__(self, nombre, saldo, num_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.num_cuenta= num_cuenta

    def info(self):
        return f" {self.nombre} tiene su cuenta {self.num_cuenta} un  saldo de {self.saldo}"

    def depositar(self,deposito):
        self.saldo = self.saldo + deposito
        return self.saldo

    def retirar(self,retiro):
        if retiro > self.saldo:
            return "Saldo insuficiente"
        self.saldo = self.saldo - retiro
        return self.saldo