# 🔮 Detector de Números Mágicos

Un proyecto educativo en Python para practicar **operadores aritméticos, lógicos y de comparación**, mediante la detección de propiedades "mágicas" en números. Ideal para estudiantes de nivel principiante e intermedio.

---

## 🎯 Objetivos

- Aplicar operadores booleanos (`and`, `or`, `not`) y de comparación (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Usar condiciones combinadas para crear expresiones lógicas complejas
- Detectar propiedades matemáticas especiales como números primos, perfectos o palíndromos
- Fomentar el pensamiento lógico y la depuración de código

---

## 📁 Estructura del Proyecto

```

detector\_numeros\_magicos/
│
├── main.py                   # Programa principal con menú interactivo
├── detector\_magico.py        # Lógica de análisis y puntuación de números
├── funciones\_magicas.py      # Funciones auxiliares (perfecto, primo, suma\_digitos)
├── README.md                 # Este archivo

````

---

## 🚀 Cómo Ejecutar

### Requisitos

- Python 3.8 o superior

### Ejecutar desde terminal

```bash
python main.py
````

---

## 📋 Funcionalidades del Menú

1. **Analizar un número manualmente**
   Introduce un número para evaluar si es mágico y ver su puntuación.

2. **Ver números mágicos famosos**
   Se analizan números como 6, 28, 496 (números perfectos).

3. **Juego: Encuentra un número mágico**
   Mini-juego en el que tienes 10 intentos para adivinar un número con nivel de magia alto.

4. **Analizar rango de números**
   Encuentra todos los números mágicos entre dos valores dados.

5. **Salir**
   Cierra el programa.

---

## 🔍 ¿Qué se considera un número mágico?

Un número puede ser considerado mágico si cumple una o más de las siguientes condiciones:

| Condición                                           | Puntos |
| --------------------------------------------------- | ------ |
| Es un número perfecto                               | +100   |
| Es primo                                            | +50    |
| Es par, múltiplo de 3 y mayor que 50                | +30    |
| Es múltiplo de 5 y 7                                | +25    |
| Suma de sus dígitos es 7, 11 o 13                   | +20    |
| Es impar, múltiplo de 3 y su suma de dígitos es par | +15    |
| Es un número culturalmente mágico (7, 13, 42, etc.) | +40    |

---

## 🎮 Mini-juego: Adivina un Número Mágico

Encuentra un número cuyo **nivel de magia sea mayor a 30**. El juego te da pistas y analiza tu número en cada intento.

---

## 💡 Conceptos Aplicados

* Uso del operador **módulo `%`**
* Evaluación de **números primos**
* **Suma de dígitos** y propiedades numéricas
* **Condicionales múltiples y anidados**
* **Depuración y análisis de lógica**
* Buenas prácticas con estructuras de control

---

## 🧠 Ejercicios Complementarios

> Para implementar como extensión del proyecto:

* **Detector de Fibonacci mágicos**
* **Detectores de números Vampiro**
* **Palíndromos mágicos (en base 10 o binario)**
* **Calculadora de expresiones mágicas booleanas**

---

## 📚 Recursos recomendados

* [Documentación oficial de Python](https://docs.python.org/3/)
* [Curso Python TuxMex](https://tuxmex.github.io/curso-python-tutorial/)
* [Wikipedia - Números mágicos, perfectos y primos](https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto)

---

## 📜 Licencia

Este proyecto es de uso educativo y está licenciado bajo **MIT**. Puedes modificarlo, usarlo y compartirlo con fines académicos.
