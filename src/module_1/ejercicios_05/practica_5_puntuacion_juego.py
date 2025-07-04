puntos = {}

def calcular_puntos(acciones_realizadas):
    return sum(acciones_realizadas.values())

def aplicar_multiplicador(puntos, multiplicador):
    return puntos * multiplicador

def guardar_record(nombre, puntos_totales):
    puntos[nombre] = puntos_totales

def mostrar_tabla_posiciones():
    print("🏆 Tabla de Posiciones")
    for jugador, puntaje in sorted(puntos.items(), key=lambda x: x[1], reverse=True):
        print(f"{jugador}: {puntaje} pts")

def mensaje_felicitacion(puntaje):
    if puntaje >= 1000:
        return "🌟 ¡Eres una leyenda!"
    elif puntaje >= 500:
        return "🔥 ¡Gran desempeño!"
    elif puntaje >= 100:
        return "👍 ¡Bien hecho!"
    else:
        return "Sigue intentando..."

# Ejemplo de uso
acciones = {"enemigos_derrotados": 100, "monedas": 200, "misiones": 150}
puntaje_base = calcular_puntos(acciones)
puntaje_final = aplicar_multiplicador(puntaje_base, 1.5)
guardar_record("Jugador1", puntaje_final)

mostrar_tabla_posiciones()
print(mensaje_felicitacion(puntaje_final))
