import random

logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
'''

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
print(f"Psst, the number is {number_to_guess}")

right_input = False
while not right_input:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
        right_input = True
    elif difficulty == "hard":
        attempts = 5
        right_input = True
    else:
        print("Incorrect difficulty level , please try again....")

print(f"You have {attempts} attempts remaining to guess the number.")
