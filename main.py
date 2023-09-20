# Author: Kavin

from random import choice
from hangman_words import word_list
from hangman_art import *

chosen_word = choice(word_list)
len_of_chosen_word = len(chosen_word)
display = ["_"] * len_of_chosen_word
lives = 6

print(logo)

# Testing code
# print(f"Pssst, the solution is {chosen_word}.")

while "_" in display:
    guess = input("Guess a letter: ").casefold()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(len_of_chosen_word):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print("".join(display))
    print(stages[lives])

    if lives == 0:
        print(f"You lose.\nThe word is {chosen_word}.")
        break
else:
    print(f"You win!\nThe word is {chosen_word}.")
