from random import *
names = []
while len(names) <= 2:
    name = input("Type the name of a person: ")
    names.append(name)

name = choice(names)
"""print(name)"""
test = bool
test = True
while test:
    name_choice = input("I'm thinking about the name in the list , Can you guess it ? ")
    if name_choice == name:
        print("You guess it ! I'am thinking about ", name)
        answer = input("Do you try again ? ")
        if answer.upper() == "NO":
            test = False
        else:
            name = choice(names)
    else:
        print("No, Try again ")
