# 🔢 Number Type Conversions

## 📌 Problem Statement
Write a Python program to perform the following number type conversions:

1. Convert a **floating-point number to an integer without losing precision**
2. Convert an **integer to a float**
3. Convert an **integer to a complex number**

The program should display the converted values in the specified order.

---

## Input Format
- Line 1: A floating-point number `F`
- Line 2: An integer `N`

---

## Output Format
Print **three lines**:
1. Integer representation of the float without losing precision
2. Float representation of the integer
3. Complex representation of the integer

---

## Constraints
- `-10⁶ ≤ F ≤ 10⁶`
- `-10⁶ ≤ N ≤ 10⁶`

---

### Sample Input
```
12.50
7
```

---

### Sample Output
```
1250
7.0
(7+0j)
```

---

## 🧠 Explanation
- Converting a float to an integer **without losing precision** means preserving all decimal digits by scaling the number appropriately.
- Converting an integer to a float adds a decimal point.
- Converting an integer to a complex number results in a complex value with zero imaginary part.

---

## 🏷️ Difficulty Level
**Easy**