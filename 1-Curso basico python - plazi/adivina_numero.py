import random

def run():
    numero_aletorio = random.randint(1,100)
    print ("""BIENVENIDO      
Programa para adivianar el numero aleatorio tienes 5 vidas 
    """)
    numero_elegido = int(input("Digite un numero del 1 al 100: "))
    
    vidas = 5 
    intentos = 1
    
    while numero_elegido != numero_aletorio:
        vidas -= 1
        intentos +=1
        if vidas == 0:
            print (f"Tus vidas se agotaron el numero era el {numero_aletorio}")
            break
        elif numero_elegido <1 or numero_elegido >100:
            print(f"Perdistes rango de numero invalido era el {numero_aletorio}")
            break
        elif numero_elegido > numero_aletorio:
            print (f"El numero es menor a {numero_elegido}")
        elif numero_elegido < numero_aletorio:
            print (f"El numero es mayor a {numero_elegido}")
        print (f"Te quedada {vidas} vidas")
        numero_elegido = int(input("Escriba otro numero: "))
    if numero_elegido == numero_aletorio:    
        print (f"Ganastes numero de intentos {intentos}!!")


if __name__ == "__main__":
    run()