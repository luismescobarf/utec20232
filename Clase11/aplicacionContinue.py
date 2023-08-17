#Requerimiento:
#Recorrer los elementos de una cadena generada aleatoriamente
#y acumular únicamente las vocales

#Librerías
import random

#1) Generar cadena aleatoria
alfabeto = "abcdefghijklmnopqrstuvwxyz1234567890"
tamanioCadena = random.randint(15,30)
cadena = str()
#cadena = ''
for _ in range(tamanioCadena):
    cadena += random.choice(alfabeto)       
    
        
print(f"Cadena Generada -> {cadena}") 


#2) Recorrido para acumular únicamente vocales
vocales = "aeiou"
vocalesExtraidas = str()
for i,caracter in enumerate(cadena):
    
    if caracter not in vocales:
        continue

    vocalesExtraidas += caracter
    

print(f"Vocales extraídas -> {vocalesExtraidas}")
    

    
    
    
    


        
    


