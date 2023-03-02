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
    print(logo)
    score = 0
    correct = True
    while correct:
        if score == 0:
            compare_a = get_item_to_compare([])  # First run
        else:
            compare_a = compare_b
        compare_b = get_item_to_compare(compare_a)
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        print(vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct = check_answer(compare_a, compare_b, answer)
        if correct:
            score += 1
    print(f"Game over! Your score is {score}")


game()
