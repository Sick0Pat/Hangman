from words import get_valid_word
import random
import string
import pyfiglet #HERNANDEZ CHIG JESUS LETRAS CON ASCII
from termcolor import colored
import os
from monito import monito_images
import time #Guillermo Islas Temporizador
import pyttsx3 #importar libreria con pip install pyttsx3
# PATRICK OWNER OF BASE HANGMAN REPOSITORY
## Instalar el termcolor 

#Erick Daniel Carrillo Jimenez
engine = pyttsx3.init() # se inicializa
engine.setProperty('rate',155) # se coloca la velocidad de reproduccion

## Alain Gonzalez Ambris 
def nombre():
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")

#Susana Robles
def clearHistory():
    file = open("match_history.txt", "a")
    file.seek(0)
    file.truncate()


def writeWins():
    file = open("match_history.txt", "a")
    file.write("You win!\n")
    file.close()
    file = open("match_history.txt", "r")
    history = file.read()
    wins = history.count("You win!")
    losses = history.count("You lose!")
    print(colored('Veces que te la has pellizcado:', 'magenta'), losses)
    print(colored('Veces que has sido digno:', 'blue'), losses)
    print("Veces que has jugado en total: ", losses + wins)
    file.close()


def writeLosses():
    file = open("match_history.txt", "a")
    file.write("You lose!\n")
    file.close()
    file = open("match_history.txt", "r")
    history = file.read()
    wins = history.count("You win!")
    losses = history.count("You lose!")
    print(colored('Veces que te la has pellizcado:', 'magenta'), losses)
    print(colored('Veces que has sido digno:', 'blue'), losses)
    print("Veces que has jugado en total: ", losses + wins)
    file.close() 

