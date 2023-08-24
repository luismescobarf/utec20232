#Importado de librerías
import random
import pprint as pp
import listasCompuestas as glc

diccionarioEstudiantes = {
    
    '1014563UTEC':{
        'nombre': 'Maria',
        'apellido': 'Suárez',
        'notas': [4.8,5.0,4.9]
    },
    
    '3456UniAndes':{
        'nombre': 'Luis',
        'apellido': 'Escobar',
        'notas': [1.8,2.0,4.7]
    },
    
    '7800Intercambio':{
        'nombre': 'John',
        'apellido': 'Dole',
        'notas': [2.8,3.0,1.1],
        'seguroInternacional': 'Mapfre'
    },
        
    
}

#Recorridos del diccionario
#1) Obtener las llaves del diccionario
coleccionLlavesDiccionario = list(diccionarioEstudiantes.keys())
print(f"Llaves del diccionario: {coleccionLlavesDiccionario}")

#Recorrer únicamente las llaves del diccionario
print("------------------------")
for llave in diccionarioEstudiantes.keys():
    print(f"Llave obtenida en el recorrido -> {llave}")
print("------------------------")

#Obtener los atributos que presenta uno de los estudiantes
codigoEstudiante = '7800Intercambio'
print(f"Atributos del estudiante {codigoEstudiante}------------------------")
for atributo in diccionarioEstudiantes[codigoEstudiante].keys():
    print(f"Atributo -> {atributo}")
print("------------------------")


#2) Obtener los valores
coleccionValores = tuple(diccionarioEstudiantes.values())
pp.pprint(coleccionValores)
print("------------------------")
for estudiante in diccionarioEstudiantes.values():
    print(f"Estudiante -> {estudiante}")
print("------------------------")


#3) Necesito los items -> parejas llave,valor
coleccionItems = list(diccionarioEstudiantes.items())
pp.pprint(coleccionItems)

print("------------------------")
for codigo,estudiante in diccionarioEstudiantes.items():
    print(f"Cod Estudiante -> {codigo}")
    print(f"Info Estudiante -> {estudiante}")
print("------------------------")

#Utilizar la información en la lista de ítems del diccionario
for i, tuplaEstudiante in enumerate(coleccionItems):
    codigo = tuplaEstudiante[0]
    estudiante = tuplaEstudiante[1]
    print(f"Info Tupla -> {codigo} | {estudiante}")
    
#Convertir el diccionario de diccionarios de estudiantes
#en una lista de diccionarios para mantener el orden
#en caso de que se necesite por algún criterio, sin
#embargo no queremos perder el código del estudiante,
#manteniendo la estructura tipo diccionario para el estudiante

listaEstudiantes = list()
for codEstudiante, estudiante in diccionarioEstudiantes.items():
    estudiante['codigoEstudiante'] = codEstudiante
    listaEstudiantes.append(estudiante)
print("------------------------")
pp.pprint(listaEstudiantes)
print("------------------------")

#Generar base de datos de estudiantes y convertirla a
#una lista de diccionarios de estudiantes, para tener
#un acceso más claro a los atributos de estos
listaCompuestaEstudiantes = glc.generarListadoEstudiantes()
print("------------------------")
pp.pprint(listaCompuestaEstudiantes)
print("------------------------")

bdEstudiantes = list()

for i in range(len(listaCompuestaEstudiantes)):
    estudianteTemp = dict()
    estudianteTemp['nombre'] = listaCompuestaEstudiantes[i][0]
    estudianteTemp['apellido'] = listaCompuestaEstudiantes[i][1]
    estudianteTemp['email'] = listaCompuestaEstudiantes[i][2]
    estudianteTemp['promedio'] = listaCompuestaEstudiantes[i][3]
    estudianteTemp['edad'] = listaCompuestaEstudiantes[i][4]
    bdEstudiantes.append(estudianteTemp)

print("------------------------")
pp.pprint(bdEstudiantes)
print("------------------------")

#Requerimiento -> conocer cuántas edades diferentes
#fueron registradas en la base de datos de estudiantes
conjuntoEdades = set()
for estudiante in bdEstudiantes:
    conjuntoEdades.add(estudiante['edad'])
print("------------------------")
print(conjuntoEdades)
numeroEdadesRepetidas = len(bdEstudiantes) - len(conjuntoEdades) 
print(f"Edades repetidas -> {numeroEdadesRepetidas}")
print("------------------------")

#Requerimiento -> ordenar los estudiantes (lista) 
#según su promedio (de mayor a menor)
def criterioOrdenamiento(estudiante):
    
    #Cubrir otros tipos de datos
    if not(isinstance(estudiante['promedio'],float) or isinstance(estudiante['promedio'],int)):
        return 0
    else:    
        #Seleccionando el atributo
        atributoInteres = estudiante['promedio']
        #Retornando para entregárselo al algoritmo de ordenamiento
        return atributoInteres

bdEstudiantes.sort(reverse=True,key=criterioOrdenamiento)
print("------------------------")
pp.pprint(bdEstudiantes)
print("------------------------")

#Ordenar por edad
# def criterioEdad(estudiante):
#     return estudiante['edad']
# criterioEdad = lambda x : x['edad']

bdEstudiantes.sort(key = lambda x : x['edad']  )
print("------------------------")
pp.pprint(bdEstudiantes)
print("------------------------")












