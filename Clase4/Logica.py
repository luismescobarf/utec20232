def calcularExcedentesDiasHabiles(capacidadAtencion,
                                  pacientesLunes,
                                  pacientesMartes,
                                  pacientesMiercoles,
                                  pacientesJueves,
                                  pacientesViernes                  
                                  ):

    #7) Obtener personas sin atender para cada día.
    difUsuariosLunes = pacientesLunes - capacidadAtencion
    difUsuarioMartes = pacientesMartes - capacidadAtencion
    difUsuarioMiercoles = pacientesMiercoles - capacidadAtencion
    difUsuarioJueves = pacientesJueves - capacidadAtencion
    difUsuarioViernes = pacientesViernes - capacidadAtencion
    
    return  difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes  

def calcularPromedioDesatencion(difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes):    

    #8) Calcular el promedio de personas que no fueron atendidas.
    excedenteAcumulado = sum([difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes])
    promedioExcedente = excedenteAcumulado / 5
    
    return promedioExcedente

def calcularDesbordeMayor(difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes):
    
    #9) Desborde máximo del servicio
    desbordeMax = max([difUsuariosLunes, difUsuarioMartes, difUsuarioMiercoles, difUsuarioJueves, difUsuarioViernes])
    
    return desbordeMax






