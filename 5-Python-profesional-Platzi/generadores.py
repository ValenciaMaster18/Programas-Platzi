import time

def fibo_gen():
    a = 0
    b = 1
    contador = 0
    
    while True:
        if contador == 0:
            contador += 1
            yield a
        elif contador == 1:
            contador += 1
            yield b
        else:
            auxiliar = a + b
            a , b = b , auxiliar
            contador +=1
            yield auxiliar


def main():
    fibonacci = fibo_gen()
    for elemento in fibonacci:
        print(elemento)
        time.sleep(1)


if __name__ == "__main__":
    main()