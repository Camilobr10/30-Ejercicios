lista = list(map(int, input("Ingrese números separados por espacio: ").split()))

promedio = sum(lista) / len(lista)

mayores = [x for x in lista if x > promedio]

print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)
