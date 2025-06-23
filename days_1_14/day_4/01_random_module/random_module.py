# Exercise

import random

# Random Whole Numbers Within a Range
    # This will produce a random whole number between 1 and 10 (inclusive).

random_integer = random.randint(1, 10)
print(f"Printing random integer: {random_integer}")

# Modules in Python
import my_module
    ## Python allows us to put code into different files and import that code
    # if needed. This means that we can better organise and modularise our code.
    ## You can create a new module simply by creating a new .py file,
    # and then you can import variables or functions from that file just by using the import keyword.
    ## Importing my module or any module to separate and facilitate the code debugging
print(f"Printing my module: {my_module.my_favorite_number}")


# Random.random
    # First random refers to the module and second to the function random.
    # The random module with random function gives us a random floating point number 0.0 <= X < 1.0
random_number_0_to_1 = random.random()
print(f"Random.Random: {random_number_0_to_1}")

    # Here we are expanding the number by multiplying by 10, so now it will be 0.0 <= X < 10.0
random_number_0_to_1 = random.random() * 10
print(f"Random.Random * 10: {random_number_0_to_1}")



# Random.Uniform
    # This will return a random floating point number N such that a<=N<=b for a<=b and b<=N<=a for b<a.
random_float = random.uniform(0, 10)
print(f"Random.Uniform: {random_float}")


# PAUSE 1 - Heads or Tails
# Create a coin flip program using what you have learnt about
# randomisation in Python. It should randomly print "Heads" or
# "Tails" everytime it is run.

coin_flip = random.randint(0 , 1)
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")
