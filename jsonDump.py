# Creates random bread "profiles" and dumps then to a JSON file randomly.


import json
import random

breads = json.load(r"./data/breads.json")

defaultbreadChoice = [
    {"name": "white bread", "desc": "greate for sandwich!."},
    {"name": "rye bread", "desc": "good if you want to be somewhat healthy..."},
]

randomBread = random.choice(defaultbreadChoice)

test = open("bredtest.json", "w")
json.dump(randomBread, test)
test.close()

#
# Dont delete this one yet, im using this for testing
#


# Notes for russian:
#
# a_file = open("bread.json", "w")
# json.dump(defaultbreadChoice, a_file)
# a_fil.close()
#
# End of notes for russian
