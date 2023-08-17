#Requerimiento
#-------------
#Desrrollar un algoritmo que genere números 
#aleatorios del 1 al 100. Contar cuántos 
#intentos fueron
#necesarios para lograr que el número 25
#fuera elegido 19 veces.

#Importado de librerías de apoyo
import random

#Estados iniciales
intentos = 1
aciertos = 0

while True:    
    valor = random.randint(1,100)
    
    if valor == 25:
        #aciertos = aciertos + 1
        aciertos += 1
        
    if aciertos == 19:
        break
    
    intentos += 1
    
print(f"Número de intentos necesario-> {intentos}")


        
        
    
    
    

