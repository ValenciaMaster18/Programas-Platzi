def run():
    # squares = []
    
    # for x in range (1,101):
    #     if x %3 !=0:
    #         squares.append(x**2)
    # print(squares)
    squares =[ x**2 for x in range (1,101) if x%3!=0]
    print (squares)

if __name__ == "__main__":
    run()

# Reto
    """
     List comprehensions de todos los multiplos de 4 que a su vez son 
     multiplos de 6 y 9 hasta de 5 digitosv
    """
    
def run():
    multiples = [i for i in range (1,100) if i%36==0]
    print (multiples)
   
   
   
if __name__ == "__main__":
    run()
