### Exercise 01: Product or Sum of Two Numbers

#### Problem Statement

Write a Python function that accepts two integers and performs an operation based on their product.

- If the product of the two numbers is **less than or equal to 1000**, return their product.
- If the product is **greater than 1000**, return their sum.

#### Objective

Practice Python conditional statements (`if-else`), arithmetic operations, and functions.

#### Input

Two integer values:
- `number1`: First integer
- `number2`: Second integer

#### Expected Output

Return a single integer representing either the product or the sum of the two input numbers.

##### Example 1

**Input:**
```python
number1 = 20
number2 = 30
```

**Output:**
```text
600
```

**Explanation:**

20 × 30 = 600

Since 600 ≤ 1000, return the product.

##### Example 2

**Input:**
```python
number1 = 40
number2 = 30
```

**Output:**
```text
70
```

**Explanation:**

40 × 30 = 1200

Since 1200 > 1000, return the sum (40 + 30 = 70)

#### Source

[PYnative – Python Basic Exercises for Beginners](https://pynative.com/python-basic-exercise-for-beginners/)