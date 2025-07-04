# funciones_basicas.py
# Ejemplos de funciones sin parámetros y con valores de retorno

def saludar():
    print("¡Hola desde una función!")

def obtener_pi():
    return 3.14159

def main():
    saludar()
    pi = obtener_pi()
    print(f"El valor de PI es: {pi}")

if __name__ == "__main__":
    main()
