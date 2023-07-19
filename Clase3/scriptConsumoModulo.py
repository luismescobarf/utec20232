#Requerimiento: solicitar al usuario el radio
#y la altura de un cilindro, reportar el área
#de un corte infinitesimal del cilindro (círculo)
#y queremos que reporte el volumen del cilindro


#Algoritmo
#1) Solicitar la altura del cilindro
#2) Solicitar el radio del cilindro
#3) Calcular el área del corte del cilindro (círculo)
#4) Calcular el volumen del cilindro
#5) Presentar en pantalla resultados

#Importar funcionalidades o librerías
from ModuloGeometrico.AreasPoligonosBasicos import calcularAreaCirculo
from ModuloGeometrico.VolumenesSolidosBasicos import calcularVolumenCilindro

altura = int(input("Ingresar altura del cilindro: "))
radio = int(input("Ingresar radio del círculo: "))
volumenCilindro = calcularVolumenCilindro(altura=altura, radio=radio)
areaCirculo = calcularAreaCirculo(radio)
print(f"V. Cilindro es: {volumenCilindro}")
print(f"A. Círculo es: {areaCirculo}")


