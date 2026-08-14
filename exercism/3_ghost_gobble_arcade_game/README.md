# Ghost Gobble Arcade Game

### Overview

In this exercise, you will build a simplified **Pac-Man Game Decision Engine** using Python.

Pac-Man moves through a maze collecting dots and power pellets while avoiding ghosts. Depending on the current game state, your program should determine whether Pac-Man can eat a ghost, score points, lose the game, or win the game.

This exercise focuses on using **Boolean values** and **logical operators** (`and`, `or`, and `not`) to make decisions based on different game scenarios.

---

### Problem Statement

Write a Python program that implements the game rules for a simplified version of Pac-Man.

Your program should determine the outcome of different game situations based on Boolean inputs provided by the user.

Implement the following four rules:

1. Determine whether Pac-Man can eat a ghost.
2. Determine whether Pac-Man scores points.
3. Determine whether Pac-Man loses the game.
4. Determine whether Pac-Man wins the game.

Each rule should return either **True** or **False**.

---

## Game Rules

### Rule 1: Can Pac-Man Eat a Ghost?

Pac-Man can eat a ghost **only if**:

* A power pellet is active.
* Pac-Man is touching a ghost.

#### Inputs

* Power Pellet Active (`True` / `False`)
* Touching Ghost (`True` / `False`)

#### Output

* `True` if Pac-Man can eat the ghost.
* `False` otherwise.

---

### Rule 2: Did Pac-Man Score?

Pac-Man scores whenever he touches:

* A power pellet **or**
* A dot.

#### Inputs

* Touching Power Pellet (`True` / `False`)
* Touching Dot (`True` / `False`)

#### Output

* `True` if Pac-Man scores.
* `False` otherwise.

---

### Rule 3: Did Pac-Man Lose?

Pac-Man loses the game if:

* He is touching a ghost.
* No power pellet is active.

#### Inputs

* Power Pellet Active (`True` / `False`)
* Touching Ghost (`True` / `False`)

#### Output

* `True` if Pac-Man loses.
* `False` otherwise.

---

### Rule 4: Did Pac-Man Win?

Pac-Man wins the game if:

* All dots have been collected.
* Pac-Man has **not** lost the game.

The losing condition follows the rules defined in **Rule 3**.

#### Inputs

* All Dots Eaten (`True` / `False`)
* Power Pellet Active (`True` / `False`)
* Touching Ghost (`True` / `False`)

#### Output

* `True` if Pac-Man wins.
* `False` otherwise.

---

## Sample Input & Output

### Rule 1 – Eat Ghost

#### Sample Input

```text
Power Pellet Active: True
Touching Ghost: True
```

#### Sample Output

```text
Can Eat Ghost: True
```

---

### Rule 2 – Score

#### Sample Input

```text
Touching Power Pellet: False
Touching Dot: True
```

#### Sample Output

```text
Scored: True
```

---

### Rule 3 – Lose

#### Sample Input

```text
Power Pellet Active: False
Touching Ghost: True
```

#### Sample Output

```text
Lost: True
```

---

### Rule 4 – Win

#### Sample Input

```text
All Dots Eaten: True
Power Pellet Active: False
Touching Ghost: False
```

#### Sample Output

```text
Won: True
```

---

## Function Requirements

Implement the following functions:

| Function                                                       | Description                                |
| -------------------------------------------------------------- | ------------------------------------------ |
| `eat_ghost(power_pellet_active, touching_ghost)`               | Returns whether Pac-Man can eat the ghost. |
| `score(touching_power_pellet, touching_dot)`                   | Returns whether Pac-Man scores points.     |
| `lose(power_pellet_active, touching_ghost)`                    | Returns whether Pac-Man loses the game.    |
| `win(has_eaten_all_dots, power_pellet_active, touching_ghost)` | Returns whether Pac-Man wins the game.     |

---

## Constraints

* All function parameters are Boolean values (`True` or `False`).
* Every function must return a Boolean value.
* Use logical operators (`and`, `or`, `not`) to implement the game rules.

---

## Expected Folder Structure

```text
3_pacman_game_decision_engine/
│
├── README.md
├── exercism_style_solution.py
└── ghostGobbleArcadeGame.py
```

---

Happy Coding! 👾🎮