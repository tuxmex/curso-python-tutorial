# funcion_suma.py
# Función que suma dos números

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    x = float(input("Ingresa primer número: "))
    y = float(input("Ingresa segundo número: "))
    print(f"Suma: {sumar(x, y)}")
