def prestamo(informacion:dict) -> dict:
    
    #Preprocesamiento (copias locales de los valores del diccionario)
    # dependientes = int()
    # if isinstance(informacion['dependientes'], int):
    #     #Acción cuando es verdadera la sentencia
    #     dependientes = informacion['dependientes']
    # else:
    #     dependientes = 3    
    dependientes = informacion['dependientes'] if isinstance(informacion['dependientes'], int) else 3
    
    #Diccionario de aprobación
    dAprobado = {'id_prestamo': informacion['id_prestamo'], 'aprobado': True}
    #Diccionario de rechazo
    dRechazo = {'id_prestamo': informacion['id_prestamo'], 'aprobado': False}
    
    #Árbol de decisiones (retornos)
    if informacion['historia_credito'] == 1:
        if informacion['ingreso_codeudor']>0 and informacion['ingreso_deudor'] / 9 > informacion['cantidad_prestamo']:
            return dAprobado
        else:
            if dependientes > 2 and informacion['independiente'] == 'Si':                
                return dAprobado if informacion['ingreso_codeudor'] / 12 > informacion['cantidad_prestamo'] else dRechazo
            else:
                return dAprobado if informacion['cantidad_prestamo'] < 200 else dRechazo                                
                
    else:
        if informacion['independiente'] == 'Si':
            if not( informacion['casado'] == 'Si' and dependientes > 1):
                if informacion['ingreso_deudor'] / 10 > informacion['cantidad_prestamo'] or informacion['ingreso_codeudor'] / 10 > informacion['cantidad_prestamo']:                    
                    
                    return dAprobado if informacion['cantidad_prestamo'] < 180 else dRechazo
                    
                else:
                    return dRechazo
            else:
                return dRechazo
        else:
            if not(informacion['tipo_propiedad'] == 'Semi Urbana') and dependientes < 2:
                if informacion['educacion'] == 'Graduado':                    
                    return dAprobado if informacion['ingreso_deudor'] / 11 > informacion['cantidad_prestamo'] and informacion['ingreso_codeudor'] / 11 > informacion['cantidad_prestamo'] else dRechazo
                    
                else:
                    return dRechazo
            else:
                return dRechazo
                
    

#Sección principal
#-----------------

casoPrueba1 = {
    'id_prestamo':'RETOS2_001',
    'casado':'No',
    'dependientes':1,
    'educacion':'Graduado',
    'independiente':'Si',
    'ingreso_deudor':4692.0,
    'ingreso_codeudor':0,
    'cantidad_prestamo':106.0,
    'plazo_prestamo':360,
    'historia_credito':1,
    'tipo_propiedad':'Rural'    
}

print(prestamo(casoPrueba1))

casoPrueba2 = {
    'id_prestamo':'RETOS2_002',
    'casado':'No',
    'dependientes':'3+',
    'educacion':'No Graduado',
    'independiente':'No',
    'ingreso_deudor':1830.0,
    'ingreso_codeudor':0,
    'cantidad_prestamo':100.0,
    'plazo_prestamo':360,
    'historia_credito':0,
    'tipo_propiedad':'Urbano'    
}

print(prestamo(casoPrueba2))

casoPrueba3 = {
    'id_prestamo':'RETOS2_003',
    'casado':'No',
    'dependientes':0,
    'educacion':'No Graduado',
    'independiente':'No',
    'ingreso_deudor':3748.0,
    'ingreso_codeudor':1668,
    'cantidad_prestamo':110.0,
    'plazo_prestamo':360,
    'historia_credito':1,
    'tipo_propiedad':'Semi Urbana'    
}

print(prestamo(casoPrueba3))
