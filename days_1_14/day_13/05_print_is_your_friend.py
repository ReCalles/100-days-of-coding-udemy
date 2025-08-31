### Print is Your Friend


# print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code. But during the loop it's difficult to see the intermediate values, that's a perfect example of how you can use print to expose those intermediate values and help you debug your code.

# Orignal Code

'''word_per_page = 0
pages = int(input("Number of pages: "))     # 50
word_per_page == int(input("Number of words per page: "))   # 250
total_words = pages * word_per_page
print(total_words)                          # 0 '''



# PAUSE 1
# The code is supposed to calculate the total number of words given the number pages and the word per page. But it's not currently giving any output. Diagnose the problem using print() statements.

'''word_per_page = 0
pages = int(input("Number of pages: "))     # 50
print (pages)

word_per_page == int(input("Number of words per page: "))   # 250     # Error is here, because we are using double "==" instead of a single to asising a value to a varaible.
print(word_per_page)


total_words = pages * word_per_page
print(total_words)                          # 0 '''




# PAUSE 2
# Fix the code.

word_per_page = 0
pages = int(input("Number of pages: "))     # 50
print (pages)

word_per_page = int(input("Number of words per page: "))   # 250
print(word_per_page)


total_words = pages * word_per_page
print(total_words)                          # 0 

