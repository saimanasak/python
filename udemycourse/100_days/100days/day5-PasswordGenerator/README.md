### Password Generator

Create a Python program that generates a randomized password based on the character counts selected by the user.

#### Problem Statement

Ask the user how many of each character type the password should contain:

1. Letters (uppercase or lowercase).
2. Symbols.
3. Numbers.

Randomly choose the requested number of characters from each group, combine them, shuffle their order, and display the generated password.

#### Example

```text
****** Welcome to PASSWORD generator ******

Number of letters you would like to have?
8
Number of symbols you would like to have?
2
Number of numbers you would like to have?
2

Your password is: a3Z!mP7@qLsK
```

The generated password will be different each time the program runs.

Run the program with:

```bash
python day5_password_generator.py
```
