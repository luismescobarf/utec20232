#Librerías
import random
import pprint as pp

#Contenedor ordenado de servicios
coleccionServicios = []


# #Contenedor ejemplo de servicio
# servicio = {
#     't0':400,
#     'tf':445,
#     'duracion':45
# }


#Generación aleatoria de servicios
numeroServicios = 20
cuatroAM = 240 #Minutos
diezPM = 1320 #Minutos
for _ in range(numeroServicios):
    t0 = random.randint(cuatroAM,diezPM)
    tf = int()
    while True:
        tf = random.randint(cuatroAM,diezPM)
        if tf > t0 and tf-t0 <= 180 and tf-t0 > 15:
            servicio = {
                't0':t0,
                'tf':tf,
                'duracion':tf-t0
            }
            coleccionServicios.append(servicio)
            break
pp.pprint(coleccionServicios)

#Caso de estudio de asignación
#Caso 1
coleccionServicios = [
    {'duracion': 27, 't0': 631, 'tf': 658},
    {'duracion': 121, 't0': 1170, 'tf': 1291},
    {'duracion': 98, 't0': 932, 'tf': 1030},
    {'duracion': 110, 't0': 801, 'tf': 911},
    {'duracion': 107, 't0': 780, 'tf': 887},
    {'duracion': 36, 't0': 828, 'tf': 864},
    {'duracion': 70, 't0': 1021, 'tf': 1091},
    {'duracion': 143, 't0': 885, 'tf': 1028},
    {'duracion': 176, 't0': 245, 'tf': 421},
    {'duracion': 168, 't0': 341, 'tf': 509},
    {'duracion': 72, 't0': 470, 'tf': 542},
    {'duracion': 16, 't0': 712, 'tf': 728},
    {'duracion': 171, 't0': 430, 'tf': 601},
    {'duracion': 94, 't0': 1196, 'tf': 1290},
    {'duracion': 68, 't0': 787, 'tf': 855},
    {'duracion': 175, 't0': 345, 'tf': 520},
    {'duracion': 116, 't0': 700, 'tf': 816},
    {'duracion': 136, 't0': 661, 'tf': 797},
    {'duracion': 32, 't0': 633, 'tf': 665},
    {'duracion': 126, 't0': 1049, 'tf': 1175}
]

#Inicializar cuadro de turnos -> Lista (también podría ser un diccionario)
cuadroTurnos = list()

#Esquema de un turno
# turno = dict()
# turno['duracion'] = sumatoriaServicios
# turno['listadoServicios'] = [
#                                 {'duracion': 171, 
#                                  't0': 430, 
#                                  'tf': 601
#                                  },
#                                 {'duracion': 116, 
#                                  't0': 700, 
#                                  'tf': 816
#                                  }
#                             ]


#Acomodar cada uno de los turnos
#Concurrent scheduler







    