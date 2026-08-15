### Hangman

Create a command-line Hangman game where the player reveals a randomly selected word by guessing one letter at a time.

#### Problem Statement

The program selects a secret word from a list of fruit names and displays one underscore for each letter. The player repeatedly enters a letter to guess.

- A correct guess reveals every matching letter in the word.
- An incorrect guess costs one life.
- The player starts with 6 lives.
- The player wins by revealing every letter before running out of lives.
- The player loses when all 6 lives are used; the program then displays the secret word.

#### Example

```text
Welcome to Hangman...!
_ _ _ _ _
Guess a letter: a
Wow... guessed the correct letter
a _ _ _ _
Guess a letter: p
Wow... guessed the correct letter
a p p _ _
```

Run the program with:

```bash
python 6-hangman.py
```