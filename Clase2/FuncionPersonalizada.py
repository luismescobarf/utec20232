"""
Escribir un programa que reciba
4 edades y muestra cuál es la mayor, cuál es la menor
y el promedio de edades
"""

#Función personalizada -> Promedio de 4 edades
def calcularPromedioEdades(e1,e2,e3,e4):
    promedio = sum([e1,e2,e3,e4]) / 4
    return promedio
    

Edad1 = 15
Edad2 = 37
Edad3 = 44
Edad4 = 62

MayorEdad = max(Edad1, Edad2, Edad3, Edad4)
MenorEdad = min(Edad1, Edad2, Edad3, Edad4)
Promedio = calcularPromedioEdades(Edad1, Edad2, Edad3, Edad4)

print(f"La mayor edad es {MayorEdad}, la menor edad es {MenorEdad} y el promedio es {Promedio}")

