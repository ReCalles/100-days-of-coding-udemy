## Reeborgs Project Challenge
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Lost in a maze
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
# -Goal: Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have 
#  Reeborg follow along the right edge of the maze, 1-turning right if it can, 2-going straight ahead if it can’t 
#  turn right, or 3-turning left as a last resort.

# What you need to know
#   The functions move() and turn_left().
#   Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
#   How to use a while loop and if/elif/else statements.
#   It might be useful to know how to use the negation of a test (not in Python).


# Solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear(): # First we will check if front is clear to avoid the infinite loop where Right is clear and Front is clear. 
    move()
turn_left()             # Then we will turn left, so that now we have a Wall on the Right

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()  
    else: 
        turn_left()
    
    
# NOTE: This is the final solution or debbuged solution for this challenge.