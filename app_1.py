import json

import re
from spellchecker import SpellChecker

# setting variables and loading in dataset and spellchecker operation
data = json.load(open("data.json"))
spell = SpellChecker()

# function takes user input word
def eng_dict():
    while True:
        try:
            # takes user's word input and checks if word is in the data file
            # also check for correct spelling if word not found
            # will offer a 'Did you mean? ___' as an alternative
            word = input("Enter word here to see definition: ").lower()
            correct = spell.correction(word)
            if word == correct:
                answer = data[word]
            else:
                right_word = input(f"Did you mean: {correct}? (y/n) ")
                if right_word.lower()[0] == 'y':
                    answer = data[correct]
                else:
                    continue
            # if word is not found - will capitalize the words and check again
            # will also make whole word uppercase to check for acronyms (eg. USA)
        except KeyError:
            proper_noun = word.title()
            miss_proper = correct.title()
            acronym = word.upper()

            if proper_noun in data:
                answer = data[proper_noun]
                break
            elif miss_proper in data:
                answer = data[miss_proper]
                break
            elif acronym in data:
                answer = data[acronym]
                break
            # if not found after checking all instances of the word
            #will return 'word does not exist' and will let user re-enter input
            else:
                print('Word does not exist. Try again.')
                continue
        else:
            # entered acceptable input
            break

    output = answer
    # prints out definition of words
    # if multiple definitions, will split to new line for more readability
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

# function for asking user if they would like to continue looking for words
# if so, will loop back to the original function
def another_word():
    while True:
        decision = input("Look up another word? (y/n) ")
        if decision.lower()[0] == 'y':
            eng_dict()
        else:
            break

#functions being executed to run program
eng_dict()
another_word()
