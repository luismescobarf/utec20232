import numpy as np

#Generar nuestras primeras colecciones de tipo arreglo de numpy
listaCompuesta = [ [1,2] , [3,4] ]
arreglo1 = np.array(listaCompuesta)
print(f"Dimensiones: {np.shape(arreglo1)}")

#Acceso a los elementos
print(listaCompuesta[0][1])
print(arreglo1[0,1])

#Reshape -> 
print(np.reshape(arreglo1,4))

#Generaciones automáticas
matrizCeros = np.zeros((5,3))
print(matrizCeros)

matrizUnos = np.ones((5,3))
print(matrizUnos)

print(np.arange(1,10,2))

coleccionEquidistan = np.linspace(1,10,7)
print(coleccionEquidistan)

print(np.random.randint(5,size=20))

matrizAleatoria = np.random.randint(-10,5,size=(6,6))
print(matrizAleatoria)

for fila in matrizAleatoria:
    for columna in fila:
        print(columna," ", end='')
    print()
    
frutas = ['manzana','pera','limón','feijoa','narnja']
print(np.random.choice(frutas, (3,3)))

print(np.random.choice(frutas, (3,3), p=[0.6,0.1,0.1,0.1,0.1]))

matrizOperaciones = np.random.randint(0,3,size=(3,3))
print(matrizOperaciones)

# #Suma de las filas
# print(np.sum(matrizOperaciones,axis=0))

# #Suma de las filas
# print(np.sum(matrizOperaciones,axis=1))

# #Rangos -> Excel
# print("Sumatoria de la tercera columna: ")
# print(np.sum(matrizOperaciones[:,2]))

# submatriz = matrizOperaciones[0:2,0:2]
# print(submatriz)

# print("Diagonal: ")
# print(matrizOperaciones.diagonal())

# print("Espejo columnas: ")
# print(np.fliplr(matrizOperaciones))

# print("Diagonal secundaria: ")
# print(np.fliplr(matrizOperaciones).diagonal())

# print("Espejo filas: ")
# print(np.flipud(matrizOperaciones))

# print("Transpuesta:")
# print(np.transpose(matrizOperaciones))

# #Generalizar operaciones a la colección
# resultado = matrizOperaciones + 5
# print(resultado)

# #Revisar si se cumple alguna condición
# filtro = matrizOperaciones == 1
# print()
# print(filtro)

# #Filtro 2
# casillasCumplen = np.where(matrizOperaciones == 1)
# print(casillasCumplen)

#Dejar únicamente los elementos que cumplen
print(matrizOperaciones[ matrizOperaciones == 1 ])





