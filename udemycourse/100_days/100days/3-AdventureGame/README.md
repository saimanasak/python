### Treasure Island Adventure Game

Create a text-based adventure in which the player must make the right choices to find hidden treasure.

#### Problem Statement

Guide the player through a short branching story. At each stage, prompt them to choose one of the available actions:

1. At a crossroad, choose `left` or `right`.
2. After going left, choose to `wait` for a boat or `swim` across a lake.
3. After waiting successfully, choose a `red`, `yellow`, or `blue` door.

The player wins by choosing **left**, then **wait**, then the **yellow** door. All other choices end the game.

#### Winning Path

```text
Where do you want to go? Type 'left' or 'right': left
Type 'wait' to wait for a boat. Type 'swim' to swim across: wait
Which colour do you choose?: yellow

You found the treasure...
You Win!
```

Run the program with:

```bash
python day3_adventure_game.py
```
