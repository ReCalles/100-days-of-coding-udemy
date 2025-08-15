### Blackjack Capstone Project

# Chose your difficulty
# - Normal 😎: Use all Hints below to complete the project.
# - Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# - Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# - Expert 🤯: Only use Hint 1 to complete the project.

# Our Blackjack Game House Rules
# - The deck is unlimited in size.
# - There are no jokers.
# - The Jack/Queen/King all count as 10.
# - The Ace can count as 11 or 1.
# - Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# - The cards in the list have equal probability of being drawn.
# - Cards are not removed from the deck as they are drawn.
# - The computer is the dealer.

import random
import art
import os
import platform # To detect the operating system
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def clear_screen():
    """Clears the terminal screen based on the operating system."""
    if platform.system() == "Windows":
        os.system('cls') # Command for Windows
    else:
        os.system('clear') # Command for macOS/Linux/Unix
        
        


def calculated_score (cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:            # Check for Blackjack and return 0 to end game ends immediately.
        return 0
    
    # Check for Aces (11s) and turn them into 1s in case we are over 21.
    while 11 in cards and sum(cards) > 21:              # We use a while loop because there can be many instances where we draw 11 several times and we want to turn 11s into 1s.
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)
    
    
    

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"




def play_game():                                  
    print (art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    users_score = -1
    is_game_over = False
    
    user_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    
    while not is_game_over:                                                                 # Checks if game is terminated or not by the User, if 21 is obtained, or we got above 21.
        users_score = calculated_score(user_cards)
        computer_score = calculated_score(computer_cards)
    
        print(f"\nYour cards are: {user_cards}, current score: {users_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        
        if users_score == 0 or computer_score == 0 or users_score > 21:                     # Cheks if cards are 21 or user got above 21 and terminates program.
            is_game_over = True
        else:
           users_choice = input("Type 'y' to get another card, type 'n' to pass: ")         # Asks User if he wants to pass or draw another card.
           if users_choice == "y":
               user_cards.append(random.choice(cards))                                      # Adds another card to the hand.
           else:
               is_game_over = True                                                          # Terminates program if User doesnt want to draw more cards.
    
    while computer_score != 0 and computer_score < 17:                                      # Once User is done drawing cards, we finish drawing cards for Computer and we calculate the score.          
        computer_cards.append(random.choice(cards))
        computer_score = calculated_score(computer_cards)

                                                                                            # Once Computer and User finished drawing cards we show the hands and final scores.
    print(f"\nYour final hand: {user_cards}, final score: {users_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} \n")
    print(compare(users_score, computer_score))                                             # We compare the scores to display the veredict of who wins.
    
    
    


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_screen()
    play_game()

