from cryptography.fernet import Fernet
from pathlib import Path 
from os import listdir

ruta = r'/home/jose/Escritorio/prueba1'

#from matplotlib.pyplot import cla
def generarClave():
    archivo = r'llave.key'
    objeto = Path(archivo)
    if not objeto.is_file():
        clave = Fernet.generate_key()

        with open("llave.key", "wb") as key_file:
            key_file.write(clave)

def cargarClave():
    return open("llave.key","rb").read()

# ENCRIPTACION Y DESENCRIPTACION 

def encriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo,"rb") as file:
        mensaje = file.read()

    datos_encriptados = f.encrypt(mensaje)
    with open(archivo, "wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo,"rb") as file:
        mensaje_encriptado = file.read()

    datos = f.decrypt(mensaje_encriptado)

    with open(archivo,"wb") as file:
        file.write(datos)

# MANEJO DE ARCHIVOS
def abrir(archivo):
    a = open(archivo,"rt", encoding="utf-8")
    print()
    print(a.read())
    print()

def crear(linea, archivos):
    with open(archivos, 'a') as file: # a = append crea o edita en el caso de que exista
        file.write("\n"+linea)






            
