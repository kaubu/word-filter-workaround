import data
import string
import random

print("Start sentence with '=' to change to strict set\n\
Start a sentence with '$' or '$=' to add diacritics\n\
Type ':q' to quit")

decisions = [True, False, False] # 1/3 times it will use a diacritic

def random_decision():
    return random.choice(decisions)

while True:
    sentence = input("\n>> ")

    diacritic_mode = False

    if sentence.startswith("="):
        charset = data.char_strict
        sentence = sentence[1:]
    elif sentence.startswith("$="):
        charset = data.char_strict
        diacritic_mode = True
        sentence = sentence[2:]
    elif sentence.startswith("$"):
        charset = data.char_generous
        diacritic_mode = True
        sentence = sentence[1:]
    elif sentence == ":q" or sentence == ":quit":
        break
    else:
        charset = data.char_generous
    
    result = ""
    
    for letter in sentence:
        if letter == " " or letter in string.punctuation:
            result += letter
            continue
        
        if letter in charset.keys():
            if diacritic_mode and random_decision(): # Add a diacritic
                new_letter = letter + random.choice(data.diacritics)
                result += new_letter
            else: # Just add new letter
                result += random.choice(charset[letter])
        else:
            result += letter
    
    print(result)

print("\nGoodbye!")