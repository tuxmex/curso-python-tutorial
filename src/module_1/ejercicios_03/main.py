from detector_magico import detectar_numero_magico

def mostrar_resultado(numero, nivel, razones):
    print("\n" + "=" * 40)
    if nivel >= 100:
        print("🌟✨🔮 ¡NÚMERO LEGENDARIO! 🔮✨🌟")
    elif nivel >= 50:
        print("✨ ¡NÚMERO MUY MÁGICO! ✨")
    elif nivel > 0:
        print("🌙 Número con propiedades mágicas")
    else:
        print("😔 Número ordinario")
    print(f"Nivel de magia: {nivel} puntos")
    if razones:
        print("📜 Razones:")
        for r in razones:
            print(f" - {r}")
    print("=" * 40)

def main():
    print("🔮 BIENVENIDO AL DETECTOR DE NÚMEROS MÁGICOS 🔮")
    while True:
        try:
            numero = int(input("\nIngresa un número o 0 para salir: "))
            if numero == 0:
                print("¡Hasta la próxima!")
                break
            nivel, razones = detectar_numero_magico(numero)
            mostrar_resultado(numero, nivel, razones)
        except ValueError:
            print("❌ Entrada inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
