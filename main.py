from words import words
import random


def get_valid_word(words):  # Funcion para escoger una palabra
    word = random.choice(words)
    while '-' in word or ' ' in word:  # valida que la palabra no tenga
        word = random.choice(words)   # guiones o espacios
    return word.upper()


print(get_valid_word(words))


def hangman():  # Funcion principal
    lives = 6  # variable para almacenar las "vidas" del jugador
    word = get_valid_word(words)
    letter_word = set(word)
    print("_ " * len(list(word)))
    print(f"you have {lives} lives")
    letter = input("choose a letter: ")
    return letter_word


print(hangman())
