# Lasagna Cooking Assistant

## Problem Statement

Write a **menu-driven Python program** called **Lasagna Cooking Assistant** to help a cook manage the preparation and baking times for making a lasagna.

The program should repeatedly display a menu with different options that allow the user to perform various time-related calculations involved in preparing a lasagna recipe.

Assume the following:

* The lasagna requires **40 minutes** of baking time in the oven.
* Each layer of the lasagna takes **2 minutes** to prepare.

The program should continue to display the menu until the user chooses to exit.

---

## Menu Options

```text
Lasagna Cooking Assistant

1. Calculate Remaining Bake Time
2. Calculate Preparation Time
3. Calculate Total Elapsed Cooking Time
4. Exit
```

---

## Option 1: Calculate Remaining Bake Time

### Description

This option calculates how many minutes of baking time are still required for the lasagna to be fully cooked.

The program should ask the user to enter the number of minutes the lasagna has already been baking in the oven.

Using the expected bake time of **40 minutes**, determine and display the remaining bake time.

### Input

* Elapsed bake time (in minutes)

### Output

* Remaining bake time (in minutes)

### Sample Input

```text
Enter your choice: 1
Enter elapsed bake time: 30
```

### Sample Output

```text
Remaining bake time: 10 minutes
```

### Explanation

The lasagna should bake for a total of 40 minutes.

If it has already baked for 30 minutes:

```text
40 − 30 = 10 minutes remaining
```

---

## Option 2: Calculate Preparation Time

### Description

This option calculates the total preparation time required to assemble the lasagna.

The program should ask the user to enter the number of layers in the lasagna.

Assume that each layer requires **2 minutes** to prepare.

### Input

* Number of lasagna layers

### Output

* Total preparation time (in minutes)

### Sample Input

```text
Enter your choice: 2
Enter number of layers: 4
```

### Sample Output

```text
Preparation time: 8 minutes
```

### Explanation

Each layer takes 2 minutes to prepare.

If the lasagna has 4 layers:

```text
4 × 2 = 8 minutes
```

---

## Option 3: Calculate Total Elapsed Cooking Time

### Description

This option calculates the total amount of time spent cooking the lasagna so far.

The total elapsed cooking time includes:

1. The time spent preparing the lasagna layers.
2. The time the lasagna has already been baking in the oven.

The program should ask the user for both the number of layers and the elapsed bake time.

### Input

* Number of lasagna layers
* Elapsed bake time (in minutes)

### Output

* Total elapsed cooking time (in minutes)

### Sample Input

```text
Enter your choice: 3
Enter number of layers: 3
Enter elapsed bake time: 20
```

### Sample Output

```text
Total elapsed cooking time: 26 minutes
```

### Explanation

Preparation time:

```text
3 × 2 = 6 minutes
```

Elapsed bake time:

```text
20 minutes
```

Total elapsed cooking time:

```text
6 + 20 = 26 minutes
```

---

## Option 4: Exit

### Description

This option allows the user to terminate the program.

When selected, the program should display a farewell message and stop execution.

### Input

```text
Enter your choice: 4
```

### Output

```text
Thank you for using Lasagna Cooking Assistant!
```

---

## Program Requirements

1. Display the menu options to the user.
2. Allow the user to choose an option from the menu.
3. Perform the corresponding calculation based on the selected option.
4. Display the result in a clear and user-friendly format.
5. Continue showing the menu after completing an operation.
6. Exit the program only when the user selects the **Exit** option.

---

## Constraints

* Number of layers must be greater than or equal to **0**.
* Elapsed bake time must be greater than or equal to **0**.
* The user's menu choice must be a valid integer between **1 and 4**.

---

## Example Program Execution

```text
Lasagna Cooking Assistant

1. Calculate Remaining Bake Time
2. Calculate Preparation Time
3. Calculate Total Elapsed Cooking Time
4. Exit

Enter your choice: 1
Enter elapsed bake time: 25

Remaining bake time: 15 minutes


Lasagna Cooking Assistant

1. Calculate Remaining Bake Time
2. Calculate Preparation Time
3. Calculate Total Elapsed Cooking Time
4. Exit

Enter your choice: 2
Enter number of layers: 5

Preparation time: 10 minutes


Lasagna Cooking Assistant

1. Calculate Remaining Bake Time
2. Calculate Preparation Time
3. Calculate Total Elapsed Cooking Time
4. Exit

Enter your choice: 3
Enter number of layers: 4
Enter elapsed bake time: 18

Total elapsed cooking time: 26 minutes


Lasagna Cooking Assistant

1. Calculate Remaining Bake Time
2. Calculate Preparation Time
3. Calculate Total Elapsed Cooking Time
4. Exit

Enter your choice: 4

Thank you for using Lasagna Cooking Assistant!
```

---

## Objective

The objective of this problem is to build a menu-driven application that helps users manage the cooking process of a lasagna recipe by performing various time-related calculations based on user input.