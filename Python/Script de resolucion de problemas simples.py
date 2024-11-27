# Calculadora básica
print("-- Calculadora -- ")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("No se puede dividir por cero")
        resultado = None
    else:
        resultado = num1 / num2
else:
    print("Operación inválida")
    resultado = None

if resultado is not None:
    print("<<El resultado es:", resultado, ">>" , "\n")

# Juego de adivinanza
print("-- Adivinador -- ")

import random
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    try:
        intento = int(input("Adivina el número (1-100): "))
        intentos += 1
        if intento < numero_secreto:
            print("\n")
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("\n")
            print("El número es menor.")
        else:
            print( "\n" , "¡Adivinaste! Tardaste", intentos, "intentos.")
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")
