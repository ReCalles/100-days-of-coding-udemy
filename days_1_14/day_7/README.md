# Day 7: Project - Hangman

Day 7 is a major milestone, combining everything we've learned so far—loops, lists, conditionals, and functions—to build a complete game from scratch: the classic word-guessing game, Hangman. This folder documents the entire development process, from initial planning to the final, polished code.

---

## Folder Contents

This directory contains all the files related to the Hangman project:

* **`part_1.py` to `part_5.py`**: These files represent the incremental development of the game, with each file corresponding to a major step in the project's logic.
* **`final_code.py`**: The complete, fully functional Hangman game.
* **`hangman_words.py`**: A Python module containing a list of words (`word_list`) from which the game randomly chooses.
* **`hangman_art.py`**: A Python module containing the game's ASCII art, including the logo and the `stages` of the hangman.
* **`my_hangman_flowchart_diagram.png`**: My personal flowchart created to plan the game's logic and flow before coding.
* **`course_solution_hangman_flowchart.png`**: The solution flowchart provided by the course for reference.
* **`basic_symbols_table.jpg`**: A reference image for symbols, likely used during the planning phase.

---

## The Development Process

The game was built iteratively, with each step adding a new layer of functionality.

### Step 1: `part_1.py` - Setup and Guessing
-   **Goal**: Choose a random word and check if a user's guessed letter is in that word.
-   **Concepts**: `random.choice()`, `input()`, `for` loops, and basic `if` statements.

### Step 2: `part_2.py` - Displaying Progress
-   **Goal**: Replace the blanks in a display list with correctly guessed letters.
-   **Concepts**: List manipulation, `range(len())` for positional iteration.

### Step 3: `part_3.py` - The Main Game Loop
-   **Goal**: Allow the user to guess repeatedly until the word is fully revealed.
-   **Concepts**: `while` loops, using the `in` keyword to check for remaining blanks.

### Step 4: `part_4.py` - Tracking Lives
-   **Goal**: Implement a life system and end the game if the player runs out of lives.
-   **Concepts**: Variable management, `if` statements with the `not in` keyword, and accessing list items by index (for the hangman `stages`).

### Step 5: `part_5.py` - Improving User Experience
-   **Goal**: Refine the game with better user feedback and code organization.
-   **Concepts**: Handling repeated guesses, providing clearer win/loss messages.

---

## Planning with Flowcharts

Before writing the final code, the game's logic was mapped out using flowcharts. This helps visualize the decision-making process (e.g., "Is the letter in the word?", "Are there lives left?"). This folder contains both my own planning flowchart (`my_hangman_flowchart_diagram.png`) and the course's example (`course_solution_hangman_flowchart.png`).

---

## Using Modules for Organization

To keep the main game file (`final_code.py`) clean and organized, the game's assets were stored in separate Python files and used as modules. This is a practical application of the concepts learned in previous lessons.

-   **`hangman_words.py`**: This file acts as a module that provides the `word_list` variable. It is imported into the main script.
-   **`hangman_art.py`**: This module contains the `logo` and `stages` variables (ASCII art), which are also imported and used for the game's visual presentation.

This separation of concerns makes the code easier to read, manage, and debug. The final, polished game is available in `final_code.py`.
```