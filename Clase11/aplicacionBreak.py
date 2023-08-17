#Requerimiento:
#Recorrer los elementos de una cadena generada aleatoriamente
#Recorrer la cadena generada y cuando el número de dígitos
#y caracteres especiales sea 4, detener el proceso 
#y mostrar en qué posición de la cadena se detuvo el recorrido

#Librerías
import random

#1) Generar cadena aleatoria
alfabeto = "abcdefghijklmnopqrstuvwxyz1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$"
tamanioCadena = random.randint(15,30)
cadena = str()
#cadena = ''
for _ in range(tamanioCadena):
    
    letraDiferenteEncontrada = False
    
    while True:
        
        letraElegida = random.choice(alfabeto)
        if letraElegida not in cadena:    
            cadena = cadena + letraElegida
            letraDiferenteEncontrada = True
        
        if letraDiferenteEncontrada:
            break
        
print(f"Cadena Generada -> {cadena}") 


#2) Recorrer hasta encontrar el número de dígitos 
#y caracteres especiales de parada (4 ocurrencias)
ocurrencias = 0
caracteresBusqueda = "0123456789!#$ "
for i,caracter in enumerate(cadena):
    
    if caracter in caracteresBusqueda:
        ocurrencias += 1
    
    if ocurrencias == 4:
        print(f"Posición resultante del recorrido -> {i}")
        break


        
    


