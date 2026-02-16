# 🔢 Check Divisibility by 3 and 5

## 📌 Problem Statement
Write a Python program that accepts an integer and determines whether it is divisible by **both 3 and 5**.

The program should print the appropriate result based on the divisibility check.

---

## Input Format
- A single integer `N`.

---

## Output Format
- Print `Divisible by both 3 and 5` if the number is divisible by both.
- Otherwise, print `Not divisible by both 3 and 5`.

---

## Constraints
- `-10⁶ ≤ N ≤ 10⁶`

---

### Sample Input 1
```
15
```

### Sample Output 1
```
Divisible by both 3 and 5.
```

---

### Sample Input 2
```
9
```

### Sample Output 2
```
Not divisible by both 3 and 5.
```

---

## 🧠 Explanation
- A number is divisible by 3 if the remainder when divided by 3 is zero.
- A number is divisible by 5 if the remainder when divided by 5 is zero.
- To satisfy the condition, both divisibility checks must be true.

---

## 🏷️ Difficulty Level
**Beginner**

---

## 🧭 Learning Focus
- Conditional statements
- Logical operators (`and`)
- Modulus operator (`%`)