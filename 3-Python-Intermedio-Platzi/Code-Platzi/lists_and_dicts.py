def main():
    super_list =[
        {"First name":"Luis","Last name":"Valencia"},
        {"First name":"Daniel","Last name":"Manzanero"},
        {"First name":"Eduardo","Last name":"Ramirez"},
    ]

    super_dist ={
        "Integer numbers":[1,2,3,4,5,6,7],
        "Decimal numbers":[1,2,3,4,5,6,7],
    }
    # Recorrer el diccionario con valores de listas
    """_summary_
    Listas y diccionarios anidados
    """
    for keys , value in super_dist.items():
        print (keys ,"-",value)
    
    # Recorrer la lista con estructura de diccionario    
        for x in super_list:            
            print (x)

if __name__ == "__main__":
    main()
    
