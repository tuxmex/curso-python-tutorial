# funcion_factorial.py
# Calcula factorial recursivo

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input("Número para factorial: "))
    result = factorial(n)
    if result is None:
        print("No se puede calcular factorial de un número negativo.")
    else:
        print(f"{n}! = {result}")
