"""
High Order Functions
Funciones que reciben como parámetro otra función

Filter
devuelve True or False según el valor esté dentro de los criterios 
buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista 
se verá reducida por este filtro.
"""
"""
Dada una lista de numeros filtra para quedarte solo con 
los números impares
"""

my_list = [i for i in range(10)]

# Usando def
def get_odds(arr):
    odds = []
    for n in arr:
        if n % 2 == 1:
            odds.append(n)
    return odds

# Usando List Comprehension
odds = [n for n in my_list if n % 2 == 1]

# Usando Filter
odds_filter = list(filter(lambda n: n % 2 == 1, my_list))
print(odds_filter)
"""
Map
Funciona muy parecido, pero su diferencia radica en que no puede eliminar 
valores de la lista del array entregado. Es decir, el output tiene la misma 
cantidad de valores que el input.
"""

"""
Obtener todos los numeros de una lista multiplicados al cuadrado
"""

# Usando Def
def get_squares(arr):
    squares = []
    for n in arr:
        squares.append(n * n)
    return squares

# Usando List Comprehension
squares = [n * n for n in my_list]

# Usando Map
squares_map = list(map(lambda x: x*x, my_list))
print(squares_map)
"""
Reduce
Toma 2 valores entregados como parámetros y el iterador como otro parámetro. 
Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor
que le sigue en el array. Y así hasta pasar por todos los valores de la lista.
"""
"""
Suma todos los valores de una lista
"""
from functools import reduce

# Usando def
def get_sum(arr):
    result = 0
    for n in arr:
        result += n
    return result

# Usando Reduce
sum = reduce(lambda a, b: a + b, my_list)
print(sum)
