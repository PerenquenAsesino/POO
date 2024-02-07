from cuenta_bancaria import CuentaBancaria

cuenta = CuentaBancaria("Juan Sin Miedo", "123456789", 1000)
print(f"Saldo inicial: {cuenta.mostrar_saldo()}€")


cuenta.depositar(400)
print(f"Despues de depositar 400€, el saldo es: {cuenta.mostrar_saldo()}€")


cuenta.retirar(2000)


cuenta.retirar(100)
print(f"Despues de retirar 100€, el saldo es: {cuenta.mostrar_saldo()}€")


