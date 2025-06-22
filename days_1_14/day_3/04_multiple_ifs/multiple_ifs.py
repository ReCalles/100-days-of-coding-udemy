# Exercise

# Objective: Your task in this assignment is to enhance the existing rollercoaster program by calculating 
# a final total bill. Starting from the code that determines age-based ticket prices, you will 
# first initialize a bill variable to 0. Then, within the age-based pricing checks, assign the 
# appropriate ticket price directly to this bill variable, instead of just printing it 
# (you can also update the print messages to be more descriptive, like "Child tickets are $5."). 
# Following the age determination, the program should prompt the user if they desire a photo. 
# If the user indicates 'yes', an additional $3 must be added to their bill. Finally, 
# the program should print the user's total calculated bill, ensuring a clear and formatted output 
# such as "Your total bill is $X." for those eligible to ride.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Would you like to have a photo take? Type 'yes' or 'no' ")
    if wants_photo == 'yes':
        # Add $3 dollars to the bill
        bill += 3
        # If answer is no, we dont need an else if statement

    print(f"Your total bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
