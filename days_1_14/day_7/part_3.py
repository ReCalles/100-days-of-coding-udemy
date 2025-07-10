import random
word_list = ["apple", "beach", "cloud", "dream", "eagle", "frog", "grape", "house", "island", "jumpy", "kite", "lemon", "moon", "novel", "ocean", "panda", "queen", "river", "sunny", "train"]

# Here we choose the random word from the word_list.
chosen_word = random.choice(word_list)
print(chosen_word)


# Here is the placeholder with the same number of blanks as the chosen_word.
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
correct_letters = []    # List is being created ouside the While loops so that it doesnt resets everytimne it runs the loop.
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()


    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
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

    if "_" not in display:
        game_over = True
        print("You won!")









#This is for step 1 purposes, we can comment now.
# # Check if the letter is one of the letter in  the chosen_word
# # for letter in chosen_word:
# #     if letter == guess:
# #         print("Right")
# #     else:
# #         print("Wrong")
