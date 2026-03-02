import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if my_choice >= 0 and my_choice <= 2:
    print(image[my_choice])

print("Computer chose:")
computer_choice = random.randint(0, 2)
print(image[computer_choice])

if my_choice == 0 and computer_choice == 2:
    print("you win")

elif my_choice == 2 and computer_choice == 0:
    print("you lose")

elif my_choice > computer_choice:
    print("you win")

elif my_choice == 2 and computer_choice == 0:
    print("you lose")

elif computer_choice > my_choice:
    print("you lose")

elif my_choice == computer_choice:
    print("draw")

else:
    print("wrong input")