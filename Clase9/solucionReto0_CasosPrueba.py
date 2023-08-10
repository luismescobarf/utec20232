########
#Reto 0#
########
#(Se omiten tildes para evitar problemas de codificacion)

#Tipado de la funcion
def empaquetador(porcentajeAjuste: float, largo1: float, largo2: float, largo3: float, largo4: float) -> str:

    #Calcular las áreas de los 
    areaPieza1 = largo1 * largo1
    areaPieza2 = largo2 * largo2
    areaPieza3 = largo3 * largo3
    areaPieza4 = largo4 * largo4
    
    #Promedio
    promedioArea = (areaPieza1 + areaPieza2 + areaPieza3 + areaPieza4) / 4
    
    #Variable que calcula el area del pedido si se realiza
    areaEmpaquetado = 0
    
    #Numero de piezas aptas
    piezasAprobadas = 0
    
    #Calculo de area permitida para las piezas
    diferenciaAreaPermitida = porcentajeAjuste * promedioArea
    
    #Revisar pieza 1
    if abs(promedioArea - areaPieza1) <= diferenciaAreaPermitida:
        piezasAprobadas = piezasAprobadas + 1
        areaEmpaquetado = areaEmpaquetado + areaPieza1    
    
    #Revisar pieza 2
    if abs(promedioArea - areaPieza2) <= diferenciaAreaPermitida:
        piezasAprobadas = piezasAprobadas + 1
        areaEmpaquetado = areaEmpaquetado + areaPieza2    
    
    #Revisar pieza 3
    if abs(promedioArea - areaPieza3) <= diferenciaAreaPermitida:
        piezasAprobadas = piezasAprobadas + 1
        areaEmpaquetado = areaEmpaquetado + areaPieza3    
    
    #Revisar pieza 4
    if abs(promedioArea - areaPieza4) <= diferenciaAreaPermitida:
        piezasAprobadas = piezasAprobadas + 1
        areaEmpaquetado = areaEmpaquetado + areaPieza4    
    
    #Tomar decisiones para la salida
    if piezasAprobadas < 2:
        return f"Embalaje descartado {4 - piezasAprobadas} piezas no ajustan"
    else:
        return f"Embalaje confirmado: piezas aprobadas = {piezasAprobadas}, superficie ocupada = {areaEmpaquetado}" 

#Casos de prueba empaquetamiento (públicos)
print(empaquetador(0.2,	30,	30,	30,	30))
print(empaquetador(0.5,	30,	10,	20,	25))
print(empaquetador(0.8,	30,	10,	20,	25))
print(empaquetador(0.8,	30,	10,	5,	30))
print("--------------------------------")
##Casos de prueba empaquetamiento (ocultos)
#print(empaquetador(0.2,	55,	66,	77,	88))
#print(empaquetador(0.1,	55,	66,	77,	88))
#print(empaquetador(0.5,	100,70,	55,	70))
#print(empaquetador(0.5,	10.1,	10.5,	12.8,	7.7))
#print(empaquetador(1,	1,	1,	1,	1))





    

