import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)
lives = 6


# Here we choose the random word from the word_list.
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)


# Here is the placeholder with the same number of blanks as the chosen_word.
display = ["_"] * len(chosen_word)
print(f"{' '.join(display)}")

guessed_letters = []
game_over = False

while not game_over:
    
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    # Check guessed letter and update the display list
    if guess in guessed_letters:                 # This answers the question: "Has the user ever tried this letter before in this game?"
        print(f"You have already guessed letter: {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:       # This answers the question: "Is the user's current guess a correct letter?"
            guessed_letters.append(guess)
            display[position] = guess

    print(f"{' '.join(display)}")


    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.



    # If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
           
           # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")



    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])
