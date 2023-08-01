#Proposición: Juan es mayor de edad
edadJuan = 45
valorVerdad = edadJuan > 18
print(f"Juan es mayor de edad -> {valorVerdad}")

#Requerimiento 1:
#- Leer un número entero y leer un intervalo cerrado y determinar si el número se encuentra dentro o fuera del intervalo.

#[limInf,limSup]
#P: Número debe ser mayor o igual al límite inferior
#Q: Número debe ser menor o igual al límite superior
#P ^ Q

def identificarPertenencia():
  num = int(input("Ingresar número: "))
  limInf = int(input("Ingresar límite inferior: "))
  limSup = int(input("Ingresar límite superior: "))
  
  if num>=limInf and num<=limSup:
    #Instrucciones cuando la expresión es True
    print("Está dentro del intervalo")
    #Otras instrucciones  
    #
    #
  else:
    #Instrucciones cuando la expresión es False
    print("Está fuera del intervalo")
    #Otras instrucciones  
    #
    #

#- Desarrollar una función que reciba dos números enteros y retornar el mayor de estos números (condicionales)

def obtenerNumeroMayor(num1,num2):
  if num1 > num2:
    return num1     
  else:
    return num2

"""
num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar segundo número: "))
print("el valor mayor es ",obtenerNumeroMayor(num1,num2))
"""

#- Leer tres números enteros y retornar el mayor (únicamente condicionales)
  

def obtenerNumeroMayor3(a,b,c):
  if a>b:
    if a>c:
      return a
    else:
      return c
  else:
    if b>c:
      return b
    else:
      return c

"""
num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar segundo número: "))
num3 = int(input("Ingresar tercer número: "))
print("el valor mayor de los 3 es ",obtenerNumeroMayor3(num1,num2,num3))
"""

palabra = "hola"
numeroCaracteres = len(palabra)
print(f"Longitud Palabra ->{numeroCaracteres}")

#- Reportar la mayor (más larga) de tres palabras y revisar si presenta una longitud par o impar, adicionalmente reportar la menor y si su longitud es par o impar. Podemos utilizar max y min.

def funcion(a,b):
  c1 = a + b
  c2 = a / b
  return c1,c2

#resultado1,resultado2=funcion(a,b)

#Solución Cecilia
palabra1 = len(input("Ingrese una palabra: "))
palabra2 = len(input("ingrese la segunda palabra: "))
palabra3 = len(input("Ingrese la tercera palabra: "))

def palabraMayor(palabra1,
                palabra2,
                palabra3):
  
  if palabra1 > palabra2:
      if palabra1 > palabra3:
          return palabra1
      else:
          return palabra3
  else:
      if palabra2 > palabra3:
          return palabra2
      else:
          return palabra3

def palabraMenor(palabra1,
                palabra2,
                palabra3):
  
  if palabra1 < palabra2:
      if palabra1 < palabra3:
          return palabra1
      else:
          return palabra3
  else:
      if palabra2 < palabra3:
          return palabra2
      else:
          return palabra3
#Proposición: N es par
#Expresión booleana: N % 2 == 0

def parImpar (pc,pl):
    #Preparar las variables que reportan sobre cada palabra
    pcEsPar = False
    plEsPar = False
    #Revisar las palabras

    #Revisión de palabra corta
    if pc % 2 == 0:
      pcEsPar = True    

    #Revisión de palabra larga
    if pl % 2 == 0:
      plEsPar = True

    return pcEsPar, plEsPar
        

pcEsPar, plEsPar =  parImpar(palabraMenor(palabra1,palabra2,palabra3),        palabraMayor(palabra1,palabra2,palabra3))

print(f"La palabra corta es par? {pcEsPar}")
print(f"La palabra mayor es par? {plEsPar}")