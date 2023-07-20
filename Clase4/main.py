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

#Importar definiciones
import Interaccion as inter
import Logica as l

#1) Capacidad de atención del puesto salud (pacientes/día)
#2) Obtener pacientes que llegaron el lunes.
#3) Obtener pacientes que llegaron el martes.
#4) Obtener pacientes que llegaron el miércoles.
#5) Obtener pacientes que llegaron el jueves.
#6) Obtener pacientes que llegaron el viernes.
capacidadAtencion, pacientesLunes, pacientesMartes, pacientesMiercoles, pacientesJueves, pacientesViernes = inter.capturarInfoPuestoSalud()


#7) Obtener personas sin atender para cada día.
difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes = l.calcularExcedentesDiasHabiles(capacidadAtencion, pacientesLunes, pacientesMartes, pacientesMiercoles, pacientesJueves, pacientesViernes)

#8) Calcular el promedio de personas que no fueron atendidas.
promedioExcedente = l.calcularPromedioDesatencion(difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes)

#9) Desborde máximo del servicio.
desbordeMax = l.calcularDesbordeMayor(difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes)

#10) Presentar informe (indicadores solicitados)
inter.presentarInforme(promedioExcedente, desbordeMax)