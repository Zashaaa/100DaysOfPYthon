import random
import string

amount_letters = int(input("How many letters would you like in your password?\n"))
amount_numbers = int(input("How many numbers would you like in your password?\n"))
amount_symbols = int(input("How many symbols would you like in your password?\n"))

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
           '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

characters = []
total_characters = amount_letters + amount_numbers + amount_symbols
password = ""
##############
#    Easy    #
##############
# for letter in range(0, amount_letters):
#     letter_choice = random.randint(0, len(letters) - 1)
#     password = password + letters[letter_choice]
# for number in range(0, amount_numbers):
#     number_choice = random.randint(0, len(numbers) - 1)
#     password = password + numbers[number_choice]
# for symbol in range(0, amount_symbols):
#     symbol_choice = random.randint(0, len(symbols) - 1)
#     password = password + symbols[symbol_choice]
##############
#    Hard    #
##############
for character in range(0, total_characters):
    for letter in range(0, amount_letters):
        characters.append("letter")
    for number in range(0, amount_numbers):
        characters.append("number")
    for symbol in range(0, amount_symbols):
        characters.append("symbol")

    char_choice = random.choices(characters)

    if char_choice[0] == "letter":
        password += random.choice(letters)
        amount_letters -= 1
    elif char_choice[0] == "number":
        password += random.choice(numbers)
        amount_numbers -= 1
    else:
        password += random.choice(symbols)
        amount_symbols -= 1

    characters = []


print(f"Here is your password: {password}")
