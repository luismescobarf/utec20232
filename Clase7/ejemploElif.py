#Requerimiento: Implementar un menú de consola para elegir diferentes opciones. Cuando se ingrese el valor 1, ingresar a la opción de añadir, la 2 la opción de leer, la 3 de actualizar, la 4 de salir y si se ingresa un valor diferente avisar que se trata de una opción inválida.

def mostrarOpciones():
  print("----------------")
  print("1) Añadir")
  print("2) Consultar/Leer")
  print("3) Actualizar")
  print("4) Salir")
  print("----------------")
  

#Sección principal
mostrarOpciones()
opcion = int(input("Ingrese opción: "))

"""
if opcion == 1:
  print("Sección añadir")
else:
  if opcion == 2:
    print("Sección lectura ")
  else:
    if opcion == 3:
      print("Sección actualización ")
    else:
      if opcion == 4:
        print("Salida exitosa")
      else:
        print("Opción inválida")
"""

if opcion == 1:
  print("Sección añadir")
elif opcion == 2:
  print("Sección lectura ")
elif opcion == 3:
  print("Sección actualización ")
elif opcion == 4:
  print("Salida exitosa")
else:
  print("Opción inválida")

print("Fin de la aplicación")

"""
- Sin utilizar cadenas o string, determinar mediante condicionales
si un número es de 1 cifra, 2 cifras, 3 cifras o más de tres cifras
"""


  