# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

all_chars = [letters, numbers, symbols]

password = ""

# Implemented in a 'not python' way
# Most of the code could be replaced by random.shuffle
# However, this way will work in any programming language

for i in range(nr_letters + nr_symbols + nr_numbers):
    type = random.randint(0, 2)
    is_good = False
    while not is_good:
        if type == 0 and nr_letters > 0:
            nr_letters -= 1
            is_good = True
        elif type == 1 and nr_numbers > 0:
            nr_numbers -= 1
            is_good = True
        elif type == 2 and nr_symbols > 0:
            nr_symbols -= 1
            is_good = True
        else:
            type = random.randint(0, 2)

    value = all_chars[type][random.randint(0, len(all_chars[type]) - 1)]
    password += value

print(password)