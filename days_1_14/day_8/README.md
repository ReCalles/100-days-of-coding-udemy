# Day 8: Functions with Parameters & Caesar Cipher Project

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

You are going to build an encryption and decryption program using the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

### Demo
[Try the live demo here.](https://appbrewery.github.io/python-day8-demo/)

### Part 1: Encryption
-   **TODO-1:** Create a function called `encrypt()` that takes `original_text` and `shift_amount` as 2 inputs.
-   **TODO-2:** Inside the 'encrypt' function, shift each letter of the `original_text` forwards in the alphabet by the `shift_amount` and print the encrypted text.
    > **Hint:** You can use the built-in Python `index()` function to find out the position of an item in a list. e.g.
    > ```python
    > fruits = ["Apple", "Pear", "Orange"]
    > fruits.index("Pear") # Returns 1
    > ```
-   **TODO-3:** Call the `encrypt()` function and pass in the user inputs. You should be able to test the code and encrypt a message.
-   **TODO-4:** What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?
    > **Hint:** You can solve this by duplicating the alphabet list, e.g., `['a', 'b', ..., 'z', 'a', 'b', ..., 'z']`.

### Part 2: Decryption
-   **TODO-1:** Create a function called `decrypt()` that takes `original_text` and `shift_amount` as 2 inputs.
-   **TODO-2:** Inside the `decrypt()` function, shift each letter of the `original_text` *backwards* by the `shift_amount` and print the decrypted text.
    > **Hint:** You can multiply any number by -1 to make it a negative number.

### Part 3: Reorganizing the Code
-   **TODO-3:** Combine the `encrypt()` and `decrypt()` functions into a single function called `caesar()`. Use the value of the user-chosen `direction` variable to determine which functionality to use. Call the `caesar()` function instead of `encrypt()`/`decrypt()` and pass in all three variables: `direction`, `text`, and `shift`.
    > **Hint:** Remember that when you multiply a number by -1 it will reverse its sign. e.g. `3 + ( 5 * -1)` is the same as `3 - 5`.

### Part 4: Improving the User Experience
-   **TODO-1:** Import and print the logo from `art.py` when the program starts.
-   **TODO-2:** What happens if the user enters a number/symbol/space that's not in the `alphabet` list? Fix the code to keep the number/symbol/space when the text is encoded/decoded.
    > **Hint:** If a character is not in the `alphabet` list, you can just add it to the final string as an unmodified character.
-   **TODO-3:** Can you figure out a way to restart the cipher program? e.g. `Type 'yes' if you want to go again. Otherwise, type 'no'.`
    > **Hint:** Try creating a `while` loop that continues to execute the program if the user types 'yes'.
