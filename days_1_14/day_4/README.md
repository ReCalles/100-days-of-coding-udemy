# Day 4: Randomisation and Python Lists

On Day 4, we dive into two exciting topics: how to introduce unpredictability into our programs using Python's `random` module, and how to store and manage collections of data using Python Lists. These concepts are essential for creating dynamic games and applications, culminating in a Rock, Paper, Scissors project.

---

## 1. The Random Module

Computers are deterministic by nature, but we can simulate randomness using **pseudorandom number generators**. Python provides a built-in `random` module to handle these tasks.

To use the functions within this module, you must first **import** it at the top of your file:
```python
import random
```

A **module** is simply a Python file (`.py`) containing code that can be imported and used in other files. This helps in organizing and reusing code.

### Generating Random Numbers

-   **Random Integers**: To get a random whole number within an inclusive range, use `random.randint(a, b)`.
    ```python
    # Generates a random integer between 1 and 10 (inclusive)
    random_integer = random.randint(1, 10)
    ```

-   **Random Floats**:
    -   `random.random()`: Generates a random float between 0.0 (inclusive) and 1.0 (exclusive).
        ```python
        # Generates a float like 0.2345...
        random_float = random.random()
        ```
        You can expand this range by multiplying: `random.random() * 5` will produce a float between 0.0 and 4.999...
    -   `random.uniform(a, b)`: Generates a random float within a specific range `[a, b]`.
        ```python
        # Generates a random float between 1.0 and 5.0
        random_float_in_range = random.uniform(1, 5)
        ```
---

## 2. Python Lists

A **list** is a data structure that stores an ordered collection of items. Lists are mutable, meaning you can change their contents.

**Creating a List:**
```python
fruits = ["Apple", "Cherry", "Pear"]
```

### Working with Lists

-   **Accessing Items**: Use the item's index in square brackets `[]`. Remember, Python indexing starts at **0**.
    ```python
    print(fruits[0])  # Output: Apple
    ```
    You can also use **negative indices** to access items from the end of the list. `[-1]` is the last item, `[-2]` is the second to last, and so on.
    ```python
    print(fruits[-1]) # Output: Pear
    ```

-   **Modifying Items**: Target an item by its index and assign a new value.
    ```python
    fruits[0] = "Orange"
    # fruits is now ["Orange", "Cherry", "Pear"]
    ```

-   **Adding Items**:
    -   `.append(item)`: Adds a single item to the **end** of the list.
        ```python
        fruits.append("Banana")
        # fruits is now ["Orange", "Cherry", "Pear", "Banana"]
        ```
    -   For other list methods, refer to the official [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html).

---

## 3. Project: Banker Roulette

This is a small project that applies your knowledge of randomization and lists.

-   **Goal**: Write a program that randomly selects a person from a list of names to pay everyone's bill.
-   **What is being done**: The program takes a string of names, splits them into a Python list, and then uses a random selection method to pick one name from that list to print as the "winner" (or loser, depending on your perspective!).

-   **Approach 1 (Index-based)**:
    1.  Create a list of names.
    2.  Get the total number of items in the list using `len()`.
    3.  Generate a random integer from `0` to `len(list) - 1`.
    4.  Use this random number as an index to select and print the name.

-   **Approach 2 (Function-based)**:
    -   The `random` module has a handy function, `random.choice(list)`, which directly returns a random item from the list, simplifying the process.

---

## 4. IndexErrors and Nested Lists

### IndexError
This error occurs when you try to access an index that is outside the valid range of a list. For a list with 3 items, the valid indices are `0`, `1`, and `2`. Trying to access `list[3]` will cause an `IndexError`.

The `len()` function, which gives you the number of items in a list, is useful for avoiding this error.

### Nested Lists
You can place lists inside other lists to create a "nested list" or a 2D list. This is useful for representing grids, matrices, or grouped data.

```python
fruits = ["Strawberries", "Nectarines", "Apples"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

# A nested list containing two other lists
dirty_dozen = [fruits, vegetables]

# Accessing an item
print(dirty_dozen[1][1]) # Output: Kale
# [1] selects the 'vegetables' list, [1] selects "Kale" from that list.
```

---

## 5. Project: Rock, Paper, Scissors

The final project for Day 4 brings everything together to build a classic Rock, Paper, Scissors game.

-   **Goal**: Create a game where the user can choose Rock, Paper, or Scissors, and the computer makes a random choice to determine the winner.
-   **Core Logic**:
    1.  Get the user's choice.
    2.  Create a list of options: `["Rock", "Paper", "Scissors"]`.
    3.  Have the computer make a random choice from that list.
    4.  Use `if`/`elif`/`else` statements to compare the user's choice and the computer's choice to determine the game's outcome (win, lose, or draw).
