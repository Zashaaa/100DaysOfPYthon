from art import logo, vs
from game_data import data
from random import choice


compare_a = choice(data)
name_compare_a = compare_a["name"]
description_compare_a = compare_a["description"]
country_compare_a = compare_a["country"]
print(f"Compare A: {name_compare_a}, a {description_compare_a}, from {country_compare_a}.")
print(compare_a["follower_count"])
compare_b = choice(data)
if compare_b == compare_a:
    while compare_b == compare_a:
        compare_b = choice(data)
print(vs)
name_compare_b = compare_b["name"]
description_compare_b = compare_b["description"]
country_compare_b = compare_b["country"]
print(f"Against B: {name_compare_b}, a {description_compare_b}, from {country_compare_b}.")
print(compare_b["follower_count"])


def check_answer(guess):
    if guess == 'a':
        if compare_a["follower_count"] > compare_b["follower_count"]:
            print("You are right!")
            return True
        else:
            print("WRONG")
            return False
    else:
        if compare_b["follower_count"] > compare_a["follower_count"]:
            print("You are right!")
            return True
        else:
            print("WRONG")
            return False


answer = input("Who has more followers? Type 'A' or 'B': ").lower()
correct = check_answer(answer)
print(correct)


