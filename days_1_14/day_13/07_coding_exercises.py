### Coding Exercises

# After this course lecture I was prompted with some coding exercises


# 1- Coding Exercise: Debugging Odd or Even

# - Read the code in exercise.py - Spot the problems 🐞. - Modify the code to fix the program. Fix the code so that it works and passes the tests when you submit.
# You can copy and paste the code into PyCharm to help you debug.   

def odd_or_even(number):
    if number % 2 == 0:                             # We just added an extra "=".
        return "This is an even number."
    else:
        return "This is an odd number."
    
    
    
    
# 2- Coding Exercise: Debugging Leap Year

# - Read the code in exercise.py
# - Spot the problems 🐞.
# - Modify the code to fix the program.   

# Fix the code so that it works and when you hit submit it should pass all the tests. 
# This is how you work out whether if a particular year is a leap year.

# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder

# You can paste the code into PyCharm to help you debug.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:      # The error was here, because originally it said 4000, which is incorrect, it needs to be 400 in order to be leap year.
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))
print(is_leap(2020))
print(is_leap(1900))
print(is_leap(2021))
print("\n")



# 3- Coding Exercise: Debugging FizzFuzz

# - Read the code in exercise.py
# - Spot the problems 🐞. 
# - Modify the code to fix the program. 
# - No shortcuts 
# - don't copy-paste to replace the code entirely with a previous working solution.   

# The code needs to print the solution to the FizzBuzz game.   

# - Your program should print each number from 1 to x where x is the input number. 
# - However when the number is divisible by 3 then instead of printing the number it should print "Fizz".   
# - When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
# - And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".


# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:         # Error was here because we originally had an "or" statementinstead of an "and", which verifies that both expressions are met in order to print the correct phrase.
            print("FizzBuzz")
        elif number % 3 == 0:                           # We had to change here the "If" into an "Elif"
            print("Fizz")
        elif number % 5 == 0:                           # We had to change here the "If" into an "Elif" 
            print("Buzz")
        else:
            print(number)                               # We had to remove the "[]" so that it printed out the correct expected result.


print(fizz_buzz(25))
