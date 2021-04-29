# reto : proyecto en el cual se toma una lista y se ouede filtar los trabajadores por su diferentes keys 
# como tipo de lenguage , eda y otras cosas 
import time 
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    inicio()
    respuesta = int(input('ingresa una opcion '))
    while True :
        if respuesta == 1 : 
            try:
                lenguajes_que_hay = [x['language'] for x in DATA ] 
                print(list(set(lenguajes_que_hay)))
                legunje = input('que lengaje quieres filtar  ?? '.lowe() )
                legunje_ele = [x for x in DATA if x['language'] == legunje ]
                for i in legunje_ele:
                    print(i)
                break 
            except:
                print('err')
        if respuesta== 2 : 
            try: 
                
                edad= int(input('dime la edad en la que quieres que sse filtren los trabajadores ?? '))
                edades= [x for x in DATA if x['age'] > edad]
                #edades= [x[] for x in DATA if x['age'] > edad]
                for i in edades :
                    print(i)
                break 
            except:
                print( '\n ha ocurriod un erro , vuleve a intertarlo \n')
        if respuesta == 3 :
            companias =[x['organization'] for x in DATA  ]
            print(list(set(companias)))  # con esta fucnion lo que hacemos es que los valores que se reputen los borra 
            compania =  input('dime una compania a filtar ')
            compania = compania.title()
            compania_elegida= [i for i in DATA if i['organization'] == compania]
            print(compania_elegida)
            pregunta = input(' \n quieres saber solo el nombre de los trabajadores (si / no ) ?? ')
            
            if pregunta == 'si' :
                soloName = list(map(lambda x: x['name'] , compania_elegida ))
                print(soloName)
            else:
                print('devolviendote a la central ....')
                time.sleep(4)
                run()

            
            break 
            

            
                

        else: 
            run()








def inicio ():
    print(''' 
    Bienvenido a programadores.py
     - que quieres buscar ?
     1) filtar programadores por lenguajes  de programacion
     2) filtar programadores por edades
     3) filtar programadores por organizacion en la que trabajan  ''')
run()