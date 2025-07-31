
# Nesting a List inside a Dictionary
    # Instead of a String value assigned to a key, we can replace it with a List. You can nest a List in a Dictionary like this:

# my_dictionary = {
#     key1: [List],
#     key2: Value,
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# PAUSE 1
# See if you can figure out how to print out "Lille" from the nested List called travel_log.

#  Hint 1 
# To get this part: ["Paris", "Lille", "Dijon"] You would need: travel_log["France"]
# Therefore to get Lille, you need: travel_log["France"][1]


# The values inside this Dictonarie is a list wit 3 values.
travel_log = {
    "France": ["paris", "lille", "dijon"],
    "Germany": ["stuttgart", "berlin"],
}

# print Lille
print(f"This is the value inside a list from a key in a dictionarie: {travel_log["France"][1]}")




# Nesting Lists inside other Lists

nested_list = ["A", "B", ["C", "D"]]


# PAUSE 2
# Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.

#  Hint 2 
# To get this list: ["C", "D"] we need the code:
# nested_list[2]

# Therefore, to get "D" we need:

print(f"This is the value of an object within a nested list: {nested_list[2][1]}")




# Nesting a Dictionary inside a Dictionary
    # You can also nest a dictionary in a dictionary:

# my_dictionary = {
#     key1: Value,
#     key2: {Key: Value, Key: Value},
#     key3: {Dict}
# }

# PAUSE 3
# Figure out how to print out "Stuttgart" from the following list:



# This example showcase a list (eg. Paris, Lille, Dijon), within a dictionarie (eg. France or Germany), which is also nested within another dictionarie (eg. travel log).
travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

# Print Stuttgart

print(travel_log2["Germany"]["cities_visited"][2])