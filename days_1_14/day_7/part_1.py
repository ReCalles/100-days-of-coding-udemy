import random
word_list = ["apple", "beach", "cloud", "dream", "eagle", "frog", "grape", "house", "island", "jumpy", "kite", "lemon", "moon", "novel", "ocean", "panda", "queen", "river", "sunny", "train"]


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# Choose one random word from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)



# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Ask User to guess a letter
guess = input("Guess a letter: ").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
# Check if the letter is one of the letter in  the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")