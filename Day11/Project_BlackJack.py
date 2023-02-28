import random
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []


def get_score(hand):
    if sum(hand) > 21 and hand_contains_ace(hand):
        replace_next_ace(hand)
        get_score(hand)
    return sum(hand)


def hand_contains_ace(hand):
    for card in hand:
        if card == 11:
            return True
    return False


def replace_next_ace(hand):
    for i in range(0, len(hand)):
        if hand[i] == 11:
            hand[i] = 1
            return


def deal_card():
    return random.choice(cards)


# Deal each player 2 cards
for card in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

player_score = get_score(player_cards)

print(f"Your cards: {player_cards}.\nYour current score is {player_score}")
print(f"The dealers fist card is {dealer_cards[0]}")

player_lost = False
player_passed = False
while not player_lost and not player_passed:
    if player_score == 21:
        player_passed = True
        print("Nice one! You've got 21!")
    else:
        want_card = input("Type \"y\" to get another card or press \"n\" to pass: ")
        if want_card == "y":
            player_cards.append(deal_card())
            player_score = get_score(player_cards)
            print(f"Your cards: {player_cards}.\nYour current score is {player_score}")
            if player_score > 21:
                player_lost = True
        elif want_card == "n":
            player_passed = True

dealer_score = get_score(dealer_cards)
print(f"Dealer cards: {dealer_cards}, score: {dealer_score}")
if not player_lost:
    while dealer_score < player_score and dealer_score <= 16:
        print("Dealer takes a card.")
        time.sleep(1)
        dealer_cards.append(deal_card())
        dealer_score = get_score(dealer_cards)
        print(f"Dealer cards: {dealer_cards}, score: {dealer_score}")

if (not player_lost and player_score > dealer_score) or dealer_score > 21:
    print("You win!")
elif not player_lost and player_score == dealer_score:
    print("It's a draw")
else:
    print("You lose")

