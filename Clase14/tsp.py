#Librerías
import pprint as pp

#Distancia Euclidiana
def distanciaEuclidiana(P1,P2):
    return  int(( (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2 )**(1/2))

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
                              

            
        
    



