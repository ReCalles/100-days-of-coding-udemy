# Day 6: Python Functions & While Loops

Day 6 is all about making our code more organized, reusable, and powerful. We'll learn how to define our own functions to package up blocks of code, and we'll explore a new type of loop, the `while` loop, which allows us to repeat actions as long as a certain condition is true. These concepts are practiced extensively through problem-solving challenges on Reeborg's World.

---

## 1. Defining and Calling Functions

A function is a named block of code that performs a specific task. By defining a function, we can run that block of code whenever we need it simply by "calling" its name, which helps avoid repetition and makes our programs easier to read.

### Defining a Function
We use the `def` keyword to create, or "define," a new function. The syntax is as follows:

```python
def my_function():
    # This code is inside the function
    print("Hello")
    print("from a function")
```

### Calling a Function
Defining a function doesn't run the code inside it. To execute the function's code, you must "call" it by writing its name followed by parentheses.

```python
# Defining the function
def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

greet_user() # Calling the function
```

---

## 2. `while` Loops

While a `for` loop is great for iterating over a known number of items, a `while` loop is used to repeat a block of code as long as a specific condition remains `True`. This is perfect for situations where we don't know how many times to loop.

### Syntax
```python
while something_is_true:
    # Do something repeatedly
```

### `for` vs. `while`
-   **`for` loop**: Use when you know exactly how many times you need to iterate.
-   **`while` loop**: Use when you need to loop until a certain condition is met.

**Warning:** Be careful with `while` loops! If the condition never becomes `False`, you will create an **infinite loop**, and your program will get stuck.

---

## 3. Reeborg's World: Hurdle Challenges

The lessons of Day 6 are put into practice through a series of challenges in Reeborg's World, demonstrating the progression from simple loops to more complex, condition-driven logic. The reference images for these exercises can be found inside the `02_reeborgs_world_exercises` folder.

### Exercise 1: Hurdle Race (Fixed)
-   **Goal**: Guide Reeborg through a hurdle race where the number of hurdles is always the same.
-   **Solution**: Since the number of repetitions is known, a `for` loop is a suitable solution. We define a `jump()` function and call it a fixed number of times. (Reference image: `01_jumping_over_fixed_hurdles.png`)

### Exercise 2: Variable Hurdle Race
-   **Goal**: Guide Reeborg through a race where the position and number of hurdles change each time.
-   **Solution**: A `for` loop no longer works because the number of jumps is unknown. This requires a `while` loop that continues as long as Reeborg has not reached the goal. The condition `while not at_goal():` is used to solve this. (Reference image: `02_jumping_over_hurdles_that_vary_each_time.png`)

### Exercise 3: Variable Height Hurdle Race
-   **Goal**: Guide Reeborg through a race where the position, number, AND height of the hurdles change.
-   **Solution**: This builds on the `while` loop by adding conditional logic (`if/elif/else`) inside the loop. The program must check if there is a wall in front of it to decide whether to climb the hurdle or just move forward. (Reference image: `03_jumping_over_hurdles_with_variable_heights.png` shows a similar problem-solving approach).

---

## 4. Reeborg's Project Challenge: Lost in a Maze

This is the final project for Day 6, combining all the concepts into a more complex problem.

-   **Link**: [Reeborg's World Maze Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
-   **Goal**: Reeborg is lost in a dark maze. Write a program using an `if/elif/else` statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, (1) turning right if it can, (2) going straight ahead if it can’t turn right, or (3) turning left as a last resort.

### What you need to know
-   The functions `move()` and `turn_left()`.
-   The tests `front_is_clear()`, `right_is_clear()`, and `at_goal()`.
-   How to use a `while` loop and `if/elif/else` statements.
-   Using negation (`not`) to invert a condition.

### Project Notes
-   In this repository, there is a dedicated folder for this project. The initial coding attempt resulted in an infinite loop under certain maze conditions. After debugging, a more robust solution was developed.
-   The project folder also contains a zip file with different maze scenarios. These can be imported into the Reeborg's World application to test the final code and ensure the infinite loop bug does not reoccur.
