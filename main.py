from words import get_valid_word
import string
# PATRICK OWNER OF BASE HANGMAN REPOSITORY


def hangman():
    # Todo el codigo de abajo se ejecutara siempre y cuando no haya una 
    # interrupcion del teclado.
    try:
        lives = 6

        word = get_valid_word()

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
                print("You have already used that character." + 
                "Please try agein.")
        # Aqui se muestra si ganaste o perdiste - Jose Pablo Gonzalez Barba
        if lives == 0:
            print('Te la pelliscaste!, Nimodo. La palabra era: ', word)
        else:
            print('AHUEVO! Eres digno de poder ser amigo de ChemssDoggie!!')

        # Si hay una interrupcion del teclado, se muestra este mensaje 
        # y termina el programa.
    except KeyboardInterrupt:
        print("\n\nGracias por interrumpirme cabezon, bye.")


hangman()