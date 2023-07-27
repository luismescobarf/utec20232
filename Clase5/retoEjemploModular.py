def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:

  
  
  #2) Detectar la peor de las notas y descartarla
  peorNota = min(nota1,nota2,nota3,nota4,nota5)
  
  #3) Calcular el promedio con las mejores notas
  promedio100 = (nota1+nota2+nota3+nota4+nota5-peorNota)/4
  
  #4) Convertirlo a escala de 0.0 a 5.0
  promedio5 = promedio100 / 20
  
  #5) Redondear a 2 cifras decimales para obtener la calificación
  promedio5 = round(promedio5,2)
  
  #6) Construir el mensaje con la calificación para el estudiante
  mensaje = "El promedio ajustado del estudiante "+codigo+" es: "+str(promedio5)

  #Retorno
  return mensaje  
  

def pendienteOtraFuncion():
  pass


#Algoritmo -> Requerimiento de promedio ajustado
#1) Recolectar notas y el código del estudiante
#2) Detectar la peor de las notas y descartarla
#3) Calcular el promedio con las mejores notas
#4) Convertirlo a escala de 0.0 a 5.0
#5) Redondear a 2 cifras decimales para obtener la calificación
#6) Construir el mensaje con la calificación para el estudiante

#Sección principal

#Recolectar notas y el código del estudiante
codigo = "AA0010276"
nota1 = 40
nota2 = 50
nota3 = 39
nota4 = 76
nota5 = 96

mensaje = nota_quices(codigo,nota1,nota2,nota3,nota4,nota5)

print(mensaje)







