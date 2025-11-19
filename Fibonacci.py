n = int(input("Ingrese un número N: "))

a, b = 0, 1
print("Serie Fibonacci hasta", n, ":")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
