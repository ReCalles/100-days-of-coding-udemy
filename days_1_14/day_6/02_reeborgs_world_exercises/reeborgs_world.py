## Reeborg's World Exercises:

# Exercise 1 
# Jumping over Fixed Hurdles: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# - Goal: Write a program using functions and `while` loops to guide a robot named Reeborg through a maze.

# What you need to know
#   The functions move() and turn_left().
#   The condition at_goal() and its negation.
#   How to use a while loop.
# Your program should also be valid for world Hurdles 1.

# Solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)




# Exercise 2 
# Jumping over hurdles that vary each time: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# -Goal: The position and number of hurdles changes each time this world is reloaded.

# What you need to know
#   The functions move() and turn_left().
#   The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
#   How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    


while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
        


# Exercise 3
# Jumping Over Hurdles with Variable Heights: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# - Goal: Write a program using functions and `while` loops to guide a robot named Reeborg through a maze but
# the position, the height and the number of hurdles changes each time this world is reloaded.

# What you need to know
#   You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine 
#   them for this last hurdles race.

# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

# Solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
    
while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()