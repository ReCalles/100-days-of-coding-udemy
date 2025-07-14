# Day 8: Caesar Cipher

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