import random
import string

def generate_password(min_length,numbers= True,special_characters= True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""

    meet_criteria = False
    has_numeric = False
    has_special = False

    while not meet_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_numeric = True  
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_numeric
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return password

min_length = int(input("Enter the minimum length of the password: "))
has_numbers = input("Should the password contain numbers? (yes/no): ").strip().lower() == 'yes'
has_special = input("Should the password contain special characters? (yes/no): ").strip().lower() == 'yes'

pwd = generate_password(10,True,False)

print(pwd)


   




