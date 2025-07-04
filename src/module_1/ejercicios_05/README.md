
# 🐍 Ejercicios Prácticos - Módulo 5: Funciones en Python

Este repositorio contiene ejercicios y prácticas del módulo 5 del curso **"Fundamentos de Python"**, centrado en el uso y dominio de **funciones**. Los ejercicios buscan aplicar buenas prácticas como reutilización de código, modularidad y legibilidad.

---

## 📁 Estructura de Archivos

| Archivo                                | Descripción |
|----------------------------------------|-------------|
| `ejercicio1_generador_historias.py`   | Generador de historias cortas personalizadas usando funciones. |
| `ejercicio2_calculadora_propinas.py`  | Calculadora de propinas reutilizable. |
| `ejercicio3_validador_contrasenas.py` | Validador de contraseñas con criterios de seguridad. |
| `desafio_extra_sistema_puntuacion.py` | Sistema de puntuación para juegos con funciones avanzadas. |

---

## 📌 Ejercicios Incluidos

### ✅ Ejercicio 1: Generador de Historias

**Objetivo:** Crear funciones que generen partes de una historia y construirla de forma dinámica.

**Funciones:**

- `generar_inicio(nombre, lugar)`
- `generar_desarrollo(conflicto)`
- `generar_final(resolucion)`
- `generar_historia(nombre, lugar, conflicto, resolucion)`

📎 Ejemplo:
```python
print(generar_historia("María", "el bosque", "un dragón", "usó su ingenio para calmarlo"))
````

---

### 💰 Ejercicio 2: Calculadora de Propinas

**Objetivo:** Crear funciones reutilizables para cálculos financieros simples.

**Funciones:**

* `calcular_propina(total, porcentaje)`
* `dividir_cuenta(total, personas)`
* `formatear_dinero(cantidad)`
* `sugerir_propina(calidad_servicio)`

📎 Ejemplo:

```python
propina = calcular_propina(500, sugerir_propina("excelente"))
```

---

### 🔒 Ejercicio 3: Validador de Contraseñas

**Objetivo:** Validar contraseñas seguras con múltiples criterios.

**Funciones:**

* `tiene_longitud_minima(password, min_length)`
* `tiene_mayusculas(password)`
* `tiene_numeros(password)`
* `tiene_caracteres_especiales(password)`
* `es_password_segura(password)`

📎 Ejemplo:

```python
print(es_password_segura("ClaveFuerte123!"))
```

---

### 🎮 Desafío Extra: Sistema de Puntuación

**Objetivo:** Simular el sistema de puntuación de un juego.

**Funciones:**

* `calcular_puntos(accion)`
* `aplicar_multiplicador(puntos, nivel)`
* `guardar_record(jugador, puntos)`
* `mostrar_tabla_posiciones(records)`
* `mensaje_felicitacion(puntos)`

📎 Ejemplo:

```python
print(mensaje_felicitacion(180))
```

---

## 🛠 Requisitos

* Python 3.7 o superior
* No requiere librerías externas

---

## 🧠 Recomendaciones

* Cada archivo puede ejecutarse de forma independiente.
* Puedes extender las funciones con tus propias ideas.
* Asegúrate de probar diferentes entradas y condiciones para comprender mejor su funcionamiento.

---

## 📚 Aprendizajes Clave

✅ Reutilización de código
✅ Modularidad y funciones personalizadas
✅ Separación lógica entre entrada, procesamiento y salida
✅ Pruebas y validación de funciones

---

## ✨ Autor

[Anastacio Rodríguez García](https://github.com/tuxmex) como parte del curso de Python para aplicaciones industriales y académicas.

