import random
import art1

EASY_TURNS = 10
HARD_TURNS = 5

def check(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    
    else:
        print("Correct guess.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS
    
    else:
        return HARD_TURNS


def play():
    
    print(art1.logo)

    # dead code stay the same
    print("Welcome to the Number Gussing Game!")
    print("I'm thinking of a number between 1 and 100")

    # dead code stay the same
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0

    # make another guess needs to be reprinted so add a while loop
    while guess != answer:
        print(f"You have {turns} attempts to make a guess.")

        guess = int(input("Make a guess: "))

        turns = check(guess, answer, turns)

        if turns == 0:
            print("You lose.")
            return
        
play()