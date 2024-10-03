#Integrantes del equipo
# Carlos Alexis Vargas Flores 
# ANDRES ESPINOZA GALINDO
#José Silva Grimaldo

import openpyxl, subprocess, os, csv
from openpyxl import Workbook



# ruta al script de powershel

ruta =  os.getcwd() + "\monitor_servicios.ps1"


try:
    # Ejecutar el script de PowerShell y capturar la salida
    result = subprocess.run(["powershell", "-File", ruta], capture_output=True, text=True)
    

    # Comprobar si hubo errores en la ejecución
    if result.returncode == 0:
        print("Script de PowerShell ejecutado con éxito.")
        print("Salida del script:")
        print(result.stdout)  # Mostrar la salida


        #CSV a Excel
        csv_file = "EXPORTSERVICE.csv"
        excel_file = "SERVICIOS.xlsx"

        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)

            # Saltar la primera fila si contiene los nombres de las columnas
            next(reader)
            
            data = list(reader)

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Escribir los encabezados (si no están en el CSV)
        sheet.append(["Nombre", "DisplayName", "Status", "StartType"])

        for row in data:
            sheet.append(row)

        workbook.save(excel_file)



        
        

    else:
        print("Error en la ejecución del script de PowerShell.")
        print("Error:", result.stderr)  # Mostrar el error estándar

except ValueError and Exception as e:
    print(f"Ocurrió un error: {e}")
    print(f"----{ValueError}----")





#FUENTES
#https://www.delftstack.com/howto/powershell/python-powershell/
#https://powershellcommands.com/python-run-powershell-command
#https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3
#https://j2logo.com/python/crear-archivo-excel-en-python-con-openpyxl/
#https://j2logo.com/como-concatenar-y-formatear-strings/
#https://www.geeksforgeeks.org/working-with-excel-spreadsheets-in-python/
