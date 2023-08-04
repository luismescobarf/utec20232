#Uso del try:

edad = int()
division = float()

try:
  edad = int(input("Ingresar edad: "))
  division = 7/4  
except ValueError:
  print("Acciones correspondientes a problema de conversión a entero...")
  edad = 18
except ZeroDivisionError:
  print("Acciones recuperando div...")
  division = 7/1  
else:
  print(f"Cálculo todo ok {edad-division}")
  

#Operaciones aritméticas con la edad
print("Continuando con el resto de instrucciones...")
print(f"Tipo de edad {type(edad)}, contenido: {edad}")
print(f"Resultado de la división: {division}")