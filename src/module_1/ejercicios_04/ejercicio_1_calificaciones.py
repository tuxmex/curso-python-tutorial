# Sistema de Calificaciones
print("🎓 SISTEMA DE CALIFICACIONES")
print("=" * 40)

try:
    nota = int(input("Ingresa la calificación (0-100): "))
    if nota < 0 or nota > 100:
        print("❌ La calificación debe estar entre 0 y 100.")
    else:
        if nota >= 90:
            print("Calificación: A - Excelente 🎉")
            print("¡Sigue así, eres un ejemplo!")
        elif nota >= 80:
            print("Calificación: B - Muy bien 😊")
            print("¡Buen trabajo, puedes llegar más alto!")
        elif nota >= 70:
            print("Calificación: C - Bien 👍")
            print("¡Puedes mejorar con un poco más de esfuerzo!")
        elif nota >= 60:
            print("Calificación: D - Suficiente 😐")
            print("¡Vamos, un poco más de dedicación!")
        else:
            print("Calificación: F - Insuficiente 😔")
            print("No te rindas. Aprende del error y sigue adelante.")
except ValueError:
    print("❌ Entrada inválida. Ingresa un número entero.")
