### Reproduce The Bug

from random import randint


# Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug.

# PAUSE 1
# Change the code so that it always produces the occasional error.

'''e_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6                                        # This value produces the error.
print(dice_images[dice_num])
'''

# PAUSE 2
# Fix the code and remove the bug.


dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
