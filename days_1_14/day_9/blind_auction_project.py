
from art import logo
import os
import platform                             # To detect the operating system
print(logo)


def clear_terminal():                       # Clears the terminal screen based on the operating system.
    if platform.system() == "Windows":
        os.system('cls')                    # Command for Windows
    else:
        os.system('clear')                  # Command for macOS/Linux
        
        

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
   
    # NOTE: This is a fastest and shorter version of doign the same to find highest bidder.
    # inverse = [(value, key) for key, value in bidding_record.items()]
    # print(max(inverse)[1])                 # This is only printing the name of the highest bidder for the moment.
   
    
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] # This loops through the dictionarie, and cheks the bid_amount value.
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")




# TODO-1: Ask the user for input
blind_auction_bid = {}
more_bidders = True

while more_bidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))


    # TODO-2: Save data into dictionary {name: price}
    blind_auction_bid[name] = bid
    # print(blind_auction_bid)              # TEST
        

    # TODO-3: Whether if new bids need to be added
    valid_input_received = False
    while not valid_input_received:         # Loop until we get a 'yes' or 'no'
        another_bidder = input("Are there any more bidders? Type 'yes' or 'no'. ").lower()
        
        if another_bidder == "no":
            more_bidders = False            # Stops the outer loop.
            valid_input_received = True     # Exits this inner loop.
            clear_terminal()
            find_highest_bidder(blind_auction_bid)
            
        elif another_bidder == "yes":
            valid_input_received = True     # Exits this inner loop (outer loop continues).
            clear_terminal()
            
        else:
            print("Incorrect input. Please Type 'yes' or 'no'. ")
           
# print(blind_auction_bid)                  # TEST
