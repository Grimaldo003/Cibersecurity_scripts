# Ejecutar el script de Bash
import subprocess

process = subprocess.run(['./monitor_conexiones.sh'], capture_output=True, text=True, shell=True)


print(f"""Salida de comando: 
        
        {process.stdout}

        """)
