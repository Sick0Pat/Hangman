from words import words,example
import random
import string

# PATRICK OWNER OF BASE HANGMAN REPOSITORY

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():

    # Todo el codigo de abajo se ejecutara siempre y cuando no haya una interrupcion del teclado.
    try:
        lives = 6;

    lives = 6;
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

        
        word = get_valid_word(example)
        
        word_letters = set(word)
        
        alphabet = set(string.ascii_uppercase)
        used_letter = set()

        while len(word_letters) > 0 and lives > 0:

            user_letter = input("Guess a letter: ").upper()
            if user_letter in alphabet - used_letter:
                used_letter.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives - 1

            elif user_letter in used_letter:
                print("You have already used that character. Please try agein.")
            



        return word_letters
    # Si hay una interrupcion del teclado, se muestra este mensaje y termina el programa.
    except KeyboardInterrupt:
        print("\n\nGracias por interrumpirme cabezon, bye.")
        
print(hangman())