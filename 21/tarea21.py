import argparse, sys, getpass
from tarea21_haveibeenpwn import email
def input_e():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, help="Ingrese el correo a investigar")
    args=parser.parse_args()
    sys.stdout.write(str(email_r(args)))


def email_r(args):
    args.email
    return email

input_e()