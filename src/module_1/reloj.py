# reloj.py

import time
import os
import platform
from datetime import datetime

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_reloj():
    try:
        while True:
            ahora = datetime.now()
            hora_str = ahora.strftime("%H:%M:%S")
            limpiar_pantalla()
            print("Hora actual:", hora_str)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReloj detenido.")

if __name__ == "__main__":
    mostrar_reloj()
