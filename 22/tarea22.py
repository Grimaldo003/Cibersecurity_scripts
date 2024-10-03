
"""
Tarea 22/ Prgramación para Ciberseguridad
Integrantes del equipo:
José Silva Grimaldo 2049762
Andrés Espinoza Galindo 2120658

"""


import six, getpass, argparse, sys
from tarea21_haveibeenpwn import * 

try:
    if six.PY3==True:  


        print(f"""
            \n
            \t Está ejecuntado en PYTHON 3
            \n
            """)
except:

    print(f"""
          \n\t¡¡¡Su código no es comaptible con este lenguaje de programación!!!\n
          
          Puede ser que sea Python 2
          """)


key_segura = getpass.getpass("Ingrese la clave de la API: ")
    
    
if key_segura == key:
    print(f"Clave correcta\n")
else:
    print(f"Clave incorrecta\n")
    
    
def input_e():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, help="Ingrese el correo a investigar")
    args=parser.parse_args()
    sys.stdout.write(str(email_r(args)))


def email_r(args):
    args.email
    return email

input_e()


    
    



