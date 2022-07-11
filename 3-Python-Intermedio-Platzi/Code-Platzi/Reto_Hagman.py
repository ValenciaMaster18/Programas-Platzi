import random
import os
from re import A

def words_random():
    words = []
    with open("./archivos/palabras_hagman.txt","r",encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip())
    return random.choice(words)


def save_word():
    word = words_random () # Estoy guardando mi palabra al azar en esta variable
    unknown_word = len(word) * "_" # Esto va crear unos guiones dependiendo los caracteres de la palabra
    return word,unknown_word
    

""""
Ahora creamos una funcion que compare si la palabra ingresada esta en palabra la remplace y 
la ubique en la posicion que tiene que estar
"""

def replace_letter(word,unknown_word,letter):
    number_of_letter = word.count(letter)
    beginner = 0
    for i in range(number_of_letter):
        position = word.find(letter,beginner)
        unknown_word = unknown_word[:position] + letter + unknown_word [position + 1:]
        beginner = position + 1
    return unknown_word 


"""_summary_
FUNCIONAMIENTO DEL JUEGO
"""
def hagman():
    word , unknown_word = save_word()
    fails = 0
    while unknown_word != word and fails <= 5:
        print("Palabra: " + unknown_word)
        guess = input ("Ingresa una letra ")
        os.system("cls")
        if guess in word:
            unknown_word = replace_letter(word,unknown_word,guess)
        else:
          fails += 1
    
    if unknown_word == word:
        print ("""
                              _  
                             | |       
   __ _  __ _ _ __   __ _ ___| |_ ___  
  / _` |/ _` | '_ \ / _` / __| __/ _ \ 
 | (_| | (_| | | | | (_| \__ \ ||  __/ 
  \__, |\__,_|_| |_|\__,_|___/\__\___| 
   __/ |                               
  |___/                                
             
               """)
    else:
        print ("""   
                     _ _     _       
                    | (_)   | |      
  _ __   ___ _ __ __| |_ ___| |_ ___ 
 | '_ \ / _ \ '__/ _` | / __| __/ _ \
 | |_) |  __/ | | (_| | \__ \ ||  __/
 | .__/ \___|_|  \__,_|_|___/\__\___|
 | |                                 
 |_|                                 
               """)            

print("""   
  _    _                           
 | |  | |                                  
 | |__| | __ _  __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` |/ _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|\__, |_| |_| |_|\__,_|_| |_|
                __/ |                      
               |___/                       
     
      """)
answer = input("Ingrese una x para empezar: ").lower()
if answer == "x":
    print("""
          
       _                          _____            _           _       
      | |                        |_   _|          (_)         | |      
      | |_   _  ___  __ _  ___     | |  _ __   ___ _  __ _  __| | ___  
  _   | | | | |/ _ \/ _` |/ _ \    | | | '_ \ / __| |/ _` |/ _` |/ _ \ 
 | |__| | |_| |  __/ (_| | (_) |  _| |_| | | | (__| | (_| | (_| | (_) |
  \____/ \__,_|\___|\__, |\___/  |_____|_| |_|\___|_|\__,_|\__,_|\___/ 
                     __/ |                                             
                    |___/                                              
         
          """)
else:
    print("""
    _                                                   _           _       
   (_)                                                 | |         | |      
    _ _   _  ___  __ _  ___     ___ __ _ _ __   ___ ___| | __ _  __| | ___  
   | | | | |/ _ \/ _` |/ _ \   / __/ _` | '_ \ / __/ _ \ |/ _` |/ _` |/ _ \ 
   | | |_| |  __/ (_| | (_) | | (_| (_| | | | | (_|  __/ | (_| | (_| | (_) |
   | |\__,_|\___|\__, |\___/   \___\__,_|_| |_|\___\___|_|\__,_|\__,_|\___/ 
  _/ |            __/ |                                                     
 |__/            |___/                                                                               
          """)
      
def run():
    hagman()

if __name__ == "__main__":
    run()