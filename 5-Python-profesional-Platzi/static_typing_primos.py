def prime_number(num: int) ->bool:
    list_prime = [i for i in range(1,num+1) if num%i==0]
    result_list = len(list_prime)==2
    
    if result_list == True:
        print (num, "Es un numero primo")
    else:
        print (num, "No es un numero primo sus divisores son", list_prime)



def main():
    answer = input("Digite un numero: ")
    num: int = int(answer)
    
    if num >=1:
        print(prime_number(num))
    


if __name__ == "__main__":
    main()