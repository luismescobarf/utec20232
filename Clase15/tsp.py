#Librerías
import pprint as pp

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
    for i in range(len(nodos)-1): 
        nombrePartida = nodos[ i ]['Nombre']
        nombreLlegada = nodos[ i+1 ]['Nombre']
        nombreConexion = nombrePartida + '-' + nombreLlegada
        
        #Salida de diagnóstico
        print("->",nombreConexion)
        
        distanciaTotal += conexiones[nombreConexion][2]
    return distanciaTotal    
    

#Represntar red
nodos = [] #Permite asociar un id a cada uno de los elementos

#Nodo a nodo adición en esa lista
nodos.append({'Nombre':'A','x':0,'y':0})
nodos.append({'Nombre':'B','x':10,'y':10})
nodos.append({'Nombre':'C','x':-10,'y':-3})
nodos.append({'Nombre':'D','x':-5,'y':8})
nodos.append({'Nombre':'E','x':11,'y':-2})


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
                              
#Algoritmo para encontrar el recorrido para el TSP
#Vecino más cercano NN Nearest Neigborgh

#Establecer estructuras de control de los nodos que han sido cubiertos y los que no
nodosCubiertos = set()
nodosPendientes = set()
for i in range(len(nodos)):
    nodosPendientes.add(i)  

    
#Inicialización -> Nodo 0
nodoInicial = 4
ruta = [nodoInicial]
#Cubrir nodo inicial
nodosCubiertos.add(nodoInicial)
#Quitar el nodo inicial de los pendientes
nodosPendientes.remove(nodoInicial)

#Ciclo general del algoritmo
while nodosPendientes != set():
#while len(nodosPendientes) > 0:
    
    #Último nodo cubierto -> Nodo actual
    nodoActual = ruta[-1]
    
    #Colección de conexiones a nodos que salen del actual
    #Debe ser una lista porque vamos a ordenar
    salidas = []
    
    #Selección de conexiones
    for llave, infoConexion in conexiones.items():
        
        #Condiciones del filtrado
        #1) Todas las que están conectadas al nodo actual
        nombreNodoActual = nodos[nodoActual]['Nombre']
        puntoPartida = llave.split('-')[0]
        cond1 = nombreNodoActual == puntoPartida        
        
        #2) Además se debe cumplir que el nodo final esté en los pendientes
        puntoTerminal = llave.split('-')[-1]
        # for i,nodo in enumerate(nodos):
        #     if puntoTerminal == nodo['Nombre']:
        #         puntoTerminal = i
        #         break  
        puntoTerminal = traducirNombreIndice(puntoTerminal,nodos)
                
        cond2 = puntoTerminal in nodosPendientes
        
        #Si se cumplen ambas condiciones entonces es una salida candidata
        if cond1 and cond2:
            salidas.append(infoConexion)
        
    #Seleccionar la mejor salida
    salidas.sort(key= lambda salida : salida[2] )
    indiceNodoSalida = traducirNombreIndice(salidas[0][1], nodos)    
    ruta.append(indiceNodoSalida)
    nodosCubiertos.add(indiceNodoSalida)
    nodosPendientes.remove(indiceNodoSalida)

#Completar la ruta
ruta.append(nodoInicial)
distanciaTotal = calcularDistancia(ruta,nodos,conexiones)
print(f"Ruta: {ruta} Distancia: {distanciaTotal}")

    
    
    
    
        
        
        
        
        
        
        
        
    
    


    

            
        
    



