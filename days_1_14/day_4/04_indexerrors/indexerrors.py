
# Exercise 1

# IndexError
    # When you try to access an item that is not in the range of the List, you will get an IndexError
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(len(states_of_america[50])) # This will give me an IndexError Out of range, because we are looking for an index that doesnt exist.

# To solve this we set an offset of -1
num_of_states = len(states_of_america) #50 -> 49
print(states_of_america[num_of_states - 1])


# Exercise 2

# Nested Lists
    # You can put Lists inside other Lists, this becomes something called a "Nested List" or a "2D List".

# This is a list that includes Fruits and Vegetables, but what if we want to have the 2 kinds of items separated and still being able to access them as they have something in common.
    # dirty_dozen = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pear", "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pear"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# What happens if we want to print something within the nested list?
    # print(dirty_dozen[2][3]) # Will give us an error due to the fact that first number is accesing the index of the nested list, and second number is accessing the index of items within that list.
print(dirty_dozen[0][3]) # Here we select list 0 -> fruits, and 3 -> Grapes