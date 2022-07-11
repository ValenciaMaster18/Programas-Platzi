def area_triangulo(base, altura):
    return (base*altura)/2

triangulo1 = area_triangulo(6,5)
triangulo2 = area_triangulo(4,5)
print(triangulo1)
print(triangulo2)

"""
    Ahora para el ejemplo de lambda vamos a simplificar
    la anterior funcion de la siguiente forma:
"""
area_triangulo = lambda base,altura: (base*altura)/2
print(area_triangulo(7,5))
