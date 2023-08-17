import random
#cadena = "letras hola "
animales = ['loro',
            'gato',
            'perrT',
            300,
            0.10,
            True,
            [],
            23,
            'mono',
            False
            ]

#Acceder al primer elemento
print(animales[0])

#Acceder a la primera letra de la primera palabra
print("Primera letra primera palabra")
print(animales[0][0])

#Acceder a la última letra de la tercera palabra
print("última letra de la tercera palabra")
print(animales[2][-1])

#Avisar el tipo de dato de cada elemento de la lista
for i, elemento in enumerate(animales):
    if isinstance(elemento, int) and type(elemento) != bool:    
        print(f"La posición {i} es de tipo int")        
        
        #Incrementar solamente los enteros de mi lista
        animales[i] += 1        
        
    elif isinstance(elemento, str):
        print(f"La posición {i} es de tipo str")
    elif isinstance(elemento, float):
        print(f"La posición {i} es de tipo float")
    elif isinstance(elemento, list):
        print(f"La posición {i} es de tipo lista")
        
        #Agregar un número aleatorio a la lista dentro de la lista
        animales[i].append( random.randint(1,10) )
    
    else:
        print(f"Tipo no soportado por el programa en la posicion {i}")
        
#Probar otras operaciones de actualización

#Eliminar el último elemento de una lista
animales.pop()

#Insertar en cierta posición un elemento
elemento = ['Pepe','Carla','Cecilia','Aldo']
animales.insert(3,elemento)



        

        
