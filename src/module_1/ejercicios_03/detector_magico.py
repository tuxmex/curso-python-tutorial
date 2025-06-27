from funciones_magicas import (
    es_numero_perfecto, es_numero_primo, suma_digitos
)

def detectar_numero_magico(numero):
    print(f"\n🔮 ANALIZANDO EL NÚMERO {numero}...")
    print("=" * 40)

    es_par = numero % 2 == 0
    es_multiplo_3 = numero % 3 == 0
    es_multiplo_5 = numero % 5 == 0
    es_multiplo_7 = numero % 7 == 0
    es_primo = es_numero_primo(numero)
    es_perfecto = es_numero_perfecto(numero)
    suma_dig = suma_digitos(numero)
    suma_dig_es_par = suma_dig % 2 == 0

    print(f"✓ ¿Es par? {es_par}")
    print(f"✓ ¿Es múltiplo de 3? {es_multiplo_3}")
    print(f"✓ ¿Es múltiplo de 5? {es_multiplo_5}")
    print(f"✓ ¿Es múltiplo de 7? {es_multiplo_7}")
    print(f"✓ ¿Es primo? {es_primo}")
    print(f"✓ ¿Es perfecto? {es_perfecto}")
    print(f"✓ Suma de dígitos: {suma_dig} (par: {suma_dig_es_par})")

    nivel_magia = 0
    razones = []

    if es_perfecto:
        nivel_magia += 100
        razones.append("¡Es un número PERFECTO! ✨")
    if es_primo:
        nivel_magia += 50
        razones.append("Es un número primo 🌟")
    if es_par and es_multiplo_3 and numero > 50:
        nivel_magia += 30
        razones.append("Es par, múltiplo de 3 y mayor que 50")
    if es_multiplo_5 and es_multiplo_7:
        nivel_magia += 25
        razones.append("Es múltiplo de 5 y 7")
    if suma_dig in [7, 11, 13]:
        nivel_magia += 20
        razones.append("Suma de dígitos mística")
    if not es_par and es_multiplo_3 and suma_dig_es_par:
        nivel_magia += 15
        razones.append("Impar, múltiplo de 3 y suma de dígitos par")
    if numero in [7, 13, 42, 69, 420, 666, 777]:
        nivel_magia += 40
        razones.append("Número culturalmente mágico")

    return nivel_magia, razones
