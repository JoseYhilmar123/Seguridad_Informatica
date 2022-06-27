import encriptacion
from os import listdir
from os.path import isfile,join


encriptacion.generarClave()
clave=encriptacion.cargarClave()

ruta = r'/home/jose/Escritorio/prueba1'

def listar(ruta):
    archivo = [a for a in listdir(ruta) if isfile(join(ruta,a)) if a.endswith('txt')]
    return archivo
listado_archivos = listar(ruta)

menuprincipal = int(input("Menu principal\n1.\t Ver Archivos\n2.\t Crear - Editar archivos\n3.\t Encriptar Archivos\n4.\t Desencriptar archivos\n0. \t Salir del Programa\n "))

while menuprincipal != 0:
    if menuprincipal == 1:
        
        print(listado_archivos)
        a = input("Seleccione archivo a leer: ")
        encriptacion.abrir(a)
    elif menuprincipal == 2:
        opcion = input ("Ingresa un nuevo archivo ")    
        linea = input("Texto a agregar:")
        encriptacion.crear(linea, opcion)
    elif menuprincipal == 3:
        
        print(listado_archivos)
        opcion = input('Elija el archivo que desee encriptar: ')
        if opcion == 'archivo1.txt':
            encriptacion.encriptar(opcion,clave)
            print("Archivo encriptado, el texto es: ")
            encriptacion.abrir(opcion) 
        if opcion == listado_archivos:
            encriptacion.encriptar(opcion,clave)
            print("Archivo encriptado, el texto es: ")
            encriptacion.abrir(opcion) 
        if opcion == 'archivo3.txt':
            encriptacion.encriptar(opcion,clave)
            print("Archivo encriptado, el texto es: ")
            encriptacion.abrir(opcion) 


    elif menuprincipal == 4:
        print(listado_archivos)
        archivo = input('Elija el archivo que desee desencriptar: ')
        if archivo == 'archivo1.txt':
            encriptacion.desencriptar(archivo,clave)
            print("Archivo desencriptado, el texto es: ")
            encriptacion.abrir(archivo)
        if archivo == 'archivo2.txt':
            encriptacion.desencriptar(archivo,clave)
            print("Archivo desencriptado, el texto es: ")
            encriptacion.abrir(archivo)
        if archivo == 'archivo3.txt':
            encriptacion.desencriptar(archivo,clave)
            print("Archivo desencriptado, el texto es: ")
            encriptacion.abrir(archivo)
    else:
        print('Digite una opcion correcta')

    menuprincipal = int(input("Menu principal\n1.\t Ver Archivos\n2.\t Crear - Editar archivos\n3.\t Encriptar Archivos\n4.\t Desencriptar archivos\n0. \t Salir del Programa\n "))
else:
    print('Salimos del programa')