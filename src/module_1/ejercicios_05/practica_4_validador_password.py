import string

def tiene_longitud_minima(password, min_length=8):
    return len(password) >= min_length

def tiene_mayusculas(password):
    return any(char.isupper() for char in password)

def tiene_numeros(password):
    return any(char.isdigit() for char in password)

def tiene_caracteres_especiales(password):
    especiales = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"
    return any(char in especiales for char in password)

def es_password_segura(password):
    return (
        tiene_longitud_minima(password)
        and tiene_mayusculas(password)
        and tiene_numeros(password)
        and tiene_caracteres_especiales(password)
    )

# Ejemplo
clave = "Contrasena123!"
if es_password_segura(clave):
    print("✅ La contraseña es segura.")
else:
    print("❌ La contraseña no cumple con todos los criterios.")
