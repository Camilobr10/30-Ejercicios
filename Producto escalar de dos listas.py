A = list(map(int, input("Lista A: ").split()))
B = list(map(int, input("Lista B: ").split()))

producto_escalar = sum(A[i] * B[i] for i in range(len(A)))

print("Producto escalar =", producto_escalar)
