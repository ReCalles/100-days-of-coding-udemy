bmi = 84 / 1.65 ** 2


# ### Flooring a Number
# You can floor a number or remove all decimal places using the `int()` function which converts a floating point number (with decimal places) into an integer (whole number).

# `int(3.738492) # Becomes 3` 

# Original Float with decimal places
print(bmi)

# Flooring the number by converting it into int
print(int(bmi))


# ### Rounding a Number
# However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python `round()` function.

# `round(3.738492) # Becomes 4`
# `round(3.14159) # Becomes 3`
# `round(3.14159, 2) # Becomes 3.14`

# Rounding the number into a whole number
print(round(bmi))

# Rounding only to 2 decimal places
print(round(bmi, 2))


# ### Assignment Operators
# Assignment operators such as the addition assignment operator `+=` will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

# `+=`
# `-=`
# `*=`
# `/=`

## Accumulate
score = 0

# User scores a point
score += 1
print(score)

#Also
score -= 1
score *= 2
score /= 2

# ### f-Strings
# In Python, we can use f-strings to insert a variable or an expression into a string.

# `age = 12`
# `print(f"I am {age} years old")`
# `# Will output I am 12 years old.`

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
