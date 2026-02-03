# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def highest_bidder(bidding_dict):
    winner = ""
    highest = 0

    for key in bidding_dict:
        their_bids = bidding_dict[key]
        if their_bids > highest:
            highest = their_bids
            winner = key
    
    print(f"The winner is {winner} with bid amount ${highest}")

dict = {}
cont = True

while cont:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    dict[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if choice == "no":
        cont = False
        highest_bidder(dict)

    else:
        cont = True
        print("\n" * 20)