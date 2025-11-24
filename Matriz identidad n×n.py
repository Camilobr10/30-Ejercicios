n = int(input("Ingrese n: "))

identidad = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(1 if i == j else 0)
    identidad.append(fila)

for fila in identidad:
    print(fila)
