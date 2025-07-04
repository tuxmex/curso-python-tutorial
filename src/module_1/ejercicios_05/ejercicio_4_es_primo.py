# funcion_es_primo.py
# Verifica si un número es primo

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Ingresa un número: "))
    print(f"{n} es primo: {es_primo(n)}")
