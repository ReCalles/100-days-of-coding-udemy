# Exercise: Mid-Life Crisis & Photo Refinement

# Objective and Desired Output: In this assignment, you will modify your rollercoaster code 
# further to introduce a special age-based discount and refine the photo option. Building on 
# your current program that calculates age-based ticket prices, your goal is so that people 
# age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age 
# is greater than 45, and it's also less than 55.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7.")
    elif 45<= age <= 55:   # Complex way to do it:  age >= 45 and age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill += 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
