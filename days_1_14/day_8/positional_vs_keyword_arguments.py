# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")



# Multiple Inputs
    # You can have multiple inputs in functions. All you need to do is separate them with a comma ,.
    # PAUSE 1
    # Create a function with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


    # PAUSE 2
    # Modify the function so that it prints the expected values.
print("Here we are showing Keyword Arguments")
greet_with("Jack Bauer", "Nowhere")



# Positional arguments
    # Positional Arguments
    # By default, when you create a function in Python, it will keep the order of arguments in the function definition.
print("Here we are showing Positional Arguments and the position error")
greet_with("Jack Bauer", "Nowhere")
greet_with("Nowhere", "Jack Bauer")


# Keyword arguments
    # Positional Arguments
    # By default, when you create a function in Python, it will keep the order of arguments in the function definition.
    # PAUSE 3
    # Call the greet_with() function using keyword arguments.
print("Here we are showing Positional Arguments")
greet_with(location="London", name="Angela")




# Activity
    # Love Calculator
    # You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

    # 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
    # 2. Then check for the number of times the letters in the word LOVE occurs.   
    # 3. Then combine these numbers to make a 2 digit number and print it out. 
    # e.g. name1 = "Angela Yu" name2 = "Jack Bauer"

    # T occurs 0 times 
    # R occurs 1 time 
    # U occurs 2 times 
    # E occurs 2 times 
    # Total = 5 

    # L occurs 1 time 
    # O occurs 0 times 
    # V occurs 0 times 
    # E occurs 2 times 
    # Total = 3 

    # Love Score = 53

    # Example Input 
    # calculate_love_score("Kanye West", "Kim Kardashian")
    # Example Output
    # 42
    
def calculate_love_score(name1, name2):
    true_love = ['t', 'r', 'u', 'e','l','o','v']
    combined_names = name1 + name2
    lower_combined_names = combined_names.lower()
    
    t = lower_combined_names.count("t")
    r = lower_combined_names.count("r")
    u = lower_combined_names.count("u")
    e = lower_combined_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_combined_names.count("l")
    o = lower_combined_names.count("o")
    v = lower_combined_names.count("v")
    e = lower_combined_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(f"The Love score is: {score}")

calculate_love_score("Kanye West", "Kim Kardashian")
    


