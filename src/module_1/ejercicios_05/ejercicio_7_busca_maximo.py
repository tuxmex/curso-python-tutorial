# ejercicio_busqueda_maximo.py
# Devuelve número máximo de una lista usando función

def maximo(lista):
    mayor = lista[0]
    for num in lista[1:]:
        if num > mayor:
            mayor = num
    return mayor

if __name__ == "__main__":
    datos = [float(input(f"Valor {i + 1}: ")) for i in range(5)]
    print(f"Máximo: {maximo(datos)}")
