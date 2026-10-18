### Exercise 03: Print Characters at Even Index Positions

#### Problem Statement

Write a Python program that accepts a string and displays only the characters present at **even index positions**.

- Use zero-based indexing, where the first character starts at index `0`.
- Print characters at indices `0, 2, 4, 6, ...`.
- Skip characters at odd index positions.
- Display each selected character on a separate line.

#### Objective

Practice Python strings, zero-based indexing, loops, and accessing individual characters.

Understand how to identify and retrieve characters from specific positions within a string.

#### Input

A string value:

```python
string = "pynative"
```

#### Expected Output

Print the original string followed by the characters located at even index positions.

##### Example 1

**Input:**

```python
string = "pynative"
```

**Output:**

```text
Original String is  pynative
Printing only even index chars
p
n
t
v
```

**Explanation:**

The string `"pynative"` contains the following characters and index positions:

| Index | Character | Position |
|---|---|---|
| 0 | p | Even |
| 1 | y | Odd |
| 2 | n | Even |
| 3 | a | Odd |
| 4 | t | Even |
| 5 | i | Odd |
| 6 | v | Even |
| 7 | e | Odd |

The characters at even indices are `p`, `n`, `t`, and `v`.

**Note:** Even index positions refer to indices divisible by `2`, including `0`, not characters that appear in the 2nd, 4th, or 6th positions when counting from 1.

#### Source

[PYnative – Python Basic Exercises for Beginners](https://pynative.com/python-basic-exercise-for-beginners/)