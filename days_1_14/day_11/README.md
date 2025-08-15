# Day 11: The Blackjack Capstone Project

Day 11 marks a significant milestone: the first "Capstone Project." The goal was to combine all the Python skills learned so far—including functions, loops, lists, dictionaries, and conditional logic—to build a complete, playable game of Blackjack from the ground up.

## 1. The Goal & House Rules

The objective was to create a command-line version of the card game Blackjack. Before coding, the first step was to clearly define the rules for our specific version of the game:

* **The Deck**: The deck is unlimited in size, and cards are not removed after being drawn. This simplifies the logic by ensuring the probability of drawing any card is always the same. The deck is represented by the list: `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`.
* **Card Values**:
    * Numbered cards are worth their face value.
    * Jack, Queen, and King are all worth 10.
    * The Ace is special: it counts as 11, unless the hand's total goes over 21, in which case it automatically counts as 1.
* **The Dealer**: The computer plays the role of the dealer.

## 2. Planning the Logic

Before writing any code, the project emphasized the importance of planning. This involved:

1.  Playing a real version of the game to understand the flow.
2.  Reading a detailed breakdown of the program's requirements.
3.  Creating a **flowchart** to map out the game's logic, decisions, and outcomes. This helps visualize the program's structure before implementation.

## 3. Building the Core Components (Functions)

The program was built in a modular way, with each piece of logic encapsulated in its own function.

### `calculated_score()`

This was the most complex and critical function. It takes a list of cards (a hand) as input and returns the score. Its logic was built in three parts:

1.  **Check for Blackjack**: It first checks if the hand is a "Blackjack" (a two-card hand totaling 21). In our game, a Blackjack is represented by a score of `0` to signal an instant win/loss.
2.  **Handle the Ace**: If the score is over 21 and there is an Ace (an 11) in the hand, this function uses a `while` loop to cleverly remove the 11 and replace it with a 1, then recalculates the score. This correctly implements the Ace's special rule, even for multiple Aces.
3.  **Sum the Cards**: If neither of the above conditions is met, it returns the simple sum of the cards in the hand.

### `compare()`

This function is called at the end of the game. It takes the final scores of the user and the computer as inputs and determines the outcome by running through a series of conditional checks to see who won, who lost, or if it was a draw.

### `clear_screen()`

A helper function was created to clear the console screen between games. It intelligently checks the operating system (Windows, macOS, or Linux) and uses the correct system command (`cls` or `clear`) for a clean user experience.

## 4. Implementing the Game Flow

With the core functions built, the main game logic was orchestrated within a `play_game()` function.

1.  **The Initial Deal**: At the start of a game, both the user and the computer are dealt two random cards using `random.sample(cards, 2)`.
2.  **The User's Turn**: A `while` loop is used to manage the user's turn. The loop continues as long as the user's score is not over 21 and they want to draw another card ("hit"). For each hit, a new card is added using `random.choice(cards)`. After each new card, the score is recalculated. If the user decides not to draw another card ("stand"), their turn ends.
3.  **The Computer's Turn**: After the user's turn, the computer plays. Its logic is simpler: a `while` loop makes the computer keep drawing cards as long as its score is less than 17.
4.  **Determining the Winner**: Once both turns are over, the `compare()` function is called to evaluate the final hands and print the result.
5.  **Restarting the Game**: The entire game is wrapped in a global `while` loop that asks the user if they want to play another round. If they answer "yes," the `clear_screen()` and `play_game()` functions are called to start a new game.