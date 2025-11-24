agenda = {}

while True:
    nombre = input("Nombre (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

print(agenda)
