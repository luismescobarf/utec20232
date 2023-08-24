#Importado de librerías
import random
import pprint as pp

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
    }    
    
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
#3) Necesito los items -> parejas llave,valor


