# Day 12: Scope & The Number Guessing Game

On Day 12, we delved into a crucial and often tricky concept in programming: **scope**. Understanding scope is essential for writing bug-free code, as it determines where our variables can be accessed. We then applied this knowledge to build a fun and interactive Number Guessing Game.

---

## 1. Namespaces and Scope

A namespace is the system that Python uses to keep track of all the names (variables, functions, etc.) in a program. Scope refers to the region of the code where a particular name is accessible.

### Local Scope
When a variable is created inside a function, it has **local scope**. This means it only exists and can only be accessed from within that specific function. Trying to access it from outside the function will result in a `NameError`.

```python
def my_function():
  potion_strength = 2 # This is a local variable
  print(potion_strength)

my_function() # This works and prints 2
# print(potion_strength) # This would cause a NameError
```

### Global Scope
A variable created in the main body of a Python file (at the top level, with no indentation) has **global scope**. It can be accessed from anywhere in the code, including from inside any function.

```python
player_health = 10 # This is a global variable

def drink_potion():
  # We can read the global variable from inside the function
  print(player_health)

drink_potion() # This works and prints 10
```

---

## 2. Block Scope in Python

One unique aspect of Python is that it **does not have block scope**. In many other languages, a variable created inside a block like an `if` statement, `while` loop, or `for` loop only exists within that block.

In Python, if a variable is created inside one of these blocks, its scope is determined by where the block itself is located. If the block is inside a function, the variable has local scope to that function. If the block is at the top level, the variable has global scope.

```python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0] # This variable is created inside an if block

# Because the 'if' block is at the global level, 'new_enemy' is also a global variable.
print(new_enemy) # This works and prints "Skeleton"
```

---

## 3. Modifying Global Variables

While you can read a global variable from within a function, trying to modify it directly will cause an error or create a new local variable with the same name.

To explicitly modify a global variable from within a local scope (like a function), you must use the `global` keyword.

```python
enemies = 1 # Global variable

def increase_enemies():
  global enemies # Tells Python we want to modify the global variable
  enemies += 1
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
# Both will print 2
```
**Note:** It's generally considered bad practice to modify global variables frequently. A better approach is often to use `return` statements to pass values out of functions.

### Global Constants
For values that are defined globally and are never intended to change, we use **global constants**. By convention, their names are written in `ALL_CAPS_WITH_UNDERSCORES`. This makes it clear to anyone reading the code that this value should not be modified.

```python
PI = 3.14159
URL = "[https://www.google.com](https://www.google.com)"
```

---

## 4. Project: The Number Guessing Game

The project for Day 12 was to build a number guessing game, which put our understanding of scope into practice.

### How It Works
1.  **Welcome and Setup**: The game starts by welcoming the player and randomly choosing a number between 1 and 100.
2.  **Difficulty Selection**: The player is asked to choose a difficulty level, "easy" or "hard". This choice determines the number of guesses they get. These turn counts are stored as global constants.
3.  **The Guessing Loop**: A `while` loop runs as long as the player has guesses remaining.
4.  **Feedback**: Inside the loop, the player makes a guess. The program then tells them if their guess is "Too high," "Too low," or if they've guessed the correct number.
5.  **Tracking Turns**: For each incorrect guess, the number of remaining turns is reduced by one.
6.  **Game Over**: The game ends when the player either guesses the number correctly (they win) or runs out of turns (they lose).

This project was a great exercise in using functions to organize code and understanding how to manage variables (like the number of turns and the secret number) across different parts of the program.
