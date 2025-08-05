# Day 10: Functions with Outputs and the Calculator Project

On Day 10, we completed our understanding of Python functions by learning how to make them produce outputs using the `return` keyword. This allows functions to not only perform actions but also to pass back data for use elsewhere in our program. We applied this, along with other advanced concepts, to build a fully functional command-line calculator.

---

## 1. Functions with Outputs

So far, our functions have executed a block of code. Now, we'll make them return a value. This is the final and most powerful form of a function.

### The `return` Keyword
The `return` keyword allows a function to send back a result. When a `return` statement is executed, the function stops running and sends the specified value back to the place where the function was called.

**`print` vs. `return`**
It's crucial to understand the difference:
-   **`print()`**: Displays a value to the console. It's for human eyes only; the program can't use this displayed value.
-   **`return`**: Provides a value as an output from the function. This output can be stored in a variable, passed to another function, or used in any way you would use a piece of data.

**Example: Formatting a Name**
We practiced this by creating a function to format a first and last name into title case.

```python
def format_name(f_name, l_name):
  """Takes a first and last name and formats it to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs." # An early, conditional return
  
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  
  # The final output of the function
  return f"{formatted_f_name} {formatted_l_name}"

# The returned value is stored in a variable
formatted_string = format_name("rICARDO", "cALLES") 
print(formatted_string) # Output: Ricardo Calles
```

---

## 2. Multiple `return` Statements

A function immediately exits once it hits a `return` statement. We can use this to our advantage by having multiple return points within a function, often combined with conditional logic (`if`/`else`).

This is useful for handling different cases or for "short-circuiting" a function if an input is invalid. An "empty" `return` can be used to exit the function without sending back any value.

**Example: Input Validation**
```python
def can_buy_alcohol(age):
  # If the input is invalid, exit the function immediately.
  if type(age) != int:
    return "Invalid input."

  # Otherwise, check the condition and return the appropriate boolean.
  if age >= 18:
    return True
  else:
    return False
```

---

## 3. Docstrings

A **docstring** is a string literal that occurs as the first statement in a module, function, class, or method definition. It's enclosed in triple quotes (`"""Docstring goes here"""`) and serves as built-in documentation for your code. It explains what the function does, what inputs it expects, and what it returns. This is a crucial practice for writing clean, maintainable code.

The `format_name` function in the first example includes a docstring.

---

## 4. Project: Calculator

The main project for Day 10 was to build a command-line calculator that can perform basic arithmetic and chain calculations together.

### Demo
[Try the live demo here.](https://appbrewery.github.io/python-day10-demo/)

### Core Concepts and Functionality

1.  **Defining Operation Functions**: First, we created separate functions for each mathematical operation (`add`, `subtract`, `multiply`, `divide`). Each function takes two numbers as input and returns the result.

2.  **Storing Functions in a Dictionary**: This was a key learning point. We created a dictionary where the keys were the mathematical symbols (`"+"`, `"-"`, `"*"`, `"/"`) and the **values were the actual functions themselves**.

    ```python
    def add(n1, n2):
      return n1 + n2

    operations = {
      "+": add,
      # ... other operations
    }
    ```

3.  **Calling Functions from the Dictionary**: This structure allowed us to dynamically call the correct function based on the user's input. If the user chose `*`, we could retrieve the `multiply` function from the dictionary and immediately call it with the user's numbers.

    ```python
    # Example of how to use the dictionary
    calculation_function = operations["+"]
    answer = calculation_function(2, 3) # answer is 5
    ```

4.  **Chaining Calculations**: The program was designed to be continuous. After the first calculation, the result was stored. The user was then asked if they wanted to continue calculating with that result or start a new calculation. This was achieved using a `while` loop or recursion, where the previous answer becomes the first number in the next operation.

5.  **User Experience**: Finally, a logo was imported from an `art.py` file to give the calculator a polished look, reinforcing the concept of using modules to organize code.
