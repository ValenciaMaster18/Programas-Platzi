def run():
    divisors = lambda num: [x for x in range(1, num + 1) if num % x == 0]

    try:
        num = int(input('Ingresa un numero: '))
        if num < 0:
            raise ValueError('Solo ingresa numeros positivos')
        print(divisors(num))
        print("Termino")
    except ValueError:
        print('Solo Ingrese Numeros Positivos :|')

if __name__ == '__main__':
    run()