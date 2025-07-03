En Python, es importante seguir ciertas convenciones para escribir código claro, legible y consistente. Aquí tienes las reglas básicas que deberías seguir:

---

## **1. Estilo General (PEP 8)**

La guía de estilo oficial de Python es **PEP 8**, que establece las siguientes convenciones:

### **Indentación**

* Usa **4 espacios** por nivel de indentación. No uses tabulaciones.

```python
def funcion():
    if True:
        print("Correcto")
```

---

### **Longitud de líneas**

* Limita la longitud de las líneas a **79 caracteres** para código normal y **72 caracteres** para comentarios o docstrings.

---

### **Espaciado**

* **Evita espacios adicionales innecesarios:**

  * Correcto:

    ```python
    suma = a + b
    ```
  * Incorrecto:

    ```python
    suma = a  +  b
    ```
* Usa un espacio después de las comas, pero no antes:

  ```python
  lista = [1, 2, 3]
  ```

---

### **Nombrado**

* Variables y funciones: **snake\_case** (letras minúsculas y guiones bajos).

  ```python
  numero_total = 10
  def calcular_suma(a, b):
      return a + b
  ```
* Clases: **CamelCase** (Primera letra de cada palabra en mayúsculas).

  ```python
  class MiClase:
      pass
  ```
* Constantes: **MAYÚSCULAS\_CON\_GUIONES\_BAJOS**.

  ```python
  PI = 3.14159
  ```

---

### **Cadenas**

* Usa comillas simples (`'`) o dobles (`"`) para cadenas. Sé consistente en su uso.
* Para cadenas largas, utiliza triples comillas (`'''` o `"""`).

---

## **2. Importaciones**

* Agrupa importaciones en el siguiente orden:

  1. Librerías estándar.
  2. Librerías de terceros.
  3. Módulos locales o del proyecto.
* Usa una línea por cada módulo importado:

  ```python
  import os
  import sys

  from django.conf import settings
  ```

---

## **3. Comentarios**

* Comenta el **porqué** y no solo el **qué**.
* Usa comentarios claros y concisos:

  ```python
  # Este bucle calcula el total
  for i in range(10):
      total += i
  ```

---

## **4. Documentación (Docstrings)**

* Usa **docstrings** para describir módulos, clases y funciones.

  ```python
  def sumar(a, b):
      """
      Suma dos números.

      Args:
          a (int): Primer número.
          b (int): Segundo número.

      Returns:
          int: La suma de a y b.
      """
      return a + b
  ```

---

## **5. Buenas Prácticas**

* Usa `if __name__ == "__main__":` para definir el punto de entrada principal.

  ```python
  if __name__ == "__main__":
      print("Hola, mundo")
  ```
* Usa variables significativas y descriptivas:

  ```python
  # Correcto
  velocidad_media = distancia / tiempo
  # Incorrecto
  x = d / t
  ```

---
