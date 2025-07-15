```
# Day 8: Functions with Parameters & Caesar Cipher Project

# Day 8: Function Parameters & The Caesar Cipher

### Functions with Inputs
Day 8 expands on our knowledge of functions by introducing parameters, which allow us to pass data into our functions and make them much more flexible and powerful. We'll explore the difference between positional and keyword arguments and apply these concepts to build a classic cryptography program: the Caesar Cipher.

Previously, we've seen that functions allow us to package code into a named block which can be used repeatedly at a later point.
---

#### PAUSE 1 - Review
- Create a function called `greet()`.
- Write 3 `print` statements inside the function.
- Call the `greet()` function and run your code.
## 1. Functions with Inputs (Parameters)

#### Inputs
By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called. That means we can modify how the function behaves each time by passing in different inputs.
On this day, we learned how to make our functions more dynamic by giving them inputs. By adding a variable name, called a **parameter**, inside the function's parentheses, we can pass in data when we call the function. This data, called an **argument**, allows the function to produce different results each time it's run.

**Example:**
# Creating the function
def myFunction(input):
    print(f"Hey! {input}")

# Using the function
myFunction("Tommy")
# Will output "Hey! Tommy"

#### Inputs are Variables
When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.
# 'name' is the parameter
def greet(name):
    print(f"Hello, {name}")

The name of the input variable, e.g. `name` in this code here: `def greet(name):` is called the **parameter**.

The value of the input variable, e.g. `Angela` when you call the previous `greet` function: `greet("Angela")` is called the **argument**.
# "Angela" is the argument passed to the function
greet("Angela")

---

### Functions with Multiple Inputs & Arguments

#### Multiple Inputs
You can have multiple inputs in functions. All you need to do is separate them with a comma `,`.

#### PAUSE 1
Create a function with multiple inputs.
## 2. Functions with Multiple Inputs

> **Hint:**
> def greet(name, greeting):
>     print(f"{greeting} {name}")
>
> greet("Angela", "Yo!")
We also learned that functions are not limited to a single input. By separating variable names with commas in the function definition, we can create functions that accept multiple arguments.

#### PAUSE 2
Modify the function so that it prints the expected values.
**Example:**
def greet_with(name, location):
    # Expected output:
    # Hello name
    # What is it like in location
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

#### Positional Arguments
By default, when you create a function in Python, it will keep the order of arguments in the function definition.
greet_with("Ricardo", "Mexico")

e.g. In the function below, the first argument that goes in will always be printed before the second one. `a = 2, b = 1`
---

def my_function(a, b):
    print(a)
    print(b)

my_function(2, 1)
# It will print:
# 2
# 1
## 3. Positional vs. Keyword Arguments

#### Keyword Arguments
You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.
When using multiple inputs, it's important to understand how Python matches arguments to parameters.

#### PAUSE 3
Call the `greet_with()` function using keyword arguments.
- **Positional Arguments**: This is the default behavior. The arguments are assigned to parameters based on their order. The first argument goes to the first parameter, the second to the second, and so on. The order matters.
- **Keyword Arguments**: To make code clearer and avoid order-related bugs, we can explicitly assign an argument to a parameter by name. With keyword arguments, the order no longer matters.

> **Hint:**
> greet_with(location="London", name="Angela")
**Example:**
# Using keyword arguments makes the code's intent very clear.
greet_with(location="London", name="Angela")

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
```