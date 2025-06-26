# operaciones.py

def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None

def division(a, b):
    try:
        return a / b
    except TypeError:
        print("Error: Tipo de dato no válido")
        return None
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
        return None
