# ejercicio_lista_promedios.py
# Calcula el promedio de una lista usando funciones

def promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def main():
    numeros = []
    for i in range(5):
        numeros.append(float(input(f"Número {i + 1}: ")))
    print(f"Promedio: {promedio(numeros):.2f}")

if __name__ == "__main__":
    main()
