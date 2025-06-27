# ejercicio_3_calculadora_mascota.py
# Cálculos con datos de la mascota

edad_meses = 6
peso_kg = 2.5
costo_mensual = 350.0

dias_de_vida = edad_meses * 30
comida_al_ano = peso_kg * 365
gasto_anual = costo_mensual * 12

print("📊 Calculadora de Mascota")
print(f"Días de vida: {dias_de_vida} días")
print(f"Comida necesaria al año: {comida_al_ano:.1f} kg")
print(f"Gasto anual estimado: ${gasto_anual:.2f}")
