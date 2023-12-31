#Librerías
import random
import pprint as pp
import json
import urllib.request

#Definición de funciones
def generarCasoCSP():
    coleccionServicios = []
    
    #Generación aleatoria de servicios
    numeroServicios = 20
    cuatroAM = 240 #Minutos
    diezPM = 1320 #Minutos
    for i in range(numeroServicios):
        t0 = random.randint(cuatroAM,diezPM-16)
        while True:
            tf = random.randint(t0,diezPM)
            if tf > t0 and tf-t0 <= 180 and tf-t0 > 15:
                servicio = {
                    'codigo': i,
                    't0':t0,
                    'tf':tf,
                    'duracion':tf-t0
                }
                coleccionServicios.append(servicio)
                break    
    return coleccionServicios
    


#Caso de estudio de asignación
#Caso 1
coleccionServicios = [
    {'codigo': 0, 'duracion': 66, 't0': 1100, 'tf': 1166},
    {'codigo': 1, 'duracion': 103, 't0': 915, 'tf': 1018},
    {'codigo': 2, 'duracion': 68, 't0': 1024, 'tf': 1092},
    {'codigo': 3, 'duracion': 97, 't0': 749, 'tf': 846},
    {'codigo': 4, 'duracion': 82, 't0': 1055, 'tf': 1137},
    {'codigo': 5, 'duracion': 133, 't0': 620, 'tf': 753},
    {'codigo': 6, 'duracion': 153, 't0': 879, 'tf': 1032},
    {'codigo': 7, 'duracion': 160, 't0': 538, 'tf': 698},
    {'codigo': 8, 'duracion': 144, 't0': 299, 'tf': 443},
    {'codigo': 9, 'duracion': 90, 't0': 714, 'tf': 804},
    {'codigo': 10, 'duracion': 45, 't0': 1005, 'tf': 1050},
    {'codigo': 11, 'duracion': 73, 't0': 514, 'tf': 587},
    {'codigo': 12, 'duracion': 81, 't0': 914, 'tf': 995},
    {'codigo': 13, 'duracion': 83, 't0': 341, 'tf': 424},
    {'codigo': 14, 'duracion': 57, 't0': 335, 'tf': 392},
    {'codigo': 15, 'duracion': 179, 't0': 657, 'tf': 836},
    {'codigo': 16, 'duracion': 49, 't0': 432, 'tf': 481},
    {'codigo': 17, 'duracion': 55, 't0': 1230, 'tf': 1285},
    {'codigo': 18, 'duracion': 21, 't0': 636, 'tf': 657},
    {'codigo': 19, 'duracion': 66, 't0': 1122, 'tf': 1188,
     'personas': ['Aldo','Maria','Ana']}
 ]

#Generar un archivo con la información de la colección
rutaArchivo = "json/caso1Servicios.json"



# #Mientras el archivo esté abierto
# with open(rutaArchivo,"w") as f:
    
#     #Descargar información en el archivo
#     for i,servicio in enumerate(coleccionServicios):
#         linea = str()
#         linea += str(servicio['codigo']) + " "
#         linea += str(servicio['duracion']) + " "
#         linea += str(servicio['t0']) + " "
#         linea += str(servicio['tf']) + "\n"
#         f.write(linea)

# print("Instrucciones posteriores al cierre del archivo")

# #Lectura del archivo generado
# coleccionDesdeArchivo = list()
# rutaRecurso = "recursos/loteServicios.txt"
# # rutaRecurso = "loteServicios.txt"


#Generar archivo json del contenedor o ED de nuestros servicios
# try:
#     with open(rutaArchivo,"w") as f:
#         json.dump(coleccionServicios,f)
# except FileNotFoundError:
#     print("Error en la ruta para almacenar el archivo!!!")
    


# try: 
    
#     with open(rutaRecurso,"r") as f:
#         for linea in f.readlines():
#             linea = linea.strip()
#             registro = linea.split(" ")
#             servicio = {
#                     'codigo': int(registro[0]), 
#                     'duracion': int(registro[1]),  
#                     't0': int(registro[2]), 
#                     'tf': int(registro[3]) 
#             }
#             coleccionDesdeArchivo.append(servicio)
            
# except FileNotFoundError:
#     print("Archivo no encontrado!!! Generando set aleatorio")
#     coleccionDesdeArchivo = generarCasoCSP()
#     print("Fin de caso alterno")


# print("Contenido cargado desde el archivo:")
# pp.pprint(coleccionDesdeArchivo)

#Cargar un archivo JSON en memoria o en ED -> Procesamiento
coleccionDesdeEndpoint = None
sitio = "https://www.datos.gov.co/resource/ffwn-j5cw.json"
try:
    with urllib.request.urlopen(sitio) as url:
        coleccionDesdeEndpoint=json.loads(url.read().decode())
except:
    print("Error en el request!!!")

print(f"Tipo de la ED -> {type(coleccionDesdeEndpoint)}")
pp.pprint(coleccionDesdeEndpoint)

conjuntoMunicipios = set()
for i,registro in enumerate(coleccionDesdeEndpoint):
    conjuntoMunicipios.add(registro['nombre_de_la_zona_wifi'])
    
print(f"No Barrios -> {len(conjuntoMunicipios)}")
pp.pprint(conjuntoMunicipios)

#Generar archivo json del contenedor o ED de nuestros servicios
try:
    with open("json/puntosWifi.json","w") as f:
        json.dump(coleccionDesdeEndpoint,f)
except FileNotFoundError:
    print("Error en la ruta para almacenar el archivo!!!")
 
        
        
    












