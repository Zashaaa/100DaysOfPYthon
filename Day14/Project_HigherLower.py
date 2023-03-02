from art import logo, vs
from game_data import data
from random import choice


def get_item_to_compare(first_to_compare):
    item = choice(data)
    if item == first_to_compare:
        while item == first_to_compare:
            item = choice(data)
    return choice(data)


def check_answer(a, b, guess):
    if guess == 'a':
        if a["follower_count"] > b["follower_count"]:
            print("You are right!")
            return True
        else:
            print("WRONG")
            return False
    else:
        if b["follower_count"] > a["follower_count"]:
            print("You are right!")
            return True
        else:
            print("WRONG")
            return False


def game():
    compare_a = {}
    compare_b = {}
    correct = True
    while correct:
        if "name" in compare_a:
            compare_a = compare_b
        else:
            compare_a = get_item_to_compare([])  # First run
        compare_b = get_item_to_compare(compare_a)
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        print(compare_a["follower_count"])
        print(vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
        print(compare_b["follower_count"])
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct = check_answer(compare_a, compare_b, answer)


game()
