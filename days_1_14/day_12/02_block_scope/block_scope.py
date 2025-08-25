## Block Scope


# Python is a bit different from other programming languages in that it does not have block scope.

# This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. They are given function scope if they are within a function or global scope if they are not.


game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


# If we want to create a new enemy and print out the result, this will definately work out, because its accessible. But what if we want to put this inside a new function?

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

#print(new_enemy)                # It will say there is an eeror here, because it cant access the value of new_enemy, because its not within the same level of indentation or the same block where its accessible.  That is why variable is also greyed out. (That is why we have commented this line to avoid error when running the code)



# This is the same example as before with the correct level of indentation or having the print on the block.

def create_enemy1():
    new_enemy1 = ""                 # We need to be very carefull and declare an empty variable otherwise we wont be creating nothing,   because there is no variable where we will be storing some value.
    if game_level < 5:
        new_enemy1 = enemies[0]

    print(new_enemy1)

create_enemy()                      # This wont print nothing because there is not output where the new_enemy variable is being called or accessed.
create_enemy1()                     # This will print out Skeleton, because the variable is being accessed and that is the logic of the Code.


# Exercise: Prime Number Checker

# Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  

# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.
# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.


# Example Input 1
# 73
# Example Output 1
# True
# Example Input 2
# 75
# Example Output 2
# False

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True

print(is_prime(73))
print(is_prime(75))