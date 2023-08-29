#Importado de librerías
import random
import pprint as pp

#Definición de funciones
def generarEstudiante():
    
    nombres = [
        'Cecilia',
        'Aldo',
        'Ana',
        'Gustavo',
        'Mario',
        'Luis',
        'Homero',
        'Lionel',
        'Cristiano',
        'Andrea'
        ]
    
    apellidos = [
        'Escobar',
        'Simpson',
        'Maradona',
        'Valderrama',
        'Messi',
        'Nader',
        'Suárez',
        'Spiess',
        'Marfurt'
        ]
    
    dominios = [
        'utec.edu.ur',
        'uniandes.edu.co'
        ]
    
    estudiante = []
    
    #Nombre
    estudiante.append( random.choice(nombres) )
    #Apelido
    estudiante.append( random.choice(apellidos) )
    #Correo
    correo = estudiante[0].lower() + '.' + estudiante[1].lower() 
    correo = correo + '@' + random.choice(dominios)
    estudiante.append( correo )
    #Promedio programa
    promedioPrograma = random.randint(0,4) + round(random.randint(0,9)*0.10,1)
    estudiante.append(promedioPrograma)
    #Edad
    edad = random.randint(12,85)
    estudiante.append(edad)
    
    return estudiante   
    
    

def generarListadoEstudiantes():
    numeroEstudiantes = random.randint(15,40)
    listaEstudiantes = []
    
    for _ in range(numeroEstudiantes):
        estudiante = generarEstudiante()
        
        # #Salida de diagnóstico
        # print("-----------------------")
        # print(estudiante)
        # print("-----------------------")
        # input()
        
        listaEstudiantes.append(estudiante)
    
    return listaEstudiantes

#1) Estudiante con mejor nota
def obtenerEstudianteMejorNota(listadoEntrada):
    
    #Preparar contenedor del retorno
    estudianteBuscado = []
    
    #Estado inicial de la incumbente
    idEstudiante = None
    mejorNota = -1
    
    #Recorrido compacto
    # for i, estudiante in enumerate(listadoEntrada):
    #     if estudiante[3] > mejorNota:
    #         #Quién
    #         idEstudiante = i
    #         #Cuánto
    #         mejorNota = estudiante[3]
    
    #Recorrido completamente basado en índices       
    for i in range(len(listadoEntrada)):
        if listadoEntrada[i][3] > mejorNota:
            #Quién
            idEstudiante = i
            #Cuánto
            mejorNota = listadoEntrada[i][3]
    
    #Cargando en variable de salida el estudiante con la mejor nota
    estudianteBuscado = list(listadoEntrada[idEstudiante])
    
    #Retornar el estudiante de interés de la función
    return estudianteBuscado 


#2) Estudiante con peor nota
def obtenerEstudiantePeorNota(listadoEntrada):
    
    #Preparar contenedor del retorno
    estudianteBuscado = []
    
    #Estado inicial de la incumbente
    idEstudiante = None
    peorNota = 999    
    
    #Recorrido completamente basado en índices       
    for i in range(len(listadoEntrada)):
        if listadoEntrada[i][3] < peorNota:
            #Quién
            idEstudiante = i
            #Cuánto
            peorNota = listadoEntrada[i][3]
    
    #Cargando en variable de salida el estudiante con la peor nota
    estudianteBuscado = list(listadoEntrada[idEstudiante])
    
    #Retornar el estudiante de interés de la función
    return estudianteBuscado 

#3) Promedio de edad del grupo de estudiantes
def obtenerPromedioGrupoEstudiantes(listadoEntrada):
    
    #Inicializar el promedio
    promedio = float()
    
    #Extraer columna de promedios
    columnaPromedios = []    
    for estudiante in listadoEntrada:
        columnaPromedios.append(estudiante[4])   
       
    #Calcular promedio
    promedio = int(sum(columnaPromedios) / len(columnaPromedios)) 
       
    #Retornar el promedio
    return promedio 

#4) Estudiantes que pertenecen a UTEC
def filtrarEstudiantesUTEC(listadoEntrada):
    
    #Inicializar subconjunto estudiantes
    estudiantesUTEC = []
    
    # #Recorrer todos los estudiantes para filtrar
    # for estudiante in listadoEntrada:
    #     partesCorreo = estudiante[2].split('@')
    #     if partesCorreo[1] == 'utec.edu.ur':
    #         estudiantesUTEC.append(estudiante)
            
    #Recorrer todos los estudiantes para filtrar
    for estudiante in listadoEntrada:        
        if 'utec' in estudiante[2]:
            estudiantesUTEC.append(estudiante)
    
    #Retornar el listado
    return estudiantesUTEC




