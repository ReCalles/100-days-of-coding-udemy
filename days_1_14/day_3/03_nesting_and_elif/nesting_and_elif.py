# Exercise:

# Objective: Building on our basic rollercoaster eligibility program, your challenge is to 
# implement a new pricing structure based on the rider's age. This will involve using nested 
# conditional statements (if, elif, else).

# Instructions:

# If the rider is tall enough (120cm or more):
# Prompt them for their age.
# Based on age, print the price:
# Age 12 or less: Pay $5
# Age 13 to 18: Pay $7
# Age 19 or more: Pay $12


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
