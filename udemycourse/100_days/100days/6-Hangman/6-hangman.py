# Import random module
import random

# Colors for terminal output
Red = '\033[31m'
End = '\033[m'
Cyan = '\033[36m'
Yellow = '\033[33m'
Green = '\033[32m'
Blue = '\033[34m'
Pink = '\033[95m'

# List of words for the game
words = ["apple", "banana", "orange", "mango", "grape"]

# Pick a random word from the list
secret_word = random.choice(words)

# Create an empty list to display blanks
blank_array = []

# Add one "_" for each letter in the secret word
for i in range(len(secret_word)):
    blank_array.append("_")

# Number of lives
lives = 6

# Display the game title and blanks
print(Yellow + "Welcome to Hangman...!", End)
print(" ".join(blank_array))

# Keep playing while the player has lives
while lives > 0:

    # Ask the player to guess a letter
    guessed_letter = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the secret word
    if guessed_letter in secret_word:
        print(Cyan + "Wow... guessed the correct letter", End)

        # Find all positions of the guessed letter
        for index, letter in enumerate(secret_word):

            # Reveal the letter at the correct position
            if guessed_letter == letter:
                blank_array[index] = guessed_letter

    else:
        # Reduce a life for a wrong guess
        print(Pink + "Oops... Wrong guess :(", End)
        lives = lives - 1
        print(Red + f"Lives left...........{lives}/6", End)

    # Display the updated word
    print(" ".join(blank_array))

    # Check if all letters have been guessed
    if "_" not in blank_array:
        print(Green + "You won!", End)
        print(f"The word was: {secret_word}")
        break

# Player loses when no lives are left
if lives == 0:
    print(Red + "You lost!", End)
    print(f"The word was: {secret_word}")