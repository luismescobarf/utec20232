#Librerías
import pprint as pp
import random 
import matplotlib.pyplot as plt
import os
    

#Distancia Euclidiana
def distanciaEuclidiana(P1,P2):
    return  int(( (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 )**(1/2))

#Traducción de nombre a índice de la estructura de datos de nodos planteada
def traducirNombreIndice(nombrePunto,nodos):    
    for i,nodo in enumerate(nodos):
        if nombrePunto == nodo['Nombre']:
            return i
        
#Función para calcular distancia total de una ruta
def calcularDistancia(ruta,nodos,conexiones):
    distanciaTotal = 0
    strRuta = str()
    for i in range(len(ruta)-1): 
        nombrePartida = nodos[ ruta[i] ]['Nombre']
        nombreLlegada = nodos[ ruta[i+1] ]['Nombre']
        nombreConexion = nombrePartida + '-' + nombreLlegada
        
        # #Salida de diagnóstico
        # print("->",nombreConexion)
        
        #Acumular la conexión con las etiquetas originales
        strRuta += " ->"+nombreConexion
        
        distanciaTotal += conexiones[nombreConexion][2]
    
    return distanciaTotal,strRuta    

#Algoritmo para encontrar el recorrido para el TSP
#Vecino más cercano NN Nearest Neigborgh
def heuristicaNN_UnicoArranque(nodos,conexiones):

    #Esquema de una solución (incumbente)
    incumbente = {
        'nodoPartida': str(),
        'funcionObjetivo' : 99999,
        'ruta': [],
        'strRuta': str()
    }   
    
    #Punto de arranque fijo
    ii = 0
    
    #Establecer estructuras de control de los nodos que han sido cubiertos y los que no
    nodosCubiertos = set()
    nodosPendientes = set()
    for i in range(len(nodos)):
        nodosPendientes.add(i)
        
    #Inicialización -> Nodo ii
    nodoInicial = ii
    ruta = [nodoInicial]
    #Cubrir nodo inicial
    nodosCubiertos.add(nodoInicial)
    #Quitar el nodo inicial de los pendientes
    nodosPendientes.remove(nodoInicial)
    
    #Ciclo general del algoritmo
    while nodosPendientes != set():
    #while len(nodosPendientes) > 0:
        
        # #Salida de diagnóstico
        # print("-->Estado de la ruta")
        # pp.pprint(ruta)        
        
        #Último nodo cubierto -> Nodo actual
        nodoActual = ruta[-1]
        
        #Incumbente de posibles salidas
        incumbenteSalidas = (-1,-1,float('inf'))       
        
        #Calcular cada salida y revisar decidir si se realiza o no actualización de la incumbente
        for nodoPendiente in nodosPendientes:
            costoSalida = distanciaEuclidiana(
                (nodos[nodoActual]['x'],nodos[nodoActual]['y']),
                (nodos[nodoPendiente]['x'],nodos[nodoPendiente]['y']),
            )
            if costoSalida < incumbenteSalidas[-1]:
                incumbenteSalidas = (nodoActual,nodoPendiente,costoSalida)         
        
        
        # #Salida de diagnóstico
        # print("Salida ganadora: ")        
        # print(incumbenteSalidas)
        # input()
        
        
        #Traducir la mejor salida obtenida        
        indiceNodoSalida = incumbenteSalidas[1]
        ruta.append(indiceNodoSalida)
        nodosCubiertos.add(indiceNodoSalida)
        nodosPendientes.remove(indiceNodoSalida)
    
    #Completar la ruta
    ruta.append(nodoInicial)
    distanciaTotal, strRuta = calcularDistancia(ruta,nodos,conexiones)
    
    #Acumular la solución
    solucion = {
        'nodoPartida': nodos[ ruta[0] ]['Nombre'],
        'funcionObjetivo' : distanciaTotal,
        'ruta': ruta,
        'strRuta': strRuta
    }        
    
    #Retornar la solución en la estructura de datos preestablecida
    return solucion

#Cargar casos TSP de National TSPs
def cargarCasoTSP(rutaArchivo: str) -> list:
    
    
    # #Formato en el que quedará el caso que vamos a cargar
    
    # #Represntar red
    # nodos = [] #Permite asociar un id a cada uno de los elementos
    
    # nodos.append({'Nombre':'A','x':0,'y':0})
    # nodos.append({'Nombre':'B','x':10,'y':10})
    # nodos.append({'Nombre':'C','x':-10,'y':-3})
    # nodos.append({'Nombre':'D','x':-5,'y':8})
    # nodos.append({'Nombre':'E','x':11,'y':-2})
    # nodos.append({'Nombre':'Z','x':13,'y':5})
    
    #Contenedor para los nodos del archivo
    nodosArchivo = []
    
    try:
        with open(rutaArchivo,'r') as f:
            for i,linea in enumerate(f.readlines()):
                #Evitar las líneas del encabezado
                if i>= 7:
                    #Limpiando movimientos de carro y caracteres especiales
                    linea = linea.strip()
                    #Evitando el final de archivo que tienen las instancias
                    if linea != 'EOF':
                        registro = linea.split(" ")
                        nodosArchivo.append({
                            'Nombre': str(registro[0]),
                            'x': float(registro[1]),                         
                            'y': float(registro[2])                         
                        })     
    except FileNotFoundError:
        print(f"Error abriendo archivo: {rutaArchivo}")        
    
    #Retornando la red recibida
    return nodosArchivo    

def ejemploGraficadoMatplotlib():
    numeroPuntos = 10
    componentesX = list(range(10))      
    componentesY = []
    for i in range(numeroPuntos):
        componentesY.append(i**2)
        
    #Ejemplo básico de graficado matplotlib
    plt.plot(
        #Componentes en X
        componentesX,
        #Componentes en Y
        componentesY,
        #Estilo graficado
        'bs:'
    )
    
    #Guardarlo en un archivo (evitar sobreescrituras)
    nombreArchivo = "primerPlot"
    elementosCarpeta=os.listdir("./")
    # pp.pprint(elementosCarpeta)
    ocurrenciasNombreArchivo = 0
    for elemento in elementosCarpeta:
        if elemento.endswith(".png") and nombreArchivo in elemento:
            ocurrenciasNombreArchivo += 1   
    
    plt.savefig(nombreArchivo+str(ocurrenciasNombreArchivo+1)+'.png',bbox_inches='tight')
    
    #Mostrarlo en pantalla
    plt.show()
    
    
#Sección principal
##################

#Llamado ejemplo básico de graficado
ejemploGraficadoMatplotlib()
# input()


#Represntar red
nodos = [] #Permite asociar un id a cada uno de los elementos

# #Nodo a nodo adición en esa lista (dummie)
# nodos.append({'Nombre':'A','x':0,'y':0})
# nodos.append({'Nombre':'B','x':10,'y':10})
# nodos.append({'Nombre':'C','x':-10,'y':-3})
# nodos.append({'Nombre':'D','x':-5,'y':8})
# nodos.append({'Nombre':'E','x':11,'y':-2})
# nodos.append({'Nombre':'Z','x':13,'y':5})

#Cargar nodos desde archivo
nodos = cargarCasoTSP("uy734.tsp")

#Óptimo caso Uruguay
optimoCasoUY = 79114

#Salida de diagnóstico
print("-------------------------")
pp.pprint(nodos)
print("-------------------------")
# input()

# #Construir ED
# conexiones = [
#  ('A','B', distanciaAB),
#  ('A','D', distanciaAD),
#  .
#  .
#  .
#  ('E','D', distanciaED),
 
#  ]

# #Estructura de datos con el cálculo de las distancias
# #Esta información se calcula y no quiero que se modifique
# conexiones = []
# for i in range(len(nodos)):
#     for j in range(len(nodos)):
#         #Nodos diferentes (prevenir conexiones a un mismo nodo)
#         if i != j:
#             conexiones.append(  #Inicio de la tupla que será coleccionada en las conexiones
#                                 (nodos[i]['Nombre'],
#                                  nodos[j]['Nombre'],
#                                  distanciaEuclidiana(
#                                     (nodos[i]['x'],nodos[i]['y']),
#                                     (nodos[j]['x'],nodos[j]['y'])
#                                  )
#                                 )#Final de la tupla por cada conexión
#                               )#Final del append que acumula en el listado de conexiones
            
#Estructura de datos con el cálculo de las distancias (diccionario)
#Esta información se calcula y no quiero que se modifique
conexiones = dict()
for i in range(len(nodos)):
    for j in range(len(nodos)):
        #Nodos diferentes (prevenir conexiones a un mismo nodo)
        if i != j:
            conexiones[ nodos[i]['Nombre'] + '-' + nodos[j]['Nombre'] ] = (
                                    nodos[i]['Nombre'],
                                    nodos[j]['Nombre'],
                                    distanciaEuclidiana(
                                        (nodos[i]['x'],nodos[i]['y']),
                                        (nodos[j]['x'],nodos[j]['y'])
                                    )
                                )#Final de la tupla por cada conexión

#Salida de diagnóstico
print("---------------")
print(f"Número de conexiones -> {len(conexiones)}")
print("---------------")


#Comparación de heurísticas
#--------------------------

#Llamado a heurística y salidas en pantalla de indicadores
print("---->Vecino Más Cercano Único Arranque")
pp.pprint(heuristicaNN_UnicoArranque(nodos, conexiones)) 


#Estudio comparativo con otros arranques...

#Estudio con otros constructivos