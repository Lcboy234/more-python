print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
tippy = tip / 100
final = (total + (total * tippy))/ split
print(f"Each person should pay: ${final}")