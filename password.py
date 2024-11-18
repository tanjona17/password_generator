import random
import string

def generate_pass(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars
    
    password = ""
    criteria = False
    has_number = False
    has_special = False
    
    while not criteria or len(password) < min_length:
        new_chars = random.choice(characters)
        password += new_chars
        
        if new_chars in digits:
            has_number = True
        elif new_chars in special_chars:
            has_special = True
        
        criteria = True    
        if numbers:
            criteria += has_number
        if special_characters:
            criteria = criteria and has_special
    
    return password    

min_lenght = int(input("Enter the minimum length"))
has_number = input("Do you want numbers in your password (y_n) ?").lower() == "y"
has_special = input("Do you want numbers in your special characters (y_n) ?").lower() == "y"
password = generate_pass(min_lenght,has_number,has_special)    
print("Your password is:", password)
    