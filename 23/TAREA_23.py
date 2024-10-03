"""
INTEGRANTES:
#ANDRÉS ESPINOZA 2120658
#JOSÉ SILVA GRIMALDO 2049762
#RAUL CARDENAS IBARRA 1992943
"""

import pyautogui as pt
import subprocess
import datetime as dt

try:
    im = pt.screenshot()
    fecha = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre = r'SCREENSHOT'+fecha
    nombre +='.png'
    im.save(nombre)
    print(f"Captura de pantalla guardada como: {nombre+fecha}")
except Exception as e:
    print(f"Error al capturar la pantalla: {e}")

try:
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"process_list_{timestamp}.txt"
    result = subprocess.run(["tasklist"], capture_output=True, text=True, shell=True)

    if result.returncode == 0:
        with open(output_filename, "w") as file:
            file.write(result.stdout)
        print(f"Lista de procesos guardada como: {output_filename}")
    else:
        print(f"Error al obtener la lista de procesos: {result.stderr}")
except Exception as e:
    print(f"Error al ejecutar el comando: {e}")
