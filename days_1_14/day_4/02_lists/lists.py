# Exercise

# Example: in the case of the list of the states of the USA, we want to store them in the order as the join the Union.
    # So in this case we did a wiki research and save them in the order they join and they will display in that same order that they are stored in the list.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
                     "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California",
                     "Minnesota", "Oregon", "Kansas", "West Virginia",
                     "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho",
                     "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]


# Print Using Index from List
    # Here we are trying to print the number of the states which joined in X order.
print(f"Print from List: {states_of_america[5]}")


# Modify Values
    # We can also modify values inside the list, as an example, we want to rewrite the name of one state.
states_of_america[1] = "Pencilvania" # Here we are specifying the Index of Pennsylavania and changeing it for Pencilvania.
print(f"Print Modified index of list: {states_of_america[1]}")


# Add to List
    # The Append adds only ONE thing at a time to the end of a list.
states_of_america.append("Angeland")
print(f"Print states of america + 1 : {states_of_america}")

    # The Extend adds several things (list) to an existing list.
states_of_america.extend(["Angelopolis", "RicardosLand"])
print(f"Print states of america ++ : {states_of_america}")