def es_numero_perfecto(n):
    if n <= 0:
        return False
    suma = sum(i for i in range(1, n) if n % i == 0)
    return suma == n

def es_numero_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_digitos(n):
    return sum(int(d) for d in str(abs(n)))
