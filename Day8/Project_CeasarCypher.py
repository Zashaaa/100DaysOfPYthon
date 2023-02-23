import string

alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))


def ceasar(text_input, shift_amount, desired_direction):
    output = ""
    if desired_direction == "encode" or desired_direction == "decode":
        if shift_amount > 26:
            shift_amount = shift_amount % 26

        for char in text_input:
            for i in range(0, len(alphabet)):
                if char == alphabet[i]:
                    if desired_direction == "encode":
                        output += alphabet[(i + shift_amount) % 26]
                    else:
                        if i - shift_amount < 0:
                            output += alphabet[((i - shift_amount) + 26)]
                        else:
                            output += alphabet[(i - shift_amount)]

        print(f"The {direction}d text is: {output}")
    else:
        print(f"Invalid input: {direction}")


ceasar(text, shift, direction)


