#Mostrar en consola estructuras de datos anidadas
import pprint as pp
from functools import reduce
import random

#PPF -> Qué se debe hacer en contraste cómo 
#se deben hacer

#Funciones de primer orden
#Funciones de orden superior -> funciones tipo de dato
#                   -> map, filter, zip, reduce, sort

estudiantes = [
    {'Nombre':'Cecilia','Nota':4.9},
    {'Nombre':'Manuel','Nota':4.7},
    {'Nombre':'Aldo','Nota':4.9},
    {'Nombre':'Luis Miguel','Nota':2.5},
    {'Nombre':'Ana','Nota':4.8}
]

#Quiero realizar una transformación a todos los elementos (map)
def bonificarNota(estudiante):
    return round(estudiante['Nota']+0.1,1)

# pp.pprint(list(map(bonificarNota,estudiantes)))

pp.pprint(list(map(
                    lambda x : round(x['Nota']+0.1,1) ,
                    estudiantes
                )
         )
)

#Ejemplo de filter -> dejar solamente estudiantes con 4.9 o más
#En filter la función de primer orden se llama predicado
def excelencia(estudiante):
    # if estudiante['Nota'] >= 4.9:
    #     return True
    # else:
    #     return False
    return True if estudiante['Nota'] >= 4.9 else False
print()
print()
pp.pprint(list(filter(excelencia,estudiantes)))

#Ejemplo del reduce

#Función de primer orden
def sumarNotas(notaA, notaB):
    return notaA + notaB

# #En dos fases
# columnaNotas = list(map(lambda x:x['Nota'],estudiantes))
# sumatoriaNotas = reduce(sumarNotas,columnaNotas)

promedioNotas = reduce(sumarNotas,
                        list(map(lambda x:x['Nota'],estudiantes)))/len(estudiantes)

print(f"Promedio Notas-> {promedioNotas}")

#Sacar estudiante con la peor nota
def comparadorEstudiantes(e1=dict(),e2=dict()):
   if e1['Nota']<e2['Nota']:
       return e1
   else:
       return e2    

#Versión lambda
# peorEstudiante = reduce(lambda e1=dict(),e2=dict(): e1 if e1['Nota']<e2['Nota'] else e2,estudiantes)

#Versión nombrada
peorEstudiante = reduce(comparadorEstudiantes,estudiantes)

print(peorEstudiante)

#Zip -> Construir tuplas de los elementos de cada colección

#Requerimiento de ejemplo -> diccionario con los nombres
nombresEstudiantes = list(map(lambda x:x['Nombre'],estudiantes))
autoNumericoEstudiantes = list(range(len(estudiantes)))
print()
pp.pprint(dict(zip(autoNumericoEstudiantes,nombresEstudiantes)))


#List comprehension: pythónica de construir colecciones
#Rendimiento -> mutando menos veces el contenedor

coleccionAleatorios = []
numeroElementos = 10
for _ in range(numeroElementos):
    coleccionAleatorios.append(random.randint(1,90))
print()
print(coleccionAleatorios)

print()
print("Utilizando list comprehension")
coleccionLC = [random.randint(1,90) for _ in range(numeroElementos)]
print(coleccionLC)

print("Utilizando list comprehension y filtrando")
print([x for x in coleccionLC if x % 2 == 0])

print()
print("Colección abreviada de elementos en un diccionario")
diccionario = { x:x**2 for x in range(numeroElementos) }
print(diccionario)








    





