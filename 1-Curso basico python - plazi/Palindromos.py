def palindromo(palabra):
    palabra = palabra.replace(" ","").lower()
    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False 


def run():
    print ("""Bienvenido
Este un programa de palindromo
           """)
    repeticiones = int(input("Cuantas palabras desea evaluar: "))
    for cantidad in range (repeticiones):
        palabra = input("Escribe una palabra: ")
        if palindromo(palabra):
            print ("Es un palindromo")
        else:
            print ("No es un palindromo")
    

if __name__ == "__main__":
    run()


# edades = [10,5,4,8,9,4,1]
# edades.sort()
# frase = "Hola mundo"
# for i in edades[-4::]:
#     print(i,end=",")
