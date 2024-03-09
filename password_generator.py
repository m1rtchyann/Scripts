import random
import string
from termcolor import cprint, colored

def generate_password(length: int) -> string:
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ""
    for i in range(length):
        symbol = random.choice(characters)
        #Checks whether a character is repeated or not
        while symbol in password:
            symbol = random.choice(characters)
        password += symbol
    return password

cprint("Let's create your strong password!!!", "green", attrs=["bold"])
while True:
    length = input("Input password length: ")
    if length.isdigit():
        length = int(length)
        if length < 8:
            cprint("Password length must be at least 8.", "red")
        else:
            password = generate_password(length)
            print("Here is your password:", end=' ')
            cprint(password, "green", attrs=["bold"])
            break
    else:
        cprint("Invalid input. Please, enter a number: ", "red")