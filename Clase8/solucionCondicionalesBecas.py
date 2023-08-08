def becasEstudiantesClase(edad,promedio,semestre):
    if semestre == 8 or semestre == 9:        
        if edad < 23 and promedio > 4.1:
            return 0.7
        else:
            return 0
    else:
        if semestre == 10:
            if edad < 23 and promedio > 4.1:
                return 0.5
            else:
                if promedio > 4.5:
                    return 0.05
                else:
                    return 0
        else:
            return 0
        
#Sección principal
#-----------------
# print( becasEstudiantesClase(18, 4.2, 8) )
# print( becasEstudiantesClase(40, 4.8, 10) )
# print( becasEstudiantesClase(20, 3.8, 10) )
# print( becasEstudiantesClase(29, 3.2, 8) )
# print( becasEstudiantesClase(17, 4.7, 3) )
# print( becasEstudiantesClase(18, 4.2, 10) )
#1 Lectura de información
edad = int(input("Ingrese la edad: "))
promedio = float(input("Ingrese el promedio: "))
semestre = int(input("Ingrese el semestre: "))
#2 Realizar el cálculo
porcentajeDescuento = becasEstudiantesClase(edad,promedio,semestre)
#3 Presentar el cálculo
print(f"Para el estudiante con edad {edad}, promedio {promedio} y semestre {semestre} el porcentaje de descuento es {porcentajeDescuento}")

"""Detalle de Casos: 
[{'Entrada': (18, 4.2, 8), 'Esperado': 0.7},
 {'Entrada': (40, 4.8, 10), 'Esperado': 0.05},
 {'Entrada': (20, 3.8, 10), 'Esperado': 0},
 {'Entrada': (29, 3.2, 8), 'Esperado': 0},
 {'Entrada': (17, 4.7, 3), 'Esperado': 0},
 {'Entrada': (18, 4.2, 10), 'Esperado': 0.5}]"""
