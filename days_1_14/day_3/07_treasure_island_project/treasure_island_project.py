# Treasure Island Project

# Objective: our goal today is to build a "Chose your own adventure game". Using what you have 
# learnt in the lessons today you will be building a very simple version of this type of text game.

# Use the flow chart linked here (https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D) to create the game logic.


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? '
                      'Type "left" or "right"\n').lower()

if choice1 == "left":
    # Continue in the game
    choice2 = input('You\'ve reached a lake. '
                          'There is an island in the middle of the lake. '
                          'Type "wait" to wait for a boat. '
                          'Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        choice3 = input('You\' reached the island unharmed. '
                        'There is a house with 3 doors. '
                        'One red, one blue, and one yellow. '
                        'Which one you choose?\n').lower()

        if choice3 == "red":
            print("Its a room fool of fire. Game Over.")
        elif choice3 == "blue":
            print("You exited the house and went into the lake. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        else:
            print("You chose a door that doesnt exist. Game Over!")

    else:
        print("You got attacked by an angry trout. Game Over")

    # Lost the game
else:
    print("You fell into a hole. Game Over.")
