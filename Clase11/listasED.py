#cadena = "letras hola "
animales = ['loro',
            'gato',
            'perrT',
            300,
            0.10,
            True,
            [],
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
    if isinstance(elemento, int):
        print(f"La posición {i} es de tipo int")
    elif isinstance(elemento, str):
        print(f"La posición {i} es de tipo str")
    elif isinstance(elemento, float):
        print(f"La posición {i} es de tipo float")
    else:
        print(f"Tipo no soportado por el programa en la posicion {i}")
        
