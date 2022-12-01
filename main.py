from words import words,example
import random
import string

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

                print('you have used these letters: ', ' '.join(used_letter))
                user_letter = input("Guess a letter: ").upper()
                if user_letter in alphabet - used_letter:
                    used_letter.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                    else:
                        lives = lives - 1

                elif user_letter in used_letter:
                    print("You have already used that character. Please try agein.")
            # Aqui se muestra si ganaste o perdiste - Jose Pablo Gonzalez Barba
            if lives == 0:
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
            
            # Si hay una interrupcion del teclado, se muestra este mensaje y termina el programa.
        except KeyboardInterrupt:
            print("\n\nGracias por interrumpirme cabezon, bye.")
                
    return word_letters  # MAX ALVAREZ-- Movi este return una tabulacion atras para sacarlo del while de start y que pudiese funcionar dicho while

print(hangman())