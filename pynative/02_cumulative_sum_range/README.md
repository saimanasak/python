### Exercise 02: Cumulative Sum of a Range

#### Problem Statement

Write a Python program that iterates through the first 10 numbers (0–9).

For each iteration:

- Print the **current number**.
- Print the **previous number**.
- Calculate and print the **sum of the current and previous numbers**.

For the first iteration, assume the previous number is `0`.

#### Objective

Practice Python `for` loops, the `range()` function, arithmetic operations, and state tracking.

Understand how to remember a value from a previous iteration and use it in the current iteration.

#### Input

A range of 10 integers:

```python
numbers = range(10)
```

The range generates integers from `0` to `9`.

#### Expected Output

Print the current number, previous number, and their sum for each iteration.

##### Example 1

**Input:**

```python
numbers = range(10)
```

**Output:**

```text
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number 0 Sum: 0
Current Number 1 Previous Number 0 Sum: 1
Current Number 2 Previous Number 1 Sum: 3
Current Number 3 Previous Number 2 Sum: 5
Current Number 4 Previous Number 3 Sum: 7
Current Number 5 Previous Number 4 Sum: 9
Current Number 6 Previous Number 5 Sum: 11
Current Number 7 Previous Number 6 Sum: 13
Current Number 8 Previous Number 7 Sum: 15
Current Number 9 Previous Number 8 Sum: 17
```

**Explanation:**

- **Iteration 1:** Current = 0, Previous = 0 → Sum = 0
- **Iteration 2:** Current = 1, Previous = 0 → Sum = 1
- **Iteration 3:** Current = 2, Previous = 1 → Sum = 3
- **Iteration 4:** Current = 3, Previous = 2 → Sum = 5
- The process continues until the current number reaches `9`.

#### Source

[PYnative – Python Basic Exercises for Beginners](https://pynative.com/python-basic-exercise-for-beginners/)