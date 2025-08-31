### Use a Debbuger

# Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.

# Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

# There are a couple of things that are the same in most IDEs which you should be familiar with:

# Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.

# Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.

# Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.

# Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.



# Following the course video we learned how to use the Debug console on PyCharm and used the following code as explanation.
'''import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])'''


# PAUSE 1
# Use the PyCharm debugger to figure out what is the issue in the starting code and fix it.

import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)                         # We just had to indent this line, based on the behavior of the debugger and identifying that b_list was never getting populated.
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])




# Extra tips for Debbugin

# 7 - Take a break.
# 8 - Ask a friend
# 9 - Run your code oftern to identify or prevent possible errors.
# 10- Ask StackOverflow
