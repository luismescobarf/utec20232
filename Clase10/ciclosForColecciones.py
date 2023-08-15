#5) Recorrer y mostrar en pantalla todos 
#los elementos de una colección ordenada (cadena)

palabra = "casa"
palabra = "Montevideo"
for i in range(len(palabra)):
    print(f"Subíndice: {i} Contenido: {palabra[i]}")
    
print("-----------------")

i = 0
while i < len(palabra):
    print(f"Subíndice: {i} Contenido: {palabra[i]}")
    i = i + 1
    
#5b) Recorrer y mostrar en pantalla  
#los elementos alternados de una colección 
#ordenada (cadena)
print("Requerimiento de alternancia:::::::")
for i in range(0,len(palabra),2):
    print(f"Subíndice: {i} Contenido: {palabra[i]}")
    
#6) Imprimir TODOS los 
#caracteres de una palabra por separado
print("%%%%%%%%%%%%%%%%%%%")
for letra in palabra:
    print(letra)
print("%%%%%%%%%%%%%%%%%%%")

#7) Imprimir TODOS los 
#caracteres de una palabra por separado y su posición
print("..................")
for i,letra in enumerate(palabra):
    print(f"Subíndice: {i} Contenido: {letra}")    
print("..................")



print("Proceso posterior al ciclo para")



