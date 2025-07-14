# Day 8: Functions with Inputs & The Caesar Cipher

## Introduction to Day 8

Day 8 delves into a fundamental concept in programming: **Functions with Inputs (Parameters and Arguments)**. We explore how to create more flexible and reusable blocks of code by passing data into functions, which is then applied in building a multi-stage programming project: the Caesar Cipher.

## Concepts Learned:

* **Functions with Inputs (`functions_and_inputs.py`):**
    * Understanding how to define functions that accept specific pieces of information (parameters).
    * Learning how to pass arguments (the actual values) into these functions when they are called.
    * The benefits of using functions for code organization, reusability, and modularity.

* **Positional vs. Keyword Arguments (`positional_vs_keyword_arguments.py`):**
    * Distinguishing between positional arguments (where the order of arguments matters) and keyword arguments (where arguments are passed by name, making the order less critical and code more readable).
    * Understanding when and why to use each type of argument in function calls.

## Project: Caesar Cipher

This project guides through the development of the Caesar Cipher, a classic substitution cipher. We progressively build the functionality, enhancing it step-by-step from basic operations to a more robust and user-friendly command-line tool.

### Development Stages:

* **Part 1: Basic Encryption & Decryption (`caesar_cipher_1.py`)**
    * This initial stage focused on creating separate `encrypt()` and `decrypt()` functions to handle message encoding and decoding based on a given shift amount.

* **Part 2: Combining Functions into One (`caesar_cipher_2.py`)**
    * Here, we refactored the code to combine both the 'encrypt()' and 'decrypt()' logic into a single, versatile function named `caesar()`. This function now handles both encryption and decryption based on a 'direction' parameter.

* **Part 3: Improving the User Experience (`caesar_cipher_3.py`)**
    * This stage concentrated on enhancing the program's interaction with the user. It involved taking user input for the message, shift amount, and direction (encode/decode), and presenting the results clearly.

* **Final Version: Refinements and Robustness (`caesar_cipher_final.py`)**
    * This is the polished version of the Caesar Cipher program. The code has been cleaned up for better readability and efficiency.
    * **Key improvement:** It now includes enhanced error handling for user input. If the user makes a typo or enters an incorrect command (anything other than 'encode' or 'decode') for the direction, the program will prompt them that the command is incorrect, guiding them to try again.

### Supporting Files:

* `art.py`: This file contains the ASCII art logo that is displayed when the Caesar Cipher program runs, adding a visual element to the user experience.