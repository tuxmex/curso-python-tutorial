def calcular_propina(total, porcentaje):
    return total * (porcentaje / 100)

def dividir_cuenta(total, personas):
    if personas == 0:
        return 0
    return total / personas

def formatear_dinero(cantidad):
    return "${:,.2f}".format(cantidad)

def sugerir_propina(calidad_servicio):
    calidad_servicio = calidad_servicio.lower()
    if calidad_servicio == "excelente":
        return 20
    elif calidad_servicio == "buena":
        return 15
    elif calidad_servicio == "regular":
        return 10
    else:
        return 5

# Ejemplo
total = 250
porcentaje = sugerir_propina("buena")
propina = calcular_propina(total, porcentaje)
total_con_propina = total + propina
print("Propina sugerida:", formatear_dinero(propina))
print("Total a pagar:", formatear_dinero(total_con_propina))
print("Cada uno paga:", formatear_dinero(dividir_cuenta(total_con_propina, 3)))
