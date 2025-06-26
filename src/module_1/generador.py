# generador.py

import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        entrada = input(mensaje)
        try:
            num = float(entrada)
            if ini <= num <= fin:
                return num
            else:
                print(f"Entrada fuera del rango [{ini}-{fin}].")
        except ValueError:
            print("Por favor, introduce un número válido.")

def generador():
    numeros = int(leer_numero(1, 20, "¿Cuántos números quieres generar? [1-20]: "))
    modo = int(leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: "))
    
    resultado = []
    for _ in range(numeros):
        num = random.uniform(0, 100)
        if modo == 1:
            red = math.ceil(num)
        elif modo == 2:
            red = math.floor(num)
        else:
            red = round(num)
        
        print(f"Número original: {num:.4f}, redondeado: {red}")
        resultado.append(red)
    return resultado

if __name__ == "__main__":
    lista = generador()
    print("Lista final:", lista)
# Generador de números aleatorios con redondeo
# Este script genera una lista de números aleatorios entre 0 y 100,
# permitiendo al usuario elegir cómo redondearlos (al alza, a la baja o normal).
# El usuario puede especificar cuántos números generar (entre 1 y 20).
# El resultado es una lista de números redondeados según la elección del usuario.
# El script maneja errores de entrada y asegura que los números generados estén dentro del rango especificado.
# El resultado final se imprime al usuario. 
# El script utiliza las bibliotecas random y math para generar números aleatorios y realizar operaciones de redondeo.
# El script se ejecuta directamente si se llama desde la línea de comandos.
# El script es útil para generar números aleatorios con diferentes métodos de redondeo,
# lo que puede ser útil en diversas aplicaciones, como simulaciones o pruebas.