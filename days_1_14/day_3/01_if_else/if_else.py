# Exercise on Course Video
# https://appbrewery.github.io/python-day3-demo/



# Example Shown on video. We placed the condition that if User is shorter than 120cm, they can't ride the rollercoaster.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you cannot ride the rollercoaster!")