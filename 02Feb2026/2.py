print("Welcome to Treasure Island. Your mission is to find the treasure.")

first_choice = input("left or right? ")

if first_choice == "left":
    second_choice = input("swim or wait? ")
    if second_choice == "wait":
        third_choice = input("which door? red, blue or yellow ")
        if third_choice == "yellow":
            print("you win!")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")