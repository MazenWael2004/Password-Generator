import random
import string
def generate_password(min_length,numbers=True,special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    characters = letters

    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    pwd = ""
    has_num = False
    has_special = False


    while len(pwd) < min_length:
     char = random.choice(characters)
     pwd+=char
    
    return pwd

print(generate_password(120))


