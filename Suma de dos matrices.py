A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

suma = []
for i in range(len(A)):
    fila = []
    for j in range(len(A[0])):
        fila.append(A[i][j] + B[i][j])
    suma.append(fila)

print(suma)
