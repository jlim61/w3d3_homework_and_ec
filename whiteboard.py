# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# On vacation in the Bahamas you decide to go out on a scuba trip one day.

# Unfortunately, disaster has struck!! The boat has caught fire!!

# You will be provided a string that lists many boat related items. Make a function called replace_fire that takes in a string (input) and if any of these items are "Fire" you must spring into action. Change any instance of "Fire" into "~~". Then return the string .

# input: "Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast",
# output: "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast"


# Porter Version

example = "Boat Rudder Mast Boat Hull Water Firemen Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast"

import re
def fire_fighter(astring):
    return re.sub(r'\bFire\b','~~',astring)

print(fire_fighter(example))


# Dylan Version

def replace_fire(astring):
    return ' '.join(map(lambda word: word if word != 'Fire' else '~~', astring.split()))

print(replace_fire(example))
