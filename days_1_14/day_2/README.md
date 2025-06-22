# Day 2: Data Types, Number Manipulation & Tip Calculator

Welcome to Day 2! This session focuses on understanding Python's fundamental data types, how to manipulate numbers and strings, and how to perform mathematical calculations. These concepts are then combined to build a practical Tip Calculator project.

---

## 1. Primitive Data Types

Python has several built-in "primitive" data types that are the most basic building blocks for storing information.

-   **String:** A sequence of characters, enclosed in quotes. Used for text.
    -   `"Hello"`, `'Python'`
-   **Integer:** A whole number, without a fractional part.
    -   `123`, `-50`, `999`
-   **Float:** A number with a decimal point.
    -   `3.14159`, `19.99`, `-0.5`
-   **Boolean:** Represents one of two values: `True` or `False`. Used for logical operations.
    -   `True`, `False`

---

## 2. Type Errors, Checking, and Conversion

Understanding and managing data types is crucial to prevent errors in your code.

### TypeError
A `TypeError` occurs when you try to perform an operation on an incorrect data type. For example, the `len()` function expects a string but will raise an error if given an integer.

-   **Incorrect Code:**
    ```python
    # This will cause a TypeError because len() doesn't work on numbers.
    len(12345)
    ```

### Type Checking
You can verify the data type of any value or variable using the built-in `type()` function.

-   **Code Example:**
    ```python
    print(type("Hello"))  # Output: <class 'str'>
    print(type(123))      # Output: <class 'int'>
    print(type(3.14))     # Output: <class 'float'>
    print(type(True))     # Output: <class 'bool'>
    ```

### Type Conversion (Casting)
You can explicitly convert a value from one data type to another using casting functions like `str()`, `int()`, and `float()`.

-   **Code Example:**
    ```python
    # To fix the TypeError from earlier, we convert the integer to a string first.
    num_characters = len(str(12345))
    print(num_characters) # Output: 5

    # Another example: getting input and using it in a string
    name_length = len(input("Enter your name: "))
    # The line below would cause a TypeError because you can't concatenate a string with an integer.
    # print("Your name has " + name_length + " characters.")

    # Corrected using type casting:
    print("Your name has " + str(name_length) + " characters.")
    ```

---

## 3. Mathematical Operations

Python supports a full range of mathematical operators. The order of operations follows the standard **PEMDAS** rule (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).

-   `+` (Addition)
-   `-` (Subtraction)
-   `*` (Multiplication)
-   `/` (Float Division) - Results in a float. e.g., `6 / 3` is `2.0`.
-   `//` (Integer Division) - Results in an integer (floors the result). e.g., `7 // 3` is `2`.
-   `**` (Exponent) - e.g., `2 ** 3` is `8`.

### Exercise Summary
- **Code:** `print(3 * 3 + 3 / 3 - 3)`
  - **Evaluation:** `9 + 1.0 - 3` -> `10.0 - 3` -> `7.0`
- **Challenge:** Change the code to output `3.0`.
  - **Solution:** `print(3 * (3 + 3) / 3 - 3)` -> `3 * 6 / 3 - 3` -> `18 / 3 - 3` -> `6.0 - 3` -> `3.0`
  - **Alternate Solution:** `print(3 / 3 * 3 + 3 - 3)` -> `1.0 * 3 + 3 - 3` -> `3.0`

---

## 4. Number Manipulation & F-Strings

### Rounding and Flooring
-   **`round()`**: Rounds a number to the nearest integer or to a specified number of decimal places.
    ```python
    print(round(8 / 3))       # Output: 3
    print(round(8 / 3, 2))    # Output: 2.67
    ```
-   **Flooring**: To simply chop off the decimal part, use integer division `//` or cast to `int()`.
    ```python
    print(8 // 3)         # Output: 2
    print(int(2.67))      # Output: 2
    ```

### Assignment Operators
These are shortcuts to perform an operation on a variable and assign the new value back to it.
```python
score = 0
score += 1  # score is now 1 (same as score = score + 1)
score *= 5  # score is now 5
```

### F-Strings
F-Strings (Formatted String Literals) are a modern and convenient way to embed expressions and variables inside strings. They are prefixed with an `f` before the opening quote.

- **Code Example:**
  ```python
  score = 10
  height = 1.8
  isWinning = True

  # This will print a string combining different data types without needing to cast.
  print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}")
  ```

---

## Project: Tip Calculator

This project applies the concepts from Day 2 to build a practical tip calculator.

### Project Goal
Create a program that:
1.  Asks the user for the total bill amount.
2.  Asks for the desired tip percentage (e.g., 10, 12, or 15).
3.  Asks how many people are splitting the bill.
4.  Calculates and prints the amount each person should pay, formatted to two decimal places.

### Calculation Logic
If the bill was `$150.00`, split between `5` people, with a `12%` tip:
1.  **Add the tip:** `$150.00 * 1.12 = $168.00`
2.  **Split the total:** `$168.00 / 5 = $33.6`
3.  **Format the result:** The final output should be `33.60`.
