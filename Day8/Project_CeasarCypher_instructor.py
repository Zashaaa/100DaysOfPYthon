import string
from caesarcipherlogo import logo

alphabet = list(string.ascii_lowercase)
decoding = True
print(logo)


def ceasar(text_input, shift_amount, desired_direction):
    end_text = ""
    if desired_direction == "decode":
        shift_amount *= -1

    for letter in text_input:
        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")


while decoding:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    ceasar(text, shift, direction)
    one_more = input("Do you want another message to encode or decode? y/n\n").lower()
    if one_more == "n":
        print("Goodbye!")
        decoding = False
    elif one_more == "y":
        continue



