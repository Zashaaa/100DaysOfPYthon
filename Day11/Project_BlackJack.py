import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []


def get_score(hand):
    score = 0
    for card in hand:
        score += card
    return score


for card in range(0, 2):
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

player_score = get_score(player_cards)

print(f"Your cards: {player_cards}.\nYour current score is {player_score}")
print(f"The dealers fist card is {dealer_cards[0]}")

player_lost = False
while not player_lost:
    want_card = input("Type \"y\" to get another card or press \"n\" to pass: ")
    if want_card == "y":
        player_cards.append(random.choice(cards))
    player_score = get_score(player_cards)
    print(f"Your cards: {player_cards}.\nYour current score is {player_score}")
    if player_score > 21:
        player_lost = True
        print("You've lost")
