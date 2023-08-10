#Variables -> Entidad (procesar)
nombre = "Camila"
edad = 30
becada = True
promedio = 4.8

#Representar Otra Persona
persona = dict()
persona['nombre'] = 'Manuel' 
persona['edad'] = 42
persona['promedio'] = 4.9
persona['estudios'] = { 'colegio':'Otro Colegio',
                     'profesional': 'UTP',
                     'especializacion': 'SantiagoChile'
                     
        }

persona2 = {
        'nombre' : 'Alejandra',
        'becada' : True,
        'promedio' : 4.8,
        'estudios' : { 'colegio':'Institución',
                         'profesional': 'UTEC',
                         'especializacion': 'Montevideo',
                         'maestria':'UniAndes'
            }
    }

def procesarPersona(nombre,
                    edad,
                    becada,
                    promedio):
    print("Paso1")
    print("Paso2")
    return 1

def procesarPersona2(persona):
    pass

