# tienda_mascotas.py
# === LA TIENDA DE MASCOTAS VIRTUALES ===

print("🐾 BIENVENIDO A LA TIENDA DE MASCOTAS VIRTUALES 🐾")
print("=" * 50)

# Datos básicos de la mascota (diferentes tipos)
nombre_mascota = "Pyto"  # string
tipo_mascota = "Perro Python"  # string
edad_meses = 6  # int
peso_kg = 2.5  # float
esta_feliz = True  # boolean
esta_vacunado = True  # boolean
colores = ["dorado", "blanco"]  # lista
juguetes_favoritos = ["pelota", "hueso", "cuerda"]  # lista

# Mostrar la información de la mascota
print("\n📋 FICHA DE LA MASCOTA:")
print("-" * 30)
print("Nombre:", nombre_mascota)
print("Tipo:", tipo_mascota)
print("Edad:", edad_meses, "meses")
print("Peso:", peso_kg, "kg")
print("¿Está feliz?", esta_feliz)
print("¿Está vacunado?", esta_vacunado)
print("Colores:", colores)
print("Juguetes favoritos:", juguetes_favoritos)

# Información adicional usando los datos
print("\n🎯 INFORMACIÓN ADICIONAL:")
print("-" * 30)

# Edad en años
edad_anos = edad_meses / 12
print(f"Edad en años: {edad_anos:.1f} años")

# Número de juguetes
numero_juguetes = len(juguetes_favoritos)
print(f"Cantidad de juguetes: {numero_juguetes}")

# Estado de salud
if esta_vacunado and esta_feliz:
    print("Estado: ¡Mascota saludable y feliz! ✨")
else:
    print("Estado: Necesita atención")

print("\n¡Gracias por visitar nuestra tienda! 🐾")
