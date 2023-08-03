#Solicitar al usuario tres palabras y encontrar el promedio de número
#de letras que tiene cada palabra. Solamente tener en cuenta las palabras
#que no sean vacías.

#Obtener las palabras sobre las cuales sacaremos un indicador
palabra1 = input("Ingresar palabra 1: ")
palabra1 = palabra1.strip()
palabra2 = input("Ingresar palabra 2: ")
palabra2 = palabra2.strip()
palabra3 = input("Ingresar palabra 3: ")
palabra3 = palabra3.strip()

#Inicializar variable de conteo
palabrasCumpliendo = 0

#Revisar la primera palabra
numeroLetrasPalabra1 = len(palabra1)
if numeroLetrasPalabra1 > 0:
    palabrasCumpliendo = palabrasCumpliendo + 1
    
#Revisar la segunda palabra
numeroLetrasPalabra2 = len(palabra2)
if numeroLetrasPalabra2 > 0:
    palabrasCumpliendo = palabrasCumpliendo + 1
    
#Revisar la tercera palabra
numeroLetrasPalabra3 = len(palabra3)
if numeroLetrasPalabra3 > 0:
    palabrasCumpliendo = palabrasCumpliendo + 1
    
#Calcular el promedio
promedio = float()
try:
    #Instrucción que puede tener problemas
    promedio = (numeroLetrasPalabra1 + numeroLetrasPalabra2 + numeroLetrasPalabra3) / palabrasCumpliendo

#Manejo de excepción específica de la instrucción
except ZeroDivisionError:
    print("Error calculando el promedio, división entre cero")
else:
    #Operación si el promedio fue exitoso
    mitad = promedio / 2
    print(f"Mostrar mitad del promedio: {mitad}")
    

print(f"Promedio de letras es: {promedio}")
print("Fin de la ejecución")


