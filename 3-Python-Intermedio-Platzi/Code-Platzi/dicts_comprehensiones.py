def run():
    # mi_dicts = {}
    
    # for i in range(1,101):
    #     if i%3 !=0:
    #         mi_dicts[i] = i**3
    # print(mi_dicts)

    # diccionario comprehensions
    mi_dicts = {i: i**3 for i in range(1,101) if i%3!=0}
    print(mi_dicts)
    

if __name__ == "__main__":
    run()
    

# Reto
    """
    Crear un diccionario comprehension un diccionario cuyas llaves sean 1000 primeros 
    numeros naturales con sus raices cuadradas
    """
# Importamos el modulo match

import math

def main():
    
    root = {i: round(math.sqrt(i),2) for i in range(1,1001)}
    print(root)
    
    # Recorrer el diccionario con un bucle for
    for keys , value in root.items():
        print(f"La raiz cuadrada de {keys} es {value}")


if __name__ == "__main__":
    main()