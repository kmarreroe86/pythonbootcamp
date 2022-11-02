import os
from art import logo


# Call for clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


auction_bids_pool = {}


def auction():
    continue_aution = True

    while continue_aution:
        name = input("What is your name?: ")
        bid = input("What is your bid?:$ ")

        auction_bids_pool[name] = float(bid)
        another_user = input(
            "Are there any another bidders? Type 'yes'or 'no'. \n").lower()
        continue_aution = another_user == "yes"
        clear_screen()

    tmp_bidder, tmp_bid = find_highest_bidder()

    print(f"The winner is {tmp_bidder} with a bid of {tmp_bid}")


def find_highest_bidder():
    tmp_bidder = ""
    tmp_bid = -1
    for auction in auction_bids_pool:
        if auction_bids_pool[auction] > tmp_bid:
            tmp_bidder = auction
            tmp_bid = auction_bids_pool[auction]
    return tmp_bidder, tmp_bid


print(logo)
auction()
