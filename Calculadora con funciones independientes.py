def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por 0"
    return a / b

def calculadora():
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
    opcion = input("Seleccione una opción: ")

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print(sumar(a, b))
    elif opcion == "2":
        print(restar(a, b))
    elif opcion == "3":
        print(multiplicar(a, b))
    elif opcion == "4":
        print(dividir(a, b))
    else:
        print("Opción inválida")
