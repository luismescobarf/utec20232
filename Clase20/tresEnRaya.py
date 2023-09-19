import numpy as np
import pprint as pp
import random


#Visualizar el tablero
def mostrarTablero(tablero):
    for fila in tablero:
        for columna in fila:
            if columna == 1:
                print(' O ', end='')
            elif columna == 10:
                print(' X ', end='')
            elif columna == 0:
                print(' _ ', end='')
        print()
    print()
    
def formatoVacias(casillasVacias):
    filas = list(casillasVacias[0])
    columnas = list(casillasVacias[1])
    listaCV = list(zip(filas,columnas))
    return listaCV
            
def jugadorO(tablero):
    
    #Identificar casillas vacías
    casillasVacias = np.where(tablero==0)
    
    # #Ilustrar la intervención de numpy y el cambio de formato
    # print("Retorna el where")
    # print(casillasVacias)
    # print("Nuevo formato")
    # print(formatoVacias(casillasVacias))

    #Nuevo formato para selección aleatoria
    listaCV = formatoVacias(casillasVacias)
    
    #Elegir el movimiento
    movimiento = random.choice(listaCV)
    
    #Aplicar el movimiento
    tablero[movimiento] = 1
    
def jugadorX(tablero):
    
    #Identificar casillas vacías
    casillasVacias = np.where(tablero==0)
    
    # #Ilustrar la intervención de numpy y el cambio de formato
    # print("Retorna el where")
    # print(casillasVacias)
    # print("Nuevo formato")
    # print(formatoVacias(casillasVacias))

    #Nuevo formato para selección aleatoria
    listaCV = formatoVacias(casillasVacias)
    
    #Elegir el movimiento
    movimiento = random.choice(listaCV)
    
    #Aplicar el movimiento
    tablero[movimiento] = 10
               
            

#Juego de tres en raya
def ejecutarJuego():
    
    #Inicio del juego -> Construir tablero
    tablero = np.zeros((3,3))
    
    # #Salida de diagnóstico
    # print(tablero)
    
    #Interacción -> mostrar el inicio del tablero
    print("---Inicio del Juego---")
    mostrarTablero(tablero)
    
    #Seleccionar el jugador que inicia
    jugadorSeleccionado = 1 if random.randint(0,1) else 10
    
    #Efectuar el turno correspondiente
    if jugadorSeleccionado == 1:
        #Juega O  
        jugadorO(tablero)  
        
        #Paso el turno a X
        jugadorSeleccionado = 10
        
    else:
        #Juega X
        jugadorX(tablero)
        
        #Paso el turno a O
        jugadorSeleccionado = 1
    
    #Ciclo principal del juego
    while True:
        
        #Revisar el estado del tablero o del juego
        
        
    
    
    
#Sección principal
#------------------
ejecutarJuego()
    


