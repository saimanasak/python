### Rock, Paper, Scissors

Create a command-line version of Rock, Paper, Scissors against a computer opponent.

#### Problem Statement

Ask the player to select a gesture using one of these numbers:

| Number | Gesture |
| --- | --- |
| `0` | Rock |
| `1` | Paper |
| `2` | Scissors |

Randomly select a gesture for the computer, show both selections, then determine the result using the standard rules:

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- Matching gestures result in a tie.

#### Example

```text
Rock - 0, Paper - 1, Scissors - 2

Choose a number: 0

You Chose: Rock
Computer Chose: Scissors
You Won
```

Run the program with:

```bash
python day4_rock_paper_scissors.py
```
