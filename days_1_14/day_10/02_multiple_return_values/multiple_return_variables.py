### Multiple Return Variables

# Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.
# However, you can have multiple return statements in one function. So how does that work?

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("This willnot be printed.")   # This will not be executed do to the indentation and because it exits the function that is being called.

print(format_name("RicARdo", "EliAS CaLLeS"))



## Conditional Returns
# When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain 
# conditional checks, we can end up with multiple endings (returns).
# e.g.
# def canBuyAlcohol(age):
#     if age >= 18:
#         return True
#     else:
#         return False


## Empty Returns
# You can also write return without anything afterwards, and this just tells the function to exit.
# e.g.
# def canBuyAlcohol(age):
#     # If the data type of the age input is not a int, then exit.
#     if type(age) != int:
#         return

#     if age >= 18:
#         return True
#     else:
#         return False



    
def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":                    # In case the user doesnt type anything...
        return "You did not provide valid inputs"       # This is an early exit to avoid the previous issue.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name2(input("What is your first name?"), input("What is your last name?")))



# Exercise: Find Out if Leap Year

# Leap Year
# 💪 This is a difficult challenge! 💪 

# Write a program that returns True or False whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice


# This is how you work out whether if a particular year is a leap year. 
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder 
# - unless the year is also divisible by 400 with no remainder   



# If English is not your first language, or if the above logic is confusing, try using this flow chart.

# e.g. The year 2000: 
# 2000 ÷ 4 = 500 (Leap)  
# 2000 ÷ 100 = 20 (Not Leap)  
# 2000 ÷ 400 = 5 (Leap!)  
# So the year 2000 is a leap year. 

# But the year 2100 is not a leap year because: 
# 2100 ÷ 4 = 525 (Leap)  
# 2100 ÷ 100 = 21 (Not Leap)  
# 2100 ÷ 400 = 5.25 (Not Leap)  


# Warning
# Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation. 
# Example Input 1
# 2400
# Example Return 1
# True

# Example Input 2
# 1989
# Example Return 2
# False



def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    
    # year = int(input("Enter the year number? "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True   # This is a Leap Year.
            else:
                return False  # This is not a Leap Year.
        else:
            return True       # This is a Leap Year.
    else:
        return False          # This is not a Leap Year.
        
        
print(is_leap_year(2400))
