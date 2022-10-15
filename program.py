import data
import string
import random

print("Start sentence with '=' to change to strict set\n\
Start a sentence with '$' or '$=' to add diacritics\n\
Type ':q' to quit")

decisions = [True, False] # 

def random_decision():
    return random.choice(decisions)

while True:
    profanity_check = input("Do you want to have profanity check on? (must have 'profanity-check' installed) [Y/n]: ")

    if profanity_check == "" or profanity_check.lower() == "y" or profanity_check.lower() == "yes":
        print("Turning profanity check on...")
        profanity_check_mode = True
        from profanity_check import predict, predict_prob
        break
    elif profanity_check.lower() == "n" or profanity_check.lower() == "no":
        print("No profanity check selected")
        profanity_check_mode = False
        break

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
    
    print(f"\n{result}")
    if profanity_check_mode:
        if predict([sentence]) == [0]:
            sentence_prediction = "No"
        elif predict([sentence]) == [1]:
            sentence_prediction = "Yes"
        else:
            print("error")

        if predict([result]) == [0]:
            result_prediction = "No"
        elif predict([result]) == [1]:
            result_prediction = "Yes"
        else:
            print("error")

        print(f"[Original] Profanity detected: {sentence_prediction}")
        print(f"[New] Profanity detected: {result_prediction}")
        print(f"[Original] Profanity percentage: {predict_prob([sentence])[0]*100:.2f}%")
        print(f"[New] Profanity percentage: {predict_prob([result])[0]*100:.2f}%")

print("\nGoodbye!")