"""
    Proyecto: filtrando datos.
    Tenemos una lista con diccionarios sobre distintas personas. 👀
    Cuando en Python colocamos una variable en mayúsculas, significa que
    no esperamos modificarla, esto es, es una constante ⛵.
    El operador pipe | te permite unir un diccionario viejo con uno nuevo, y es un feature
    nuevo de python 3.9 🤯 (sumar diccionarios).

Solución al reto:
"""

from multiprocessing import allow_connection_pickling
from tkinter import W


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
        'position': 'Support',
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
    
    #list comprehension
    
   
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    
    
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    
    # agregar una llave y un valor al dicionario 
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    
    
    for worker in old_people:
        print(worker)
    


if __name__ == '__main__': 
    run()
    
# Reto
"""    
Crear las listas all_platzi_workers y all_python_devs usando una combinacion de filter y map

crear la lista old_people y adults con list comprehension
"""

def main():
     allow_py_devs = list(filter(lambda worker: worker ["language"] == "python",DATA))
     allow_py_devs = list(map(lambda worker: worker["name"],allow_py_devs))
     
     adult = [worker["name"] for worker in DATA if worker["age"]>18 ]
     print(adult)
     
     old = [ {**worker, **{"old": worker["age"] > 70}} for worker in DATA]
     print(old)
     
     for worker in allow_py_devs:
         print(worker)


if __name__ == "__main__":
    main()