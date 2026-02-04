# 🎯 Number Guessing Game

## 📌 Problem Statement
Create an interactive **number guessing game** in Python where the computer randomly selects a number and the user attempts to guess it within a limited number of attempts.

The game provides feedback after each guess to help the user determine whether they are getting closer to or farther from the correct number.

---

## 🎮 Game Rules
- The program randomly generates an integer between **1 and 100**.
- The user has a maximum of **10 attempts** to guess the correct number.
- Feedback is provided after each guess based on proximity to the target number.

---

## Feedback Logic

### First Guess
- **OUT OF BOUND** → Guess is not in the range `[1, 100]`
- **WARM** → Guess is within ±10 of the target number
- **COLD** → Guess is more than ±10 away from the target number

### Subsequent Guesses
- **WARMER** → Current guess is closer to the target than the previous guess
- **COLDER** → Current guess is farther from the target than the previous guess
- **OUT OF BOUND** → Guess is outside the valid range

---

## Input Format
- Repeated integer inputs entered by the user (one per guess).

---

## Output Format
- Hint messages after each guess (`WARM`, `COLD`, `WARMER`, `COLDER`, `OUT OF BOUND`)
- Success message if the correct number is guessed within the allowed attempts
- Game over message if all attempts are exhausted
- Total number of guesses made
- List of all guessed numbers

---

## Constraints
- Guess range: `1 ≤ guess ≤ 100`
- Maximum attempts: `10`

---

## Sample Run
```
Guess a number: 45
COLD! guess again...

Guess a number: 65
WARMER! guess again...

Guess a number: 78
WARMER! guess again...

Game Over! You've used all your guesses.
The correct number was: 79
```

---

## Learning Objectives
This mini game reinforces:
- Random number generation
- Loop control with termination conditions
- Conditional logic
- List usage for state tracking
- User interaction and feedback
- Basic game design principles

---

## Difficulty Level
**Beginner (Applied Logic)**

---

## Notes
- ANSI escape codes are used to display colored output in the terminal.
- The game ends immediately when the correct number is guessed or when the attempt limit is reached.
- This implementation focuses on clarity and learning rather than optimization.