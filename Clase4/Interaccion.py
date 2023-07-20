def capturarInfoPuestoSalud():
    
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
    
    #Retornar toda la info capturada
    return capacidadAtencion, pacientesLunes, pacientesMartes, pacientesMiercoles, pacientesJueves, pacientesViernes 


def presentarInforme(promedioExcedente,desbordeMax):
    #10) Presentar informe (indicadores solicitados)
    print("-------------------------------------")
    print(f"Promedio de personas sin atender: {promedioExcedente}")
    print(f"Desborde máximo en un día: {desbordeMax}")
    print("-------------------------------------")




