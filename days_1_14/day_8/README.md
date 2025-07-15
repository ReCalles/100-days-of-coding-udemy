# Day 8: Functions with Parameters & Caesar Cipher Project

Day 8 expands on our knowledge of functions by introducing parameters, which allow us to pass data into our functions and make them much more flexible and powerful. We'll explore the difference between positional and keyword arguments and apply these concepts to build a classic cryptography program: the Caesar Cipher.


### Functions with Inputs

Previously, we've seen that functions allow us to package code into a named block which can be used repeatedly at a later point.

#### PAUSE 1 - Review
- Create a function called `greet()`.
- Write 3 `print` statements inside the function.
- Call the `greet()` function and run your code.

#### Inputs
By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called. That means we can modify how the function behaves each time by passing in different inputs.

```python
# Creating the function
def myFunction(input):
    print(f"Hey! {input}")
```python
# Using the function
myFunction("Tommy")
# Will output "Hey! Tommy"
```

#### Inputs are Variables
When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.

The name of the input variable, e.g. `name` in this code here: `def greet(name):` is called the **parameter**.

The value of the input variable, e.g. `Angela` when you call the previous `greet` function: `greet("Angela")` is called the **argument**.

---

### Functions with Multiple Inputs & Arguments

#### Multiple Inputs
You can have multiple inputs in functions. All you need to do is separate them with a comma `,`.

#### PAUSE 1
Create a function with multiple inputs.

> **Hint:**
> ```python
> def greet(name, greeting):
>     print(f"{greeting} {name}")
>
> greet("Angela", "Yo!")
> ```

#### PAUSE 2
Modify the function so that it prints the expected values.
```python
def greet_with(name, location):
    # Expected output:
    # Hello name
    # What is it like in location
```

#### Positional Arguments
By default, when you create a function in Python, it will keep the order of arguments in the function definition.

e.g. In the function below, the first argument that goes in will always be printed before the second one. `a = 2, b = 1`

```python
def my_function(a, b):
    print(a)
    print(b)

my_function(2, 1)
# It will print:
# 2
# 1
```

#### Keyword Arguments
You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.

#### PAUSE 3
Call the `greet_with()` function using keyword arguments.

> **Hint:**
> ```python
> greet_with(location="London", name="Angela")
> ```

---

## Project: Caesar Cipher

This project guides through the development of the Caesar Cipher, a classic substitution cipher. We progressively build the functionality, enhancing it step-by-step from basic operations to a more robust and user-friendly command-line tool.

### Development Stages:

* **Part 1: Basic Encryption & Decryption (`caesar_cipher_1.py`)**
    * This initial stage focused on creating separate `encrypt()` and `decrypt()` functions to handle message encoding and decoding based on a given shift amount.

* **Part 2: Combining Functions into One (`caesar_cipher_2.py`)**
    * Here, we refactored the code to combine both the 'encrypt()' and 'decrypt()' logic into a single, versatile function named `caesar()`. This function now handles both encryption and decryption based on a 'direction' parameter.

* **Part 3: Improving the User Experience (`caesar_cipher_3.py`)**
    * This stage concentrated on enhancing the program's interaction with the user. It involved taking user input for the message, shift amount, and direction (encode/decode), and presenting the results clearly.

* **Final Version: Refinements and Robustness (`caesar_cipher_final.py`)**
    * This is the polished version of the Caesar Cipher program. The code has been cleaned up for better readability and efficiency.
    * **Key improvement:** It now includes enhanced error handling for user input. If the user makes a typo or enters an incorrect command (anything other than 'encode' or 'decode') for the direction, the program will prompt them that the command is incorrect, guiding them to try again.

### Supporting Files:

* `art.py`: This file contains the ASCII art logo that is displayed when the Caesar Cipher program runs, adding a visual element to the user experience.