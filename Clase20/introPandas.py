import numpy as np
import pandas as pd
import random
import pprint as pp

nombres = ['Homero','Marge','Lisa','Juan','Pedro']
apellidos = ['Suarez','López','Escobar','Vélez']
numeroPersonas = 10

#Primeras series
serieNombres = pd.Series( [random.choice(nombres) for _ in range(numeroPersonas)] )
serieApellidos = pd.Series( [random.choice(apellidos) for _ in range(numeroPersonas)] )
serieCalificaciones = pd.Series( [random.randint(0,3) for _ in range(numeroPersonas)] )
print()
print(serieNombres)
print()
print()
print(serieApellidos)
print()

#Primer dataframe -> Colección nombrada de Series (diccionario de series)
diccionarioColumnas = { 'Nombre':serieNombres,
                        'Apellido':serieApellidos,
                        'Calificaciones':serieCalificaciones
                        }

df = pd.DataFrame(diccionarioColumnas)
print("Estado inicial del dataframe")
print(df)

print("Bonificación a las calificaciones 0.5")
df['Calificaciones'] = df['Calificaciones'] + 0.5
print(df)