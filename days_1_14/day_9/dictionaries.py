# A dictionary in Python functions similarly to a dictionary in real life. It's a data structure that allows us to associate a key to a 
# value and pair the two pieces of data together.
# e.g
# dictionary = {key:valaue, key2:value2...}


# This is how you create a dictionary in Python:
# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

# This is how you retrieve items from a dictionary:
print(colours["pear"])
#Will print "green"

# This is how to create an empty dictionary:
my_empty_dictionary = {}

# This is how you can add new items to an existing dictionary:
colours["peach"] = "pink"

# This is also how you can edit an existing value in a dictionary:
colours["apple"] = "green"

# This is how to loop through a dictionary and print all the keys:
print("Printing Keys: ")
for key in colours:
    print(key)
    
# This is how to loop through a dictionary and print all the values:
print("Printing Values from the keys: ")
for key in colours:
    print(colours[key])
    
    
# Course Example:
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}
print(f"Printing Original dictionary: {programming_dictionary}\n")

# Retieving a key from example dictionary.
print(f"Your value from requested Key is: {programming_dictionary["Bug"]}\n")

# Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(f"Printing dictionary with new added Key: {programming_dictionary}\n")

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(f"Printing wiped dictionary: {programming_dictionary}\n")

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(f"Printing edited dictionary: {programming_dictionary}\n")

# Loop through a dictionary
print("Loop through Dictionary: \n")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
# Loop through a dictionary 2

print("Loop through Dictionary2: \n")
for key in colours:
    print(key)
    print(colours[key])
    
    
# Grading Program Exercies

print("Grading Program Exercise: \n")


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)