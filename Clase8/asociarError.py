#Revisar el tipo de dato de una variable:
#Estoy esperando que la variable sea
#tipo float, pero la variable es tipo entero.
#Si es tipo entero, debo reportar un error.

x = 17.0

try:    
    #Problemática
    if not type(x) is float:
        raise TypeError("Se esperaba que X fuera de tipo flotante!!!")     
except Exception as err:
    
    print("----------------------------------------")
    print("Detalle del error: ")
    print(err)
    print("Tipo del error que fue generado: ")
    print(type(err))
    print("----------------------------------------")
    
    #Reporto y me recupero del error
    print("Recast de x para recuperación")
    
    try:
        x = float(x)
    except ValueError:
        print("Recuperar dando un valor inicial")        
        x = float()
    
else:
    #Si todo salió bien (solamente)
    pass
finally:
    #Siempre se realizan 
    #(no importa si fue exitosa o 
    #no la instrucción problmática)
    
    #Liberación de recursos
    pass

print("Reporte del estado final de X")
print("Tipo de dato de x -> ",type(x))
print("Contenido de x -> ",x)

print("************************************")
print("Acciones después de la estructura de control try!!!")
print("Acciones después de la estructura de control try!!!")
print("Acciones después de la estructura de control try!!!")
    