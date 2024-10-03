#!/usr/bin/env python3

"""
INTEGRANTES:
#ANDRÉS ESPINOZA 2120658
#JOSÉ SILVA GRIMALDO 2049762
#RAUL CARDENAS IBARRA 1992943
"""

import subprocess, re
try:
	puertos_estandar = {22, 25, 80, 465, 587, 8080}

	def ejecutar_script_bash(script):
	    try:
	        resultado = subprocess.run(['bash', script], capture_output=True, text=True, check=True)
	        return resultado.stdout
	    except subprocess.CalledProcessError as e:
	        print(f"Error al ejecutar el script de Bash: {e}")
	        return None

	def analizar_conexiones(salida):
	    conexiones_sospechosas = []
	    lineas = salida.splitlines()

	    for linea in lineas:
	        # Usar una expresión regular para extraer la dirección y puerto
	        coincidencia = re.search(r'(\d+\.\d+\.\d+\.\d+:\d+)', linea)
	        if coincidencia:
	            puerto = int(coincidencia.group().split(':')[-1])
	            if puerto not in puertos_estandar:
	                conexiones_sospechosas.append(linea)

	    return conexiones_sospechosas

	def guardar_reporte(conexiones_sospechosas):
	    with open('reporte_conexiones_sospechosas.txt', 'w') as archivo:
	        for conexion in conexiones_sospechosas:
	            archivo.write(conexion + '\n')

	# Ejecutar el script de Bash y analizar las conexiones
	script_bash = '/home/kali/monitor_conexiones.sh'
	salida = ejecutar_script_bash(script_bash)

	if salida is not None:
	    conexiones_sospechosas = analizar_conexiones(salida)
	    guardar_reporte(conexiones_sospechosas)
	    print("Análisis completado. Revisa 'reporte_conexiones_sospechosas.txt' para más detalles.")

except ValueError:

	print(f"""

	{ValueError}


	""")
