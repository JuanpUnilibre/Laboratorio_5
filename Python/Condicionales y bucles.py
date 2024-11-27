# Número par o impar
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Bucle for
print("\n")

for i in range(1, 6):
    print(i*i)
    
print("\n")

# Bucle while
while True:
    respuesta = input("¿Quieres continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break