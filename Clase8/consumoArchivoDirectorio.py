#Abrir un archivo de un docente en la carpeta basesDatos



#Ruta relativa (mejor práctica)
rutaArchivo = "basesDatos/docentes/docentes20232.txt"
# rutaArchivo = "../../basesDatosPadre/docentes/docentes20232.txt" #Relativa carpeta padre
# rutaArchivo = "basesDatos\docentes\docentes20232.txt"#Windows

#Ruta absoluta
# rutaArchivo = "/Users/luismiguelescobarfalcon/Dropbox/ClasesUTEC2023/repoSesiones/Clase8/basesDatos/docentes/docentes20232.txt"


f = None

try:
    f = open(rutaArchivo)
except FileNotFoundError:
    print("El archivo no fue encontrado (revisar dir)")
else:
    contenido = f.read()
    print("---------Contenido del archivo----------")
    print(contenido)
    print("----------------------------------------")
finally:
    
    try:
        f.close()
    except AttributeError:
        print("Liberación de recurso no fue necesaria")

print("Otras instrucciones...")
print("Otras instrucciones...")
print("Otras instrucciones...")
