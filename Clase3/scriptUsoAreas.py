#Requerimiento: solicitar al usuario la información
#de un cuadrado y de un círculo para calcular sus
#áreas e informarlas en pantalla

#Algoritmo
#1) Solicitar el lado del cuadrado al usuario
#2) Solicitar el radio del círculo
#3) Calcular el área del cuadrado
#4) Calcular el área del círculo
#5) Presentar áreas de los polígonos

#Importar funcionalidades o librerías
# import AreasPoligonosBasicos #Versión 1 y 2
# from AreasPoligonosBasicos import * #Versión 3
# from AreasPoligonosBasicos import calcularAreaCirculo #Versión 4
import AreasPoligonosBasicos as ap #Versión 5

"""
#Versión1
lado = int(input("Ingresar lado del cuadrado: "))
radio = int(input("Ingresar radio del círculo: "))
areaCuadrado = AreasPoligonosBasicos.calcularAreaCudarado(lado)
areaCirculo = AreasPoligonosBasicos.calcularAreaCirculo(radio)
print(f"A. Cuadrado es: {areaCuadrado}")
print(f"A. Círculo es: {areaCirculo}")
"""

"""
#Versión2
lado = int(input("Ingresar lado del cuadrado: "))
radio = int(input("Ingresar radio del círculo: "))
print(f"A. Cuadrado es: {AreasPoligonosBasicos.calcularAreaCudarado(lado)}")
print(f"A. Círculo es: {AreasPoligonosBasicos.calcularAreaCirculo(radio)}")
"""

"""
#Versión3
lado = int(input("Ingresar lado del cuadrado: "))
radio = int(input("Ingresar radio del círculo: "))
areaCuadrado = calcularAreaCudarado(lado)
areaCirculo = calcularAreaCirculo(radio)
print(f"A. Cuadrado es: {areaCuadrado}")
print(f"A. Círculo es: {areaCirculo}")
"""

"""
#Versión4
radio = int(input("Ingresar radio del círculo: "))
areaCirculo = calcularAreaCirculo(radio)
print(f"A. Círculo es: {areaCirculo}")
"""


#Versión5
lado = int(input("Ingresar lado del cuadrado: "))
radio = int(input("Ingresar radio del círculo: "))
areaCuadrado = ap.calcularAreaCudarado(lado)
areaCirculo = ap.calcularAreaCirculo(radio)
print(f"A. Cuadrado es: {areaCuadrado}")
print(f"A. Círculo es: {areaCirculo}")



