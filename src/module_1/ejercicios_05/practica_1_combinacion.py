# practica_combinacion.py
# Práctica integradora: mezcla ejercicios anteriores

from math import factorial
from funcion_es_primo import es_primo

def sumar(a, b): return a + b

def es_par(n): return n % 2 == 0

def info_numero(n):
    return {
        "es_primo": es_primo(n),
        "es_par": es_par(n),
        "factorial": factorial(n) if n >= 0 else None
    }

if __name__ == "__main__":
    num = int(input("Ingresa un número: "))
    info = info_numero(num)
    print(f"Información sobre {num}:")
    print(f"- Primo: {info['es_primo']}")
    print(f"- Par: {info['es_par']}")
    print(f"- Factorial: {info['factorial']}")
