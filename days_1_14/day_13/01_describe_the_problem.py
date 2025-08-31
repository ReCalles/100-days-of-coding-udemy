### Describe the Problem



'''def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()'''

# Corrected code
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# Its loopiong from a range of values between 1 and 20, and after it reaches 20 it prints "You Got it."

# 2. When is the function meant to print "You got it"?
# After it reaches 20.

# 3. What are your assumptions about the value of i?
# range function is non inclusive of the value 20, and that is why its not printing
