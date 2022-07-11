def divisores(num):
    divisor = []
    for i in range (1, num +1):
        if num % i == 0:
            divisor.append(i)
        return divisor


    # divisores = [i for i in range (1, num+1) if num%i==0] 
    # return divisores
"""
    Es una alternativa al try. 
    En este caso se usa un metodo de los string para comprobar que el dato ingresado es un numero.
    Nota
    Lo que pude aprecir es que el metodo isnumeric() solo cuando es un numero entero positivo 
    del resto develve false, asi que no hay necesidad de evaluar di el numero es ingresado es 
    negativo ya la isnumeric lo hace por nosotros:
"""

def run():
        num = input("Ingresa un numero positivo: ")
        assert num.isnumeric(),"Ingrese un numero entero positivo" 
        print (divisores(int(num)))
        print ("Programa finalizado  ")


if __name__ == "__main__":
    run()