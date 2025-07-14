
# Previously, we've seen that functions allow us to package code into
# a named block which can be used repeatedly at a later point. Now we
# learned how to make our functions more dynamic by giving them inputs.
# By adding a variable name, called a parameter, inside the function's
# parentheses, we can pass in data when we call the function.
# This data, called an argument, allows the function to produce different
# results each time it's run.

# PAUSE 1 - Review
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def great():
    print("Hello")
    print("How are you doing viewer?")
    print("Do you like my Github profile?")

great()



# Inputs are Variables

# When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.
# The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.
# The value of the value of the input variable, e.g. Angela when you call the previous 
# greet function: greet("Angela") is called the argument.


# Functions that allow inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Angela")

# Another Example

def life_in_weeks(years):
    current_age_weeks = years * 52
    time_left = (90 * 52) - current_age_weeks
    print(f"You have {time_left} weeks left.")

life_in_weeks(26)