def generar_inicio(nombre, lugar, criatura):
    return f"Había una vez una persona llamada {nombre} que vivía cerca de un misterioso {lugar}."

def generar_desarrollo(nombre, lugar, criatura):
    return f"Un día, {nombre} decidió explorar el {lugar} y se encontró con un {criatura} que custodiaba un secreto antiguo."

def generar_final(nombre, criatura):
    return f"Después de una gran aventura, {nombre} hizo amistad con el {criatura} y juntos protegieron el bosque por siempre."

def generar_historia(nombre, lugar, criatura):
    inicio = generar_inicio(nombre, lugar, criatura)
    desarrollo = generar_desarrollo(nombre, lugar, criatura)
    final = generar_final(nombre, criatura)
    return f"{inicio}\n{desarrollo}\n{final}"

# Ejemplo
print(generar_historia("María", "bosque encantado", "dragón"))
