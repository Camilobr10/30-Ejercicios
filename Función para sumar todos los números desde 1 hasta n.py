def suma_recursiva(n):
    if n == 0:
        return 0
    return n + suma_recursiva(n - 1)
