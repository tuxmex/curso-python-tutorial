# 🤖 Ejercicio 04.1 – Asistente Personal de Decisiones

Este ejercicio tiene como objetivo fortalecer el uso de **estructuras condicionales `if`, `elif`, `else`** en Python mediante la creación de un sistema inteligente que analiza múltiples factores personales para sugerir actividades o diagnósticos.

---

## 🎯 Objetivo

Desarrollar un asistente que tome decisiones simuladas según el **clima, dinero, humor, energía y hora**, utilizando condicionales anidadas, operadores lógicos y flujos complejos de decisión.

---

## 📁 Archivos del proyecto

| Archivo                              | Descripción                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| `asistente_decisiones.py`           | Código completo del asistente que sugiere actividades según tu contexto.   |
| `sistema_calificaciones.py`         | Convierte calificaciones numéricas en letras con mensajes motivacionales.  |
| `calculadora_descuentos.py`         | Calcula descuentos según monto, día, edad y cliente frecuente.             |
| `recomendador_peliculas.py`         | Recomienda películas con base en género, estado de ánimo y compañía.       |
| `diagnostico_pc.py`                 | Diagnóstico básico por árbol de decisión de fallas comunes en una PC.      |

---

## 💻 Instrucciones de ejecución

1. Clona el repositorio:
```bash
git clone https://github.com/tuxmex/curso-python-tutorial.git
cd curso-python-tutorial/src/module_1/ejercicios_04
````

2. Ejecuta cualquier archivo con Python:

```bash
python asistente_decisiones.py
```

---

## 🧠 Conceptos clave

* `if / elif / else` para condiciones múltiples
* Uso de `and`, `or`, `not` para construir lógica compleja
* Anidamiento de decisiones (if dentro de if)
* Buenas prácticas: orden lógico, comentarios, cláusula `else` final
* Función `input()` y validación de datos

---

## 📌 Ejercicios incluidos

### ✔️ Asistente de Decisiones

Simula un asistente virtual que, según tus respuestas, te sugiere:

* Ir al parque, descansar, ejercitarte, socializar, etc.
* Evalúa clima, dinero, energía, humor y hora actual

### ✔️ Sistema de Calificaciones

Convierte calificaciones 0-100 en letras (A, B, C, D, F) y muestra mensajes personalizados.

### ✔️ Calculadora de Descuentos

Evalúa condiciones combinadas:

* Descuento por monto, día, edad y tipo de cliente

### ✔️ Recomendador de Películas

Sugiere películas con base en:

* Género preferido, tiempo libre, estado de ánimo y compañía

### ✔️ Diagnóstico de PC (Desafío Extra)

Árbol de decisión que responde a preguntas comunes para diagnosticar fallas:

* ¿Enciende?, ¿pantalla?, ¿ruidos?, ¿última vez funcional?

---

## ✅ Buenas prácticas reforzadas

* Usar condiciones específicas antes que generales
* Evitar redundancias lógicas
* Usar `elif` en lugar de muchos `if`
* Comentar bloques complejos
* Aplicar `print("DEBUG: ...")` para depurar

---

## 📚 Recursos relacionados

* [Documentación oficial Python sobre estructuras condicionales](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
* [Curso Python de TuxMex](https://tuxmex.github.io/curso-python-tutorial/)

---

## 📜 Licencia

Este ejercicio es parte del proyecto educativo [curso-python-tutorial](https://github.com/tuxmex) y está bajo la licencia MIT.
