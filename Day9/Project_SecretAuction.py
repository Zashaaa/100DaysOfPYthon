# from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program!")

bids = {}


def get_highest_bidder():
    highest_bidder = ""
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bidder = bidder
            highest_bid = bids[bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


more_bidders = True
while more_bidders:
    name_bidder = input("Enter your name: ")
    bid_amount = int(input("Enter your bid: $"))
    bids[name_bidder] = bid_amount
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if other_bidder == "no":
        # clear()
        more_bidders = False
        get_highest_bidder()
    # clear()
