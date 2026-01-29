# 🧮 Basic Arithmetic Operations

## 📌 Problem Statement
Write a Python program that accepts **two integers** and performs the following arithmetic operations:

1. Sum  
2. Difference  
3. Product  
4. Quotient  
5. Remainder  

Each result must be printed on a **new line** in the specified order.

---

# Input Format
- The program accepts **two integers** as input:
  - First integer `A`
  - Second integer `B`

Inputs are provided via standard input.

---

# Output Format
Print **five lines**:
1. Sum of `A` and `B` (`A + B`)
2. Difference of `A` and `B` (`A - B`)
3. Product of `A` and `B` (`A * B`)
4. Quotient of `A` divided by `B` (`A / B`)
5. Remainder when `A` is divided by `B` (`A % B`)

---

# Constraints
- `-10⁹ ≤ A, B ≤ 10⁹`
- `B ≠ 0` (Division by zero is not allowed)

---

## Sample Input

- Enter the first number: 10  
- Enter the second number: 3

---

## Sample Output

- Sum:  13
- Difference:  7
- Product:  30
- Quotient:  3
- Remainder:  1

---

# Explanation
For the input values:
- `A = 10`
- `B = 3`

The calculations are:
- Sum → `10 + 3 = 13`
- Difference → `10 - 3 = 7`
- Product → `10 × 3 = 30`
- Quotient → `10 ÷ 3 = 3` (integer division)
- Remainder → `10 % 3 = 1`

---

## 🏷️ Difficulty Level
**Beginner**

---

## 🛠️ Notes
- Ensure the quotient uses **integer division**.
- Output must strictly follow the given order.
- Each result should be printed on a new line.