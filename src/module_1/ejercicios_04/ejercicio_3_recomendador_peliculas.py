# Recomendador de Películas
print("🎬 RECOMENDADOR DE PELÍCULAS PERSONALIZADO")
print("=" * 40)

genero = input("¿Qué género prefieres? (acción, comedia, drama, terror, ciencia ficción): ").lower()
estado_animo = input("¿Cómo te sientes hoy? (feliz, triste, aburrido, relajado): ").lower()
acompanado = input("¿Estás solo/a o acompañado/a? (solo/acompañado): ").lower()
tiempo = int(input("¿Cuántos minutos disponibles tienes?: "))
visto_populares = input("¿Ya viste las películas más populares? (s/n): ").lower() == "s"

print("\n🎥 RECOMENDACIÓN:")
# Lógica básica de recomendación
if genero == "comedia" and estado_animo in ["triste", "aburrido"]:
    print("🍿 Mira 'Forrest Gump' o 'La vida es bella' para mejorar tu ánimo.")
elif genero == "acción" and tiempo >= 120:
    print("💥 Prueba con 'Mad Max: Fury Road' o 'Inception'.")
elif genero == "drama" and acompañado == "solo":
    print("🎭 'El curioso caso de Benjamin Button' te hará reflexionar.")
elif genero == "terror" and acompañado == "acompañado":
    print("👻 'El Conjuro' o 'A Quiet Place' son ideales para una noche de miedo.")
elif genero == "ciencia ficción" and not visto_populares:
    print("🚀 Mira 'Interstellar' o 'Ex Machina', te volarán la mente.")
else:
    print("🎞️ Te recomendamos revisar el catálogo de Netflix o Prime según tu estado de ánimo.")
