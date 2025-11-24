x = int(input("x: "))
y = int(input("y: "))
coord = (x, y)

minimo = int(input("Límite inferior: "))
maximo = int(input("Límite superior: "))

if minimo <= coord[0] <= maximo and minimo <= coord[1] <= maximo:
    print("Dentro del rango")
else:
    print("Fuera del rango")
