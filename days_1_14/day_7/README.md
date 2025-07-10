# Day 7: Project - Hangman

Day 7 is a major milestone, combining everything we've learned so far—loops, lists, conditionals, and functions—to build a complete game from scratch: the classic word-guessing game, Hangman. This project is broken down into several steps, each building upon the last to create the final product.

---

## Step 1: Setting Up the Game

The first step is to establish the basic mechanics: choosing a word and checking the user's guess against it.

-   **TODO-1: Choose a Random Word**
    -   The program starts with a predefined list of words.
    -   Using the `random` module, a single word is randomly selected from this list and stored in a variable called `chosen_word`.

-   **TODO-2: Get User's Guess**
    -   The user is prompted to guess a letter.
    -   Their input is captured and converted to lowercase using the `.lower()` function to ensure case-insensitive matching.

-   **TODO-3: Check the Guess**
    -   A `for` loop iterates through each letter of the `chosen_word`.
    -   An `if` statement inside the loop checks if the user's `guess` matches the current letter in the iteration.
    -   "Right" is printed for a match, and "Wrong" is printed for a mismatch.

---

## Step 2: Displaying the Word and Guesses

Next, we need to create the visual representation of the hidden word and reveal letters as the user guesses them correctly.

-   **TODO-1: Create the Initial Display**
    -   An empty list called `display` is created.
    -   A `for` loop runs for the number of letters in the `chosen_word`. In each iteration, an underscore `_` is added to the `display` list.
    -   If `chosen_word` is "apple", the `display` list will be `['\_', '\_', '\_', '\_', '\_']`. This is then joined to be printed as a string for the user.

-   **TODO-2: Reveal Correctly Guessed Letters**
    -   The core logic is updated. We loop through each position of the `chosen_word` using `range(len(chosen_word))`.
    -   If the letter at the current position matches the user's `guess`, the underscore at that same position in the `display` list is replaced with the letter itself.
    -   For example, if the word is "apple" and the user guesses "p", the display becomes `_ p p _ _`.

---

## Step 3: Looping Until the Game Ends

This step introduces a `while` loop to allow the user to continue guessing until they have either won or lost the game.

-   **TODO-1: Implement the Main Game Loop**
    -   A `while` loop is used to repeat the guessing process.
    -   The loop continues as long as there are still underscores `_` in the `display` list.
    -   Once all underscores are gone, the loop ends, and a "You win." message is printed. The `in` keyword is useful here to check if `_` is still in `display`.

---

## Step 4: Tracking Player Lives and Game State

To make it a real game, there must be a consequence for wrong guesses. We introduce a life system and the "hanged man" ASCII art.

-   **TODO-1: Create a `lives` Variable**
    -   A variable called `lives` is initialized to `6`.

-   **TODO-2: Reduce Lives and Handle Game Over**
    -   An `if` statement checks if the user's `guess` is **not in** the `chosen_word`.
    -   If the guess is incorrect, `lives` is reduced by 1.
    -   The game loop now also checks if `lives` has reached `0`. If it has, a "You lose." message is printed, and the loop ends.

-   **TODO-3: Display the Hangman Art**
    -   A list called `stages` contains the ASCII art for each stage of the hangman, from 6 lives remaining to 0.
    -   After each guess, the program prints the stage from the `stages` list that corresponds to the current number of `lives`. For example, `stages[lives]` will show the correct art.

---

## Step 5: Final Touches and Refinements

The final step is to clean up the code, improve the user experience, and organize the project by importing assets from other files.

-   **TODO-1 & 2: Import Game Assets**
    -   The hardcoded `word_list` and `stages` are moved into separate Python files (`hangman_words.py` and `hangman_art.py`).
    -   These lists are then imported into the main script for use.

-   **TODO-3: Add a Logo**
    -   A game logo, also created with ASCII art, is imported from `hangman_art.py` and printed once at the very beginning of the game.

-   **TODO-4 & 5: Improve User Feedback**
    -   The logic is enhanced to give the user more specific feedback.
    -   If the user guesses a letter they have already guessed, the program informs them without deducting a life.
    -   If the user guesses an incorrect letter, the program explicitly states that the letter is not in the word before deducting a life.

-   **TODO-6 & 7: Final Output Messages**
    -   The print statements are updated to clearly show the user how many lives they have left and to reveal the correct word if they lose.
