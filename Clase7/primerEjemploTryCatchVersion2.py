#Uso del try:

edad = int()

try:
  edad = int(input("Ingresar edad: ")) 
except ValueError:
  print("Acciones correspondientes a problema de conversión a entero...")
  edad = 18
else:
  print(f"Tras conversión exitosa proyectar años {edad+3}")  

#Operaciones aritméticas con la edad
print("Continuando con el resto de instrucciones...")
print(f"Tipo de edad {type(edad)}, contenido: {edad}")