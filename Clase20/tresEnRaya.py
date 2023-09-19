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
    

#Revisar el estado del tablero
def revisarEstadoTablero(tablero):
    
    #Determinar si gana O
    ganoColumna = 3 in np.sum(tablero,axis=0)
    ganoFila = 3 in np.sum(tablero,axis=1)
    ganoDiagonal = 3 == np.sum(tablero.diagonal())
    ganoDiagonalContraria = 3 == np.sum(np.fliplr(tablero).diagonal())
    if any([ganoColumna,
            ganoFila,
            ganoDiagonal,
            ganoDiagonalContraria]):
        return 1
    
    #Determinar si gana X
    ganoColumna = 30 in np.sum(tablero,axis=0)
    ganoFila = 30 in np.sum(tablero,axis=1)
    ganoDiagonal = 30 == np.sum(tablero.diagonal())
    ganoDiagonalContraria = 30 == np.sum(np.fliplr(tablero).diagonal())
    if any([ganoColumna,
            ganoFila,
            ganoDiagonal,
            ganoDiagonalContraria]):
        return 10
    
    #Determinar si tenemos un empate
    # O -> 5 movimientos, x 4 movimientos: 5+40 = 45
    empateIniciandoO = np.sum(tablero) == 45
    # X -> 5 movimientos, O 4 movimientos: 50+4 = 54
    empateIniciandoX = np.sum(tablero) == 54
    if any([empateIniciandoO,empateIniciandoX]):
        return 0
    
    #No fue identificdo ninguno de los casos -> continuar jugando
    return -1               
            

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
        #Retorno 1 Si ganó el jugador O
        #Retorno 10 Si ganó el jugador X
        #Retorno 0 Si hay empate
        #Retorno -1 Si vamos a continuar
        estado = revisarEstadoTablero(tablero)
        
        #Posibles estados
        #-----------------------------------------        
        
        #Ganó el jugador O
        if estado == 1:                        
            print("Ganó el Jugador O")
            return  1
        #Ganó el jugador X
        elif estado == 10:            
            print("Ganó el Jugador X")
            return  10        
        #Empate
        elif estado == 0:
            print("Empate!!!")
            return  0 
        
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
            
        #El juego continúa -> mostrar el tablero y alternar jugador
        mostrarTablero(tablero)
        input()       
    
    
#Sección principal
#------------------
ejecutarJuego()
    


