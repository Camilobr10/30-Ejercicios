notas = {}

while True:
    nombre = input("Nombre (o 'fin'): ")
    if nombre == "fin":
        break
    nota = float(input("Nota: "))
    notas[nombre] = nota

promedio = sum(notas.values()) / len(notas)

print("Promedio general:", promedio)
