#Solicitar al usuario una cadena y revisar
#si esta es palíndroma (su versión invertida es igual
#a la original) 

cadena = input("Ingresar una cadena: ")

if cadena == cadena[::-1]:
    print("Cadena es palíndroma!")
else:
    print("No lo es!!!")
    
print(f"Cadena revisada -> {cadena}")