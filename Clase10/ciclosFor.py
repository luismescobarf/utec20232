#1) Algoritmo  para imprimir los números 
#del 1 al 10

#Solución especificando las repeticiones
# print("1")
# print("2")
# print(".")
# print(".")
# print(".")
# print("10")

#Generalización

#Estados previos al inicio de las repeticiones
n = 1#Variable(s) involucradas en el cómputo
#i = 0#Contador (controlar las repeticiones)

#Un solo valor en el range corresponde al límite superior
#Siempre trabaja hasta estrictamente menor al límite superior
#Por defecto: valor inicial en 0, avance en 1
for i in range(10):
    #Generalización
    print(n)
    #Actualizaciones (valor de i, n)
    # i = i + 1
    n = n + 1
    print('---')

print()
print()

#2) Algoritmo  para imprimir los números 
#desde 7 hasta un número m ingresado por el usuario

m = int(input("Ingrresar hasta donde se realiza el conteo: "))

#Dos valores en el range corresponden al límite inferior y al 
#límite superior (estrictamente menor al límite superior)
#Defecto: Avance es de uno en uno
for i in range(7,m+1):
    print(i)     
    print("***")

# print("Valor de n después de iteraciones -> ",n)

#3) Algoritmo  para imprimir los números 
#desde un número a, hasta un número b, avanzando de 3 en 3
#Ejemplo: 6 -> 16: 6,9,12,15
a = int(input("Desde dónde: "))
b = int(input("Hasta dónde: "))
for i in range(a,b+1,3):
    print(i)
    print("####")

#4) Algoritmo para imprimir un saludo n veces, donde
#n es definido por el usuario
n = int(input("Ingrese número de saludos: "))
for _ in range(n):
    print("Hola Mundo!!!")
    




print("Proceso posterior al ciclo para")



