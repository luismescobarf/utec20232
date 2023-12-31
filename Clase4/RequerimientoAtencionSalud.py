"""
2) Escribir una función que recibe la capacidad de atención
que tiene un puesto de salud (número de pacientes) por día,
y 5 valores que corresponden a los pacientes que llegaron 
los días hábiles (lunes a viernes) de la semana anterior. 
Obtener cuántas personas no fueron atendidas en promedio 
la semana anterior, y cuánto fue el número de usuarios
donde el servicio presentó mayor desborde.
"""

#Algoritmo
#1) Capacidad de atención del puesto salud (pacientes/día)
#2) Obtener pacientes que llegaron el lunes.
#3) Obtener pacientes que llegaron el martes.
#4) Obtener pacientes que llegaron el miércoles.
#5) Obtener pacientes que llegaron el jueves.
#6) Obtener pacientes que llegaron el viernes.
#7) Obtener personas sin atender para cada día.
#8) Calcular el promedio de personas que no fueron atendidas.
#9) Desborde máximo del servicio.
#10) Presentar informe (indicadores solicitados)

#Transcripción -> Lenguaje Python
#1) Capacidad de atención del puesto salud (pacientes/día)
capacidadAtencion = int(input("Ingresar pacientes/dia: "))

#2) Obtener pacientes que llegaron el lunes.
pacientesLunes = int(input("Pacientes lunes: "))

#3) Obtener pacientes que llegaron el martes.
pacientesMartes = int(input("Pacientes martes: "))

#4) Obtener pacientes que llegaron el miércoles.
pacientesMiercoles = int(input("Pacientes miércoles: "))

#5) Obtener pacientes que llegaron el jueves.
pacientesJueves = int(input("Pacientes jueves: "))

#6) Obtener pacientes que llegaron el viernes.
pacientesViernes = int(input("Pacientes viernes: "))

#7) Obtener personas sin atender para cada día.
difUsuariosLunes = pacientesLunes - capacidadAtencion
difUsuarioMartes = pacientesMartes - capacidadAtencion
difUsuarioMiercoles = pacientesMiercoles - capacidadAtencion
difUsuarioJueves = pacientesJueves - capacidadAtencion
difUsuarioViernes = pacientesViernes - capacidadAtencion

#8) Calcular el promedio de personas que no fueron atendidas.
excedenteAcumulado = sum([difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes])
promedioExcedente = excedenteAcumulado / 5

#9) Desborde máximo del servicio
desbordeMax = max([difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes])

#10) Presentar informe (indicadores solicitados)
print(f"Promedio de personas sin atender: {promedioExcedente}")
print(f"Desborde máximo en un día: {desbordeMax}")




