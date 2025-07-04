# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in and store it in a variable.
# 3. Ask the user for the name of a pet and store it in a variable.
# 4. Combine the name of their city and pet and show them their band name.

#   You can use String Concatenation to combine strings with variables too!
#   e.g. 

# print("My name is " + name)

# 5. Make sure the input cursor shows on a new line:

#   Think about how you used \n to add a new line to a string. Try putting it in some different places in your code until it does what you expect. Note, when you click into the output area you will be able to click on the end of the line as well as the new line. See the video solution for how it looks on my system.

# ## Demo:
# [Try it out first here](https://appbrewery.github.io/python-day1-demo/)

print("Welcome to the Band Name Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name could be " + city + " " + pet)
