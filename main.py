# Step 3

import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
len_of_chosen_word = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = ["_"] * len_of_chosen_word

while "_" in display:
    guess = input("Guess a letter: ").casefold()

    # Check guessed letter
    for position in range(len_of_chosen_word):
        if chosen_word[position] == guess:
            display[position] = guess

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print("".join(display))
    print(stages[lives])

    if lives == 0:
        print("You lose.")
        break
else:
    print("You win!")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
