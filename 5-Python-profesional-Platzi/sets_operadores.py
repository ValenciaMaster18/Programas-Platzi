def main():
    num1 = {1,2,3,4,5,6,7,0}
    num2 = {1,2,3,5,9,8}

    """
    Uniòn |
    """
    num3 = num1 | num2
    print("Union:   ",num3)
    
    """
    Intersecciòn &
    """
    num4 = num1 & num2
    print("Interseccion: ",num4)
    
    """
    Diferencia -
    """
    num5 = num1 - num2
    print("Diferencia: ",num5)
    
    """
    Diferencia Simetrica ^
    """
    num6 = num1 ^ num2
    print("Diferencia simetrica: ",num6)
    
    
if __name__ == "__main__":
    main()