import random
from art import logo, vs
from game_data import data

# Format the account data into printable format
def format(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(ur_input, a_followers, b_followers):
    if a_followers > b_followers:
        # if ur_input == 'A':
            # return True
        # return False
        return ur_input == 'A'
    
    else:
        return ur_input == 'B'

# Display art
print(logo)
score = 0
game_continue = True
second = random.choice(data)

while game_continue:
    # Generate a random account from the game data

    # Making account at position B become the next account at position A

    first = second
    second = random.choice(data)
    if first == second:
        second = random.choice(data)

    print(f"Compare A: {format(first)}")
    print(vs)
    print(f"Against B: {format(second)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ")

    # Screen clearing
    print("\n" * 20)
    print(logo)

    # Check if user is correct.
    # - Get follower count for each account
    # - Use if statement to check if user is correct
    first_count = first['follower_count']
    second_count = second['follower_count']

    is_correct = check_answer(guess, first_count, second_count)

    # Give user feedback based on their guess
    if is_correct:
        # score keeping
        score += 1
        print(f"Correct. Current score: {score}")
    else:
        print(f"Wrong. Final score: {score}")
        game_continue = False

    # Make the game repeatable

    # Making account at position B become the next account at position A