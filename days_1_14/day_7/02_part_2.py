import random
word_list = ["apple", "beach", "cloud", "dream", "eagle", "frog", "grape", "house", "island", "jumpy", "kite", "lemon", "moon", "novel", "ocean", "panda", "queen", "river", "sunny", "train"]


# Choose one random word from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)


# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# Here is the placeholder with the same number of blanks as the chosen_word.
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
    
# Ask User to guess a letter
guess = input("Guess a letter: ").lower()


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# Here is the display that puts a letter in the right position and _ in the rest.
display = ""
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"
print(display)

        
# Check if the letter is one of the letter in  the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")