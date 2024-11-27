# Lista de estudiantes
print("-- Creación de la lista de estudiantes --")
estudiantes = ["Ana", "Juan", "Pedro", "María"]
for estudiante in estudiantes:
    print(estudiante)
print("\n")

# Diccionario de contacto
print("-- Utilización del diccionario <<Contacto>> --")
contacto = {"nombre": "Carlos", "correo": "carlos@example.com"}
print(contacto["nombre"], " --> " ,  contacto["correo"])

print("\n")

# Agregar elemento a una lista
print("-- Adicion de un elemento (Laura) a la lista previa de <<Estudiantes>> --")
estudiantes.append("Laura")
print(estudiantes)
