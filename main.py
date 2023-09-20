# Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
len_of_chosen_word = len(chosen_word)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = ["_"] * len_of_chosen_word

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while "_" in display:
    guess = input("Guess a letter: ").casefold()

    # Check guessed letter
    for position in range(len_of_chosen_word):
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)
else:
    print("You win!")