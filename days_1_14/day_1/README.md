# Day 1: Python Fundamentals & First Project

Welcome to Day 1 of my Python journey! This document summarizes the foundational concepts covered today, from printing your first line of code to building a simple but fun project. Each section breaks down a core concept and the exercises that I worked on associated with it.

---

## 1. The `print()` Function

The first step in any programming language is often learning how to display output. In Python, this is done with the `print()` function.

### Core Concept
- **`print()`**: A built-in Python function that writes specified content to the screen.
- **Syntax**: The text (or "string") you want to print must be enclosed in parentheses `()` and quotation marks `""`.

### Exercise Summary
- **Goal**: Print the classic "Hello world!" message to the console.
- **Code Example**:
  ```python
  print("Hello world!")
  ```

---

## 2. String Manipulation

Strings are sequences of characters. You can manipulate them in various ways, such as joining them together (concatenation) or formatting them to appear on different lines.

### Core Concepts
- **String Concatenation**: Combining or linking strings together. This is typically done using the `+` operator.
- **Newline Character**: The escape sequence `\n` is used within a string to create a line break. When the string is printed, anything after `\n` will appear on a new line.

### Exercise Summary
1.  **Using Newlines**: Print "Hello world!" three times, each on a new line, using a single `print()` statement.
    - **Code Example**:
      ```python
      print("Hello world!\nHello world!\nHello world!")
      ```
2.  **Concatenating with a Space**: Combine two strings, "Hello" and a name (e.g., "Angela"), with a space in between.
    - **Code Example**:
      ```python
      # Notice the space included inside the string
      print("Hello" + " " + "Angela")
      ```

---

## 3. The `input()` Function

Programs are much more interactive when they can receive data from a user. The `input()` function pauses your program and waits for the user to type something and press Enter.

### Core Concept
- **`input()`**: A built-in function that prompts the user for input and reads a line of text.
- **Return Value**: The `input()` function always returns the user's input as a **string**.
- **Syntax**: You can include a string prompt inside the parentheses `()` to guide the user.

### Exercise Summary
- **Goal**: Ask the user for their name and then greet them with an exclamation mark.
- **Code Example**:
  ```python
  # The input() function asks the question, and the result is concatenated into the print() function
  print("Hello " + input("What is your name? ") + "!")
  ```

---

## 4. Variables

Variables are containers for storing data values. Using variables makes your code more readable and allows you to reuse data without having to type it out every time.

### Core Concepts
- **Assignment**: You create a variable by giving it a name and using the equals sign `=` to assign it a value.
- **Reusability**: Once a value is stored in a variable, you can reference it simply by using its name.
- **`len()` Function**: A built-in function that returns the number of items in an object. For a string, it returns the number of characters.

### Exercise Summary
1.  **One-Line Length Check**: Get user input and immediately print the length of that input, all in one line.
    - **Code Example**:
      ```python
      print(len(input("What is your name? ")))
      ```
2.  **Using Variables**: Split the previous exercise into separate, more readable steps using variables.
    - **Code Example**:
      ```python
      username = input("What is your name? ")
      length_of_name = len(username)
      print(length_of_name)
      ```

---

## 5. Variable Naming Conventions

Choosing good variable names is crucial for writing clean, understandable, and maintainable code. Python has several established conventions.

### Rules for Naming Variables
1.  **Be Descriptive**: Names should clearly reflect the data they hold (e.g., `user_name` is better than `un`).
2.  **No Spaces**: Use underscores `_` to separate words (this is called `snake_case`). For example: `favorite_city`.
3.  **Cannot Start with a Number**: A variable name must begin with a letter or an underscore. `1st_place` is invalid; `first_place` is valid.
4.  **Avoid Keywords**: Don't use names of built-in functions or reserved keywords like `print`, `input`, or `str`.
5.  **Keep it Simple**: Choose clear and concise names to reduce the chance of typos.
6.  **Follow Style Guides**: In a professional setting, always adhere to the company's coding style guide.

---

## Project: Band Name Generator

This project combines all the concepts learned today to create a simple, interactive program.

### Project Steps
1.  **Greeting**: Start by printing a welcome message to the user.
2.  **Get City**: Ask the user for the city they grew up in and store the result in a variable.
3.  **Get Pet Name**: Ask the user for their pet's name and store it in another variable.
4.  **Combine and Display**: Concatenate the city and pet name to create a band name and print it for the user.
5.  **Format Input Cursor**: Ensure that when the program asks for input, the user's cursor appears on a new line for better readability. This is achieved by using the `\n` character at the end of your prompt string.

### Example Interaction
```
Welcome to the Band Name Generator!
What's the name of the city you grew up in?
New York
What's your pet's name?
Zoe
Your band name could be New York Zoe
