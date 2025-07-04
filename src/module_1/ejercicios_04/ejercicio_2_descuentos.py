# Calculadora de Descuentos
print("💰 CALCULADORA DE DESCUENTOS INTELIGENTE")
print("=" * 40)

# Entrada de datos
monto = float(input("Monto total de la compra: $"))
dia = input("Día de la semana: ").lower()
cliente_frecuente = input("¿Es cliente frecuente? (s/n): ").lower() == "s"
edad = int(input("Edad del cliente: "))

descuento = 0

# Descuento por volumen
if monto >= 1000:
    descuento += 15
elif monto >= 500:
    descuento += 10
elif monto >= 200:
    descuento += 5

# Descuentos por día
if dia in ["martes", "miércoles"]:
    descuento += 5

# Cliente frecuente
if cliente_frecuente:
    descuento += 5

# Edad (estudiantes o jubilados)
if edad <= 25 or edad >= 60:
    descuento += 10

# Calcular monto final
descuento_total = monto * (descuento / 100)
total_pagar = monto - descuento_total

print(f"\nDescuento aplicado: {descuento}%")
print(f"Total a pagar: ${total_pagar:.2f}")
