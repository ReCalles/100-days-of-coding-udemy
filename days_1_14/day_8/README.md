# Day 8: Function Parameters & The Caesar Cipher

Day 8 expands on our knowledge of functions by introducing parameters, which allow us to pass data into our functions and make them much more flexible and powerful. We'll explore the difference between positional and keyword arguments and apply these concepts to build a classic cryptography program: the Caesar Cipher.

---

## 1. Functions with Inputs (Parameters)

On this day, we learned how to make our functions more dynamic by giving them inputs. By adding a variable name, called a **parameter**, inside the function's parentheses, we can pass in data when we call the function. This data, called an **argument**, allows the function to produce different results each time it's run.

**Example:**
```python
# 'name' is the parameter
def greet(name):
    print(f"Hello, {name}")

# "Angela" is the argument passed to the function
greet("Angela")
```

---

## 2. Functions with Multiple Inputs

We also learned that functions are not limited to a single input. By separating variable names with commas in the function definition, we can create functions that accept multiple arguments.

**Example:**
```python
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

greet_with("Ricardo", "Mexico")
```

---

## 3. Positional vs. Keyword Arguments

When using multiple inputs, it's important to understand how Python matches arguments to parameters.

-   **Positional Arguments**: This is the default behavior. The arguments are assigned to parameters based on their order. The first argument goes to the first parameter, the second to the second, and so on. The order matters.
-   **Keyword Arguments**: To make code clearer and avoid order-related bugs, we can explicitly assign an argument to a parameter by name. With keyword arguments, the order no longer matters.

**Example:**
```python
# Using keyword arguments makes the code's intent very clear.
greet_with(location="London", name="Angela")
```

---

## 4. Project: Caesar Cipher

The major project for Day 8 was building the Caesar Cipher, an encryption and decryption tool. This project was broken down into several parts to build the final program incrementally.

### Part 1: Encryption
The first step was to create an `encrypt()` function. This function takes a text message and a shift number as inputs. It works by looping through each letter of the message, finding its position (index) in a list of the alphabet, and adding the shift number to find the new letter. A key challenge was handling letters at the end of the alphabet, like 'z'. The solution involved duplicating the alphabet list (`['a', ..., 'z', 'a', ..., 'z']`) to ensure the new index would always be valid.

### Part 2: Decryption
Next, a `decrypt()` function was created. The logic is the reverse of encryption: instead of adding the shift number, it subtracts it from each letter's position to return the original text.

### Part 3: Reorganizing the Code
To make the code more efficient and avoid repetition, the `encrypt()` and `decrypt()` functions were combined into a single `caesar()` function. This new function takes a third input, `direction`, which tells it whether to "encode" or "decode". If the direction is "decode", the function simply reverses the sign of the shift number (e.g., `5` becomes `-5`) and applies the same shifting logic, cleaning up the codebase significantly.

### Part 4: Improving the User Experience
The final step involved polishing the program. This included:
-   Importing a logo from a separate `art.py` file to be displayed at the start.
-   Modifying the code to correctly handle numbers, symbols, and spaces by simply adding them to the output without trying to shift them.
-   Adding a `while` loop to give the user the option to run the program again after it finishes, creating a continuous user experience.
