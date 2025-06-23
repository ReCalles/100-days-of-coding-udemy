# Exercise

# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.
# Demo
# https://appbrewery.github.io/python-day4-demo/


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices_list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
if user_choice >= 0  and user_choice <= 2:
    print(choices_list[user_choice])


computer_choice = random.randint(0,2) # This will generate a random number between 0 and 2(choices_list)
print(f"Computer chose: {choices_list[computer_choice]}")

# We first needs to check if users choice is greater than 3 but less than 0, and then if that is 
# not true if we need to continue checking to see who won the game.
if user_choice >= 3 or user_choice < 0:         
    print("\nYou typed an invalid number. You lose!\n")
elif user_choice == 0 and computer_choice == 2: # This are exceptions saying that rock beats scissors
    print("You win!")
elif computer_choice == 0 and user_choice == 2: # This are exceptions saying that rock beats scissors
    print("You lose!")
elif user_choice > computer_choice:             # This is the normal case
    print("You win!")
elif computer_choice > user_choice:             # This is the normal case
    print("You lose!")
elif user_choice == computer_choice: 
    print("It's a draw")