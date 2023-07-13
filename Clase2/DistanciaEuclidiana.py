
"""
3) Algoritmo para calcular la distancia entre dos
puntos (Distancia Euclidiana) (x1,y1) (x2,y2)
"""

#Cargar las componentes de los puntos en variables
x1 = x2 = y1 = y2 = int()
x1 = 0
y1 = 0
x2 = 25
y2 = 0

#Calcular la distancia
dP1P2  = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

#Mostrar la distancia
print(dP1P2)
