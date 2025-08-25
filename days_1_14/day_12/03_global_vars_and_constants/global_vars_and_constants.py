## Modifying Global Scope: Global Vars


# You can force the code allow you to modify something with global if you use the global keyword before you use it.

# e.g. This will give you an error
# a = 1
# def my_function():
#     a += 1
#     print(a)

# But this will work
# a = 1
# def my_function():
#     global a
#     a += 1
#     print(a)


# This will print 2 different values, because we have a local and global variables.

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")



# Modifying a Global Scope Variable

# The only issue, is that is a bad practice to modify a Global Variable.

enemies1 = 1

def increase_enemies():
     global enemies1
     enemies1 += 1
     print(f"enemies inside function: {enemies1}")


# What do we do then? We can so as follows, this is a better practice.
# We can return the current value plus the number you would like to change.

enemies2 = 1

def increase_enemies2(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1


enemies2 = increase_enemies2(enemies2)
print(f"enemies outside function: {enemies2}")




## Global Constants


# You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to mofy them.

# Naming Convention
# Global constants are normally declared in ALL_CAPS with a underscore in between.

# e.g.

# PI = 3.14159
# GOOGLE_URL = "https://www.google.com"



