from turtle import *
import random

is_race_on = False

screen = Screen()
screen.setup(height = 400, width = 500)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

y = -100
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x = -230, y = y)
    y += 30
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for one_turtle in all_turtles:
        if one_turtle.xcor() > 225:
            is_race_on = False
            winning_color = one_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        one_turtle.forward(random_distance)

screen.exitonclick()