def borrarPantalla(): #Limpiar pantalla Dulce Badillo
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def hangman():
    # MAX ALVAREZ
    start = True  # Variable para empezar el juego al menos la primera vez
    while start:  # evalua si la variable es verdadera, en caso de que si, inicia el juego, de lo contrario lo termina
    # MAX ALVAREZ
       
        # Todo el codigo de abajo se ejecutara siempre y cuando no haya una interrupcion del teclado.
        try:

            #Cambio de Andres Karim Ruiz Del Cid: Agregar la funcionalidad de que el usuario elija una dificultad, si elige Easy, el programa le revelara algunas letras de la palabra
            print("Easy")
            print("Hard")
            difficulty = input("Choose the difficulty: ").upper()

            lives = 6
            word = get_valid_word()
            help = 1
            word_letters = set(word)

            alphabet = set(string.ascii_uppercase)
            used_letter = set()
            hangman_name = input("Choose a name for a hangman: ")# Erick vera - Nombre del hangman

           #Obtenemos la cantidad de la palabra
            quantity=len(word)
            if difficulty=="EASY":
                quantityBetween2=0
                wordRandom=''
                #dividimos entre 2 y ese valo lo metemos a un for
                quantityBetween2=quantity/2
                for f in range(int(quantityBetween2)):

                    #En este for, buscamos una cantidad X de letras dentro de la palabra de forma aleatoria
                    wordRandom=word[random.randrange(quantity)]
                for x4 in range(quantity):

                    if(wordRandom in word[x4]):
                        #Aqui las agregamos a las letras usadas para que el usuario tenga que poner menos letras
                        used_letter.add(wordRandom)
                        #aqui realizamos un ordenamiento para restarle las letras random a la palabra original y asi hacerla mas corta para que el usuario adivine en menos intentos
                        word_letters=word_letters-{wordRandom}
                        word_letters2=set(word_letters)
                        word_letters=word_letters2
                print("Welcome to easy version, you have "+str(lives)+" lives")
            elif difficulty=="HARD":
                print("Welcome to hard version, you have "+str(lives)+" lives")

            while len(word_letters) > 0 and lives > 0:
                
                
                
                time.sleep(2)
                borrarPantalla() #Dulce Badillo
                 # Mejora 1: Mensaje de bienvenida (Sáenz)
                print('*' * 55)
                bienvenida = pyfiglet.figlet_format('Hello welcome! This is the hangman game, good luck!')
                print(bienvenida)
                print('*' * 55)

                #Mejora de impresion de monito Roberto Ibarra
                print(monito_images[-lives-1])

                # Fabiola Vazquez - Mostrar las letras adivinas y faltantes
                word_list = [letter if letter in used_letter else '_' for letter in word]
                
                print('Current word: ', ' '.join(word_list))
                print('you have used these letters: ', ' '.join(used_letter))
                print("You have  " , lives,  "  lives left and you dead")
                
                print(hangman_name + ": You did it!!!") # Erick vera - Nombre del hangman
                
                user_letter = input("Guess a letter: ").upper()

                if len(user_letter) !=1 :
                    print("usa solo una letra")
                elif user_letter in alphabet - used_letter:
                    used_letter.add(user_letter)
                    
                    if user_letter in word_letters:

                        word_letters.remove(user_letter)
                    else:
                        lives = lives - 1
                        # Diana Colon
                        if lives == 1:
                            print("🤨  pobrecito te queda una vida") #Diana colon
                            #advertencia cuando queda una vida
                        # Gerardo Kim - Mostrar si la letra no esta en la palabra
                        print('\nYour letter,', user_letter, 'is not in the word.')
                        
                        print(hangman_name + ": OHH NOO!!!")# Erick vera - Nombre del hangman
                        
                        if help > 0:
                            print(colored("Input # to get a letter", "cyan"))


                elif user_letter in used_letter:
                     print(colored('You have already used that character. Please try again.', 'yellow'))
                
                if user_letter == "#":
                    if help > 0:
                        help -= 1
                        print(colored("Try with", "blue"), colored(random.choice(word), "blue"))
                    else:
                        print(colored("You don't have any help :(", "cyan"))
                    
            # Aqui se muestra si ganaste o perdiste - Jose Pablo Gonzalez Barba
            if lives == 0:
                ##Sarahi Bañuelos - monito
                print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|`   
                    |           ' '
                    |
                    """)
                print(colored('Te la pelliscaste!, Nimodo. La palabra era: ', 'red'), word)
                print(hangman_name + ": I'll be back")# Erick vera - Nombre del hangman
                engine.say("ya te moriste") # texto a voz si pierde
                engine.runAndWait()
                writeLosses()

            else:
                print(colored('AHUEVO! Eres digno de poder ser amigo de ChemssDoggie!!', 'green'))
                engine.say("felicidades") #voz si gana
                engine.runAndWait()
                writeWins()

            # MAX ALVAREZ --Pregunta si quiere volver a jugar o no y modifica el valor de start
            if input('Wanna play again? (Yes or No): ').upper().startswith('Y'): # Si lo que ingresa empieza con Y entonces es un Yes
                if input('Wanna clear history? (Yes or No): ').upper().startswith('Y'):#Susana Robles
                    clearHistory()
                start = True
            else:
                start = False # Se modifica start, lo que afecta el while de start y finaliza el juego
            # MAX ALVAREZ

                # Mejora 2: Mensaje de despedida/fin del juego (Sáenz)
                print('*' * 29)
                print('* Good luck next time, bye! *')
                print('* Made by group 372 *') # Mejora 3: Mensaje de creditos del juego (Sáenz)
                print('*' * 29)
            
            # Si hay una interrupcion del teclado, se muestra este mensaje y termina el programa.
        except KeyboardInterrupt:
            print("\n\nGracias por interrumpirme cabezon, bye.")
                
    return word_letters  # MAX ALVAREZ-- Movi este return una tabulacion atras para sacarlo del while de start y que pudiese funcionar dicho while


# Williams --Realizamos el menu de inicio para empezar el juego
def show_menu():
    while True:
        print(f"                ********************** \n\
                ********************** \n\
                Human what do you want, wanna play with the life of others?\n\
                   _____           O   \n\
              * * /_____\ * *     `|`\n\
              | | |_____| | |     ' '\n\
                                 \n\
                press m to start the game.\n\
                Press x to exit.")
        opcion = input()
        if opcion == 'm':
            print(hangman())
        elif opcion == 'x':
            break
        input()
        os.system("cls")
nombre()
show_menu()