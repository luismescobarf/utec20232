#Abrir archivo de texto (BD, fuente externa info)
rutaArchivo = "archivoTexto.txt"

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
