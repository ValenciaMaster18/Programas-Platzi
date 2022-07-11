def divisores(num):
    divisor = []
    try:
        if num < 0 or num ==0:
            raise ValueError("El numero tiene que ser positivo y mayor a 0")
        else:
            for i in range (1, num +1):
                if num % i == 0:
                    divisor.append(i)
            return divisor
    except ValueError as ve:
        print (ve)


    # divisores = [i for i in range (1, num+1) if num%i==0] 
    # return divisores


def run():

    try:
        num = int(input("Ingresa un numero positivo: "))
        print (divisores(num))
        print ("Programa finalizado  ")
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == "__main__":
    run()