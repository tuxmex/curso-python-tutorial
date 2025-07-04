# ejercicio_fibonacci.py
# Genera secuencia Fibonacci

def fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[-1] + serie[-2])
    return serie[:n]

if __name__ == "__main__":
    n = int(input("¿Cuántos términos quieres?: "))
    print(f"Primera serie Fibonacci: {fibonacci(n)}")
