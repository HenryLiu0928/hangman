import random
import string

from Words import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice((words))

    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives, "lives left. You have used these letters: ", " ".join(used_letters))

        word_list = []

        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove((user_letter))
            else:
                lives -= 1
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("you have already guessed it.")
        else:
            print("Invalid character.")
    if lives == 0:
        print(f"You lost. The word is {word}")
    else:
        print(f"you won! It is {word}")

hangman()