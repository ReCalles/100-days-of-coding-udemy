import random
import hangman_words
import hangman_art

# Print hangman logo being imported from hangman_art.py.
print(hangman_art.logo)
lives = 6


# Here we choose the random word from the word_list.
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)    # This is the chosen word and its hidden from user.


# Here is the placeholder with the same number of blanks as the chosen_word.
display = ["_"] * len(chosen_word)
print(f"{' '.join(display)}")

guessed_letters = []
game_over = False

while not game_over:

    # Asks user for a letter to guess and prints the number of lives left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    

    # Check guessed letter to see if it has already been guessed.
    if guess in guessed_letters:                 # This answers the question: "Has the user ever tried this letter before in this game?"
        print(f"You have already guessed letter: {guess}")


    # This checks if the users current letter is a correct letter.
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:       # This answers the question: "Is the user's current guess a correct letter?"
            guessed_letters.append(guess)
            display[position] = guess
    print(f"{' '.join(display)}")


    # If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose". and display the chosen word.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")


    # Checks if there are no more blank spaces and if there are no more, that means we win and exit while loop.
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])
