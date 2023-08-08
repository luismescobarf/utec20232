def calcularCobroAgua(consumo:int,estrato:int) -> float:
    
    tarifaMetroCubico = 980
    
    #Revisar el estrato
    if estrato <= 3:
        if consumo <= 33:
            if estrato == 1:
                return (consumo * 980) * 0.5
            elif estrato == 2:
                return (consumo * 980) * 0.6
            elif estrato == 3:
                return (consumo * 980) * 0.75
        else:
            #Estratos 1,2 y 3 excediendo el consumo y recibiendo tarifa completa            
            return (consumo * 980)
    
    #Estratos 4 a 6
    else:
        if consumo < 33:
            #Incentivo para estratos 4 a 6
            return (consumo * 980) * 0.95
        else:
            #Estratos 4,5 y 6 excediendo el consumo y recibiendo tarifa completa                        
            return (consumo * 980)
        
#Sección principal
#-----------------
print(calcularCobroAgua(12,3))
print(calcularCobroAgua(40,5))
print(calcularCobroAgua(10,6))
print(calcularCobroAgua(33,2))
print(calcularCobroAgua(100,1))

