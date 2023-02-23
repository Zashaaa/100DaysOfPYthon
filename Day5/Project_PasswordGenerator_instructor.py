import random
import string

amount_letters = int(input("How many letters would you like in your password?\n"))
amount_numbers = int(input("How many numbers would you like in your password?\n"))
amount_symbols = int(input("How many symbols would you like in your password?\n"))

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
           '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

password_list = []
for letter in range(0, amount_letters):
    password_list.append(random.choice(letters))
for number in range(0, amount_numbers):
    password_list.append(random.choice(numbers))
for symbol in range(0, amount_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")
