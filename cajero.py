"""
1. crear una cuenta. el programa pide nombre e ingreso inicial

2.- presenta un mensaje que dice "tipo de movimiento (I-ingrso, R-retirada *-fin)

    -si el tipo de movimiento es I
        -pedir cantidad
        -validar que la cantidad sea un numero y positiva
        -realizar el ingreso
        -si la cantiada no es un numero o no es positiva, volver a pedirla

    - si el tipo de movimiento es R
        -pedir cantidad
        - validar que la cantidad se a un numer y positiva
        - si el numero es correcto, realizar la retiurarda
            -si la retirada devuielve saldo insuficiente, avisar y volver al punto 2
            -si la retirada va bien volver al punto 2
        - sila cantidad no es un numero o no e spositiva, vo0lver a pedirla (pedir cantidad)

    -si el tipo es *
        -imprimir el saldo de la cuenta
        -fin del programa

    -si el tipo no e sniunguno de los anteriores volver a 2

"""
import random
from entities import Cuenta_bancaria

"""
Entrada del nombre
"""
nombre = input("Nombre: ")
while len(nombre) < 3:
    print("El nombre debe tener al menos 3 caracteres.")
    nombre = input("Nombre: ")

"""
Entrada del saldo inicial
"""
saldo = input("Cantidad a ingresar: ")
while not saldo.isnumeric() or int(saldo) < 50:
    if not saldo.isnumeric():
        print("Introduce un valor numerico")
    else:
            print("Ingreso minimo de 50 Euros")
    saldo = input("Cantidad a ingresar: ")


la_cuenta = Cuenta_bancaria(nombre ),
                            float(input("Cantidad a ingresar: "),
                            random.randint(1000, 9999))