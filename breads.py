import json
import random

with open("./data/breads.json", "r") as file:
    breads = json.load(file)


def get(name=None):
    if name is None:
        return random.choice(breads["breads"])
    else:
        for bread in breads["breads"]:
            if bread["name"] == name:
                return bread
        return {"name": "not found :o"}


defaultbreadChoice = [
    {"name": "white bread", "desc": "greate for sandwich!."},
    {"name": "rye bread", "desc": "good if you want to be somewhat healthy..."},
]


def getRandom():
    breadData = open("./data/breads.json", "r")

    breads = json.load(breadData)  # lots of bread, kinda hard to read ngl | lol
    
    randomBread = random.choice(breads["breads"])

    listRandom = open("randomBread.json", "w")
    json.dump(randomBread, listRandom)
    listRandom.close()#Lmao
    return #the bread? | why return the bread, was it moldy? (bad joke)


# Chat
# RD: I dunno how the api is gonna work
# fl: make functions to get random and get by name, ill add it in api cog
# RD: ok
# RD: https://mrconos.pythonanywhere.com/rock/random <= like this?
# fl: yes ill add the path
# RD: ok
# fl : i added /bread/random in cog in bread.py
# --------------------------------------------------------------------------
# RD: did you just build it?
# aight i gona close liveshare, i gtg out
# RD: aight, cya
# bye

