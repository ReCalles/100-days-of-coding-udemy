letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random


# Easy Version

# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$*924

# You can see that all the letters are together. All the symbols are together and all the numbers 
# follow each other as well. Try to solve this problem first.

# HINT: Remember you can use the random.choice() function to get a random item from a List! But you need to 
# import the random module first.

easy_password = ""

print("Welcome to the Easy PyPassword Generator!")
nr_letters_easy = int(input("How many letters would you like in your password?\n"))
nr_symbols_easy = int(input(f"How many symbols would you like?\n"))
nr_numbers_easy = int(input(f"How many numbers would you like?\n"))


for letter in range(0, nr_letters_easy):
  easy_password += random.choice(letters)

for symbol in range(0, nr_symbols_easy):
  easy_password += random.choice(symbols)        

for number in range(0, nr_numbers_easy):
  easy_password += random.choice(numbers)

print("Easy Version Pasword: " +    easy_password)




# Hard Version

# When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of 
# this project the final password does not follow a pattern. So the example above might look like this:

# x$d24g*f9

# And every time you generate a password, the positions of the symbols, numbers, and letters are different. 
# This will make the password more difficult for hackers to crack.

# The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not 
# memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, 
# check the hint below for what to Google.
# HINT: Try googling: "How to shuffle items in a List in Python"

hard_password = []

print("\n\nWelcome to the Hard PyPassword Generator!")
nr_letters_hard = int(input("How many letters would you like in your password?\n"))
nr_symbols_hard = int(input(f"How many symbols would you like?\n"))
nr_numbers_hard = int(input(f"How many numbers would you like?\n"))

for letter in range(0, nr_letters_hard):
  hard_password.append(random.choice(letters))

for symbol in range(0, nr_symbols_hard):
  hard_password.append(random.choice(symbols))        

for number in range(0, nr_numbers_hard):
  hard_password.append(random.choice(numbers))


print(f"Hard Password List (Original) :   {hard_password}")
random.shuffle(hard_password)
print(f"Hard Password List (Shuffled) :  {hard_password}")

password = ""   # We need to create a string from our Hard Shuffle Password List, since every value is still stored on a list.

for char in hard_password:
  password += char

print(f"Hard Version Password:  {password}")


