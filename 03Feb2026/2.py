import art
print(art.logo)

def find_highest(bidding_dict):
    winner = ""
    highest = 0

    for key in bidding_dict:
        bid_amount = bidding_dict[key]
        if bid_amount > highest:
            highest = bid_amount
            winner = key

    print(f"Winner is {winner} with bid amount ${bid_amount}.")

dict = {}
continue_bid = True

while continue_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    dict[name] = bid
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more_bidder == "no":
        continue_bid = False
        find_highest(dict)
    else:
        print("\n" * 20)