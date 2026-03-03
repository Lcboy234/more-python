from turtle import *
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which color are you choosing? Pick your color: ")
colors = ["red", "blue", "green", "purple", "black", "brown"]
distances = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for index in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.speed("fast")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=distances[index])
    all_turtles.append(tim)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for one_turtle in all_turtles:
        if one_turtle.xcor() > 225:
            is_race_on = False
            winning_color = one_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} color reached the end first.")
            else:
                print(f"You've lose! The {winning_color} color reached the end first.")
                
        distance = random.randint(0, 10)
        one_turtle.forward(distance)

screen.exitonclick()