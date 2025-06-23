
# Exercise

# Create a program that simulates a "Banker Roulette" game,
# where one person is randomly chosen from a list of names to
# pay the bill.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option #1
# This the simpliest way to print a random item from a list, it will randomly pick something from within a list.
print(random.choice(friends))

# Option #2
random_index = random.randint(0,4)
# This second option is taking random number from index 0 - 4 inclusive, but it will only work because we know the size of list.
print(friends[random_index])