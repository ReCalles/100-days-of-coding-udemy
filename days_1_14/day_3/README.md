# Day 3: Control Flow and Logical Operators

Day 3 introduces a fundamental concept in programming: control flow. We'll learn how to make decisions in our code using conditional statements (`if`, `else`, `elif`), and how to combine these conditions with logical operators. These skills will be used to build a Pizza Order program and a "Choose Your Own Adventure" game.

---

## 1. Conditional Statements: `if` / `else`

Conditional statements allow a program to execute different blocks of code depending on whether a condition is `True` or `False`.

-   **`if` statement**: Executes a block of code only if its condition is true.
-   **`else` statement**: Provides an alternative block of code to execute if the `if` condition is false.
-   **Indentation**: Python uses indentation (spaces or tabs) to define which lines of code belong to the `if` or `else` block. This is a strict syntax rule.

**Structure:**
```python
if condition:
    # This code runs if the condition is True.
    # Notice the indentation.
else:
    # This code runs if the condition is False.
```

### Comparison Operators
These operators are used to create the conditions for our `if` statements.

-   `>` : Greater than
-   `<` : Less than
-   `>=`: Greater than or equal to
-   `<=`: Less than or equal to
-   `==`: Equal to (Note: a double equals sign is for comparison, a single one is for assignment)
-   `!=`: Not equal to

---

## 2. The Modulo Operator (`%`)

The modulo operator (`%`) performs a division and returns the **remainder**. It's incredibly useful for tasks like checking if a number is odd or even.

-   `6 % 2` results in `0` (6 divides by 2 with no remainder).
-   `7 % 2` results in `1` (7 divides by 2 with a remainder of 1).
-   `10 % 3` results in `1` (10 divides by 3 with a remainder of 1).


---

## 3. Nested `if` and `elif`

We can place conditional statements inside other conditional statements.

-   **Nested `if`**: An `if` statement inside another `if` block. This allows for checking a secondary condition only if the first one is met.
-   **`elif` (else if)**: Used to check multiple, mutually exclusive conditions in sequence. The program will execute the code for the first `True` condition it finds and then skip the rest in the chain.

**Structure Comparison:**

```python
# Nested if
if condition_A:
    # Do something
    if condition_B:
        # Do something else (only if A and B are both true)
```python
# if/elif/else
if condition_A:
    # Do A
elif condition_B:
    # Do B (only if A is false, but B is true)
else:
    # Do C (if both A and B are false)
```

---

## 4. Multiple `if` Statements

Unlike `elif`, multiple independent `if` statements will each be checked and executed separately, regardless of the outcome of the others. This is useful when you want to check for several different conditions that could all be true at the same time.

**Example:** In a pizza order, a customer might want pepperoni **and** extra cheese. Both conditions need to be checked independently.

```python
# Multiple if statements (independent checks)
if condition_A:
    # Do A
if condition_B:
    # Do B (this check happens no matter what)
if condition_C:
    # Do C (this check also happens no matter what)
```

---

## 5. Logical Operators

Logical operators are used to combine multiple conditional statements.

-   `and`: Returns `True` only if **both** conditions are true.
-   `or`: Returns `True` if **at least one** of the conditions is true.
-   `not`: Inverts a boolean value ( `not True` becomes `False`).

### Exercise Example
- **Goal**: Check if a person's age is between 45 and 55 (inclusive).
- **Logic**: The age must be greater than or equal to 45 **AND** less than or equal to 55.

```python
age = int(input("What is your age? "))
if age >= 45 and age <= 55:
    print("You get a free ride!")
```

---

## Projects for Day 3

### Python Pizza Order
-   **Goal**: Build an automatic ordering program that calculates the final bill based on user choices.
-   **Pricing Rules**:
    -   Small Pizza: $15
    -   Medium Pizza: $20
    -   Large Pizza: $25
    -   Pepperoni for Small: +$2
    -   Pepperoni for Medium/Large: +$3
    -   Extra Cheese (any size): +$1
-   This project requires using multiple `if` statements to handle the different pizza sizes and toppings, which can be added independently.

### Treasure Island
-   **Goal**: Create a "Choose Your Own Adventure" text-based game based on a provided flowchart.
-   **Logic**: The game uses nested `if`/`elif`/`else` statements to guide the player through a story. The player's choices (`"left"` or `"right"`, `"swim"` or `"wait"`, etc.) determine the outcome.
-   **Helpful Function**: The `.lower()` string method is useful for converting user input to all lowercase to avoid errors (e.g., accepting "Left", "left", and "LEFT" as the same choice).
