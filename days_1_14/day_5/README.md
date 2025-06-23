# Day 5: Python Loops

Day 5 introduces one of the most powerful concepts in programming: loops. We'll learn how to use `for` loops to repeat actions, iterate over data structures like lists, and perform calculations. The day culminates in building a functional Password Generator.

---

## 1. `for` Loops

Loops allow us to execute a block of code multiple times without having to write it repeatedly. A `for` loop is typically used to iterate over a sequence (like a list).

### Syntax
The basic structure of a `for` loop that iterates through a list is:

```python
for item in list_of_items:
    # Do something with each 'item'
```
-   `list_of_items`: The sequence you want to loop through.
-   `item`: A temporary variable that holds the value of the current element in the list for each iteration.

### Indentation
Indentation is critical in Python. Any code that is indented under the `for` loop line will be executed on every iteration. Code that is not indented will run only after the loop has finished.

**Example 1: Indented Code (runs 3 times)**
```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
# Output:
# Apple
# Apple Pie
# Peach
# Peach Pie
# Pear
# Pear Pie
```

**Example 2: Unindented Code (runs once)**
```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello") # This line is outside the loop
# Output:
# Apple
# Peach
# Pear
# Hello
```

---

## 2. Exercise: Highest Score

This challenge requires you to find the highest score in a list of numbers *without* using the built-in `max()` function. This is a classic exercise to practice loop and conditional logic.

### Background on Built-in Functions
Python provides convenient functions like `sum()` and `max()` to perform common operations on lists.
-   `sum(list)`: Adds up all the numbers in the list.
-   `max(list)`: Finds the highest number in the list.

### The Challenge
**Goal:** Replicate the functionality of `max()` using a `for` loop.

**Logic:**
1.  Initialize a variable, let's call it `highest_score`, to `0`.
2.  Loop through each `score` in the list of `student_scores`.
3.  Inside the loop, compare the current `score` with `highest_score`.
4.  If the current `score` is greater than `highest_score`, update `highest_score` to be the current `score`.
5.  After the loop finishes, `highest_score` will hold the maximum value from the list.

```python
# Example list of scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}") # Output: 91
```

---

## 3. `for` Loops with the `range()` Function

The `range()` function generates a sequence of numbers, which is often used with a `for` loop to repeat an action a specific number of times.

-   **`range(start, stop)`**: Generates numbers starting from `start` up to, but **not including**, `stop`.
-   **`range(start, stop, step)`**: Generates numbers from `start` to `stop`, incrementing by `step`.

**Example:**
```python
# This will print numbers from 1 to 9
for number in range(1, 10):
    print(number)
```

---

## 4. Project: Password Generator

This project combines loops, lists, and the `random` module to generate a random password based on user specifications.

-   **Goal**: Ask the user how many letters, symbols, and numbers they want in their password, and then generate a password that meets those criteria.

### Easy Version
In the easy version, the characters are generated in sequence (all letters, then all symbols, then all numbers).

-   **Logic**:
    1.  Create lists for letters, numbers, and symbols.
    2.  Use a `for` loop with `range()` for the number of letters requested. In each iteration, randomly choose a letter and add it to a password list.
    3.  Repeat this process for symbols and numbers.
    4.  Finally, join the items in the password list to form the final password string.

### Hard Version
The hard version generates a much more secure password by shuffling the order of the characters.

-   **Logic**:
    1.  Follow the same steps as the easy version to create a list of password characters (e.g., `['a', 'g', 't', '%', '!', '5', '8']`).
    2.  Instead of joining them directly, use the `random.shuffle()` function to randomize the order of the items within the list.
    3.  After shuffling, join the items in the list to form the final, randomized password string.

**Hint for the Hard Version:** The key is the `random.shuffle()` method, which shuffles a list in place.
