# A function in its simplest form is just a wrapper name for a block of code. You give it name and then when 
# you call the function by that name, all the code within the function block will be executed. It can help us save 
# time and reduce repeated code.

## Defining a new Function
    # def <function name>():
    #     print("Hello")
    #     # Do something else
    #     # Do something else ...
    
    
## Calling a Function
# Calling a function just means triggering the function. We can call a function at any point in our code in Python.

    # <function name>()
    
# Putting everything together e.g.
#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function

# This code will result in the following sequence of output:
# Hello
# What is your name? #I type Angela
# Hello, Angela



## Indentation
# Indentation is critical in Python. Any code that is indented under the for loop line will be executed on 
# every iteration. Code that is not indented will run only after the loop has finished.

# Example 1: Indented Code (runs 3 times)
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

# Example 2: Unindented Code (runs once)
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello") # This line is outside the loop
# Output:
# Apple
# Peach
# Pear
# Hello



## While Loops
# While a `for` loop is great for iterating over items in a list or a range, a `while` loop 
# is used to repeat a block of code as long as a specific condition remains `True`.

# Syntax

# while something_is_true:
#     # Do something repeatedly

# The loop will continue to run as long as the condition `something_is_true` evaluates to `True`.

# Example 1:
# This loop will run 5 times
number_of_hurdles = 5
while number_of_hurdles > 0:
    print("Jumping a hurdle...")
    number_of_hurdles -= 1 # This line is crucial to prevent an infinite loop

print("Finished the race!")
