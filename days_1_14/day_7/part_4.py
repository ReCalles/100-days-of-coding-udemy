import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
You Lose!
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
Lives 1/6
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
Lives 2/6
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Lives 3/6
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
Lives 4/6
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
Lives 5/6
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
Lives 6/6
''']
word_list = ["apple", "beach", "cloud", "dream", "eagle", "frog", "grape", "house", "island", "jumpy", "kite", "lemon", "moon", "novel", "ocean", "panda", "queen", "river", "sunny", "train"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.
lives = 6


# Here we choose the random word from the word_list.
chosen_word = random.choice(word_list)
print(chosen_word)


# Here is the placeholder with the same number of blanks as the chosen_word.
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)


correct_letters = []    # List is being created ouside the While loops so that it doesnt resets everytimne it runs the loop.
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Here is the display that puts a letter in the right position and _ in the rest.
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)


    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        game_over = True
        print("You won!")


    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])








#This is for step 1 purposes, we can comment now.
# # Check if the letter is one of the letter in  the chosen_word
# # for letter in chosen_word:
# #     if letter == guess:
# #         print("Right")
# #     else:
# #         print("Wrong")
