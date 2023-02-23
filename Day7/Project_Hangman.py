import random

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       ''')
# Images
pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]


# Lijst met te raden woorden
words = ["balloon", "talent", "adventure", "bye", "buy"]
# Kies een random woord uit
word_to_guess = random.choice(words)

# Maak een list met alle letters van het woord
list_word_to_guess = []
for letter in word_to_guess:
    list_word_to_guess.append(letter)

lenght_word_to_guess = len(word_to_guess)
show_word = ""  # Om te tonen aan de speler
list_printed_word = []  # Zelfde als show_word, maar dan in lijst

# Zorg dat alle letters verborgen zijn voor de speler
for letter in range(0, lenght_word_to_guess):
    list_printed_word.append("_")
    show_word += "_ "

# Laat het te raden "woord" zien, bestaat nu nog alleen uit underscores
print(f"Word to guess: {show_word}")
print(pics[0])

number_of_failes = 0
play_on = True

while play_on:
    # reset
    right_guess = False
    # list_guessed_letters = []
    guessed_letter = input("Guess a letter:\n").lower()
    print("\n\n")

    if len(guessed_letter) > 1:
        print("You can only guess 1 letter at a time")
    else:
        # Loop om te kijken of de gekozen letter voorkomt in het woord
        for letter in range(0, lenght_word_to_guess):
            if guessed_letter == list_word_to_guess[letter]:
                list_printed_word[letter] = guessed_letter
                # list_guessed_letters.append(guessed_letter)
                right_guess = True

            # Opbouwen van het te tonen woord aan de speler met alle garden letters op hun plek
            show_word = ""
            for letter in range(0, lenght_word_to_guess):
                show_word += list_printed_word[letter] + " "

        # Woord tonen aan de speler om te laten zien wat er tot nu toe geraden is
        print(f"Word to guess: {show_word}")

        # You lost a life
        if not right_guess:
            number_of_failes += 1

        # Toon de galg
        print(pics[number_of_failes])

        # Bepalen hoeveel letters nog geraden moeten worden
        letters_to_guess = 0
        for letter in range(0, lenght_word_to_guess):
            if list_printed_word[letter] == "_":
                letters_to_guess += 1
        if letters_to_guess == 0:
            print("You win!")
            play_on = False
        if number_of_failes == 6:
            print("You lose...")
            play_on = False

print("\n\nThnx for playing hangman!\nCoded by Louis Fares, 2023")
