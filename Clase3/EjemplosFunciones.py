#Definir función
def sumarDosNumeros(a,b):
    # resultado = a + b
    return a + b

def restarDosNumeros(a=0,b=7):
    return a - b

#Llamados

#1) Envío de parámetros según su posición
resultado = restarDosNumeros(3,5)
print(f"El resultado de la operación es {resultado}")

#2) Envío de parámetros según su nombre
resultado = restarDosNumeros(b=3,a=5)
print(f"El resultado de la operación es {resultado}")

#3a) Llamar la función sin satisfacer todos los parámetros envío por orden
resultado = restarDosNumeros(12)
print(f"El resultado de la operación es {resultado}")

#3b) Llamar la función sin satisfacer todos los parámetros envío por nombre
resultado = restarDosNumeros(b=12)
print(f"El resultado de la operación es {resultado}")


