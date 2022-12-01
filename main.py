from words import words,example
import random
import string
import os

# PATRICK OWNER OF BASE HANGMAN REPOSITORY

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def writeWins():
    file = open("match_history.txt", "a")
    file.write("You win!\n")
    file.close()
    file = open("match_history.txt", "r")
    history = file.read()
    wins = history.count("You win!")
    losses = history.count("You lose!")
    print(f"Veces que te la has pellizcado: {losses}\n Veces que has sido digno: {wins}")
    file.close()


def writeLosses():
    file = open("match_history.txt", "a")
    file.write("You lose!\n")
    file.close()
    file = open("match_history.txt", "r")
    history = file.read()
    wins = history.count("You win!")
    losses = history.count("You lose!")
    print(f"Veces que te la has pellizcado: {losses}\n Veces que has sido digno: {wins}")
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
            lives = 6
            word = get_valid_word(example)

            word_letters = set(word)

            alphabet = set(string.ascii_uppercase)
            used_letter = set()

            while len(word_letters) > 0 and lives > 0:
                borrarPantalla() #Dulce Badillo
                 # Mejora 1: Mensaje de bienvenida (Sáenz)
                 print('*' * 55)
                print('* Hello welcome! This is the hangman game, good luck! *')
                print('*' * 55)

                if lives == 6:
                    ##Sarahi Bañuelos - Monito
                    print("""
                    -------------
                    | /          |
                    |/
                    |
                    |
                    |
                    """)
                elif lives == 5:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |
                    |
                    |
                    """)
                elif lives == 4:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |            | 
                    |            
                    |
                    """)
                elif lives == 3:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|   
                    |            
                    |
                    """)
                elif lives == 2:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|`   
                    |            
                    |
                    """)
                elif lives == 1:
                    print("""
                    -------------
                    | /          |
                    |/           O   
                    |           `|`  
                    |           ' 
                    |
                    """)

                print('you have used these letters: ', ' '.join(used_letter))
                user_letter = input("Guess a letter: ").upper()
                if len(user_letter) !=1 :
                    print("usa solo una letra")
                elif user_letter in alphabet - used_letter:
                    used_letter.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                    else:
                        lives = lives - 1

                elif user_letter in used_letter:
                    print("You have already used that character. Please try agein.")
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
                print('Te la pelliscaste!, Nimodo. La palabra era: ', word)
                writeLosses()

            else:
                print('AHUEVO! Eres digno de poder ser amigo de ChemssDoggie!!')
                writeWins()

            # MAX ALVAREZ --Pregunta si quiere volver a jugar o no y modifica el valor de start
            if input('Wanna play again? (Yes or No): ').upper().startswith('Y'): # Si lo que ingresa empieza con Y entonces es un Yes
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

print(hangman())