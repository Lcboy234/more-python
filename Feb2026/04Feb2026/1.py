import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(anything):
    if len(anything) == 2 and sum(anything) == 21:
        return 0
    
    if 11 in anything and sum(anything) > 21:
        anything.remove(11)
        anything.append(1)

    return sum(anything)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "You lose, computer has Blackjack."
    elif user_score == 0:
        return "You have Blackjack, win."
    elif user_score > 21:
        return "Went over, you lose."
    elif computer_score > 21:
        return "Computer lose by going over."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose"

def play():
    print(art.logo)
    user_cards = []
    computer_cards = []
    u_score = -1
    c_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        u_score = calculate_score(user_cards)
        c_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {u_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if u_score == 0 or c_score == 0 or u_score > 21:
            game_over = True

        else:
            more_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if more_card == "y":
                user_cards.append(deal_card())

            else:
                game_over = True

    while c_score != 0 and c_score < 17:
        computer_cards.append(deal_card())
        c_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {u_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {c_score}")
    print(compare(u_score, c_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play()