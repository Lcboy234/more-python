from turtle import *
import random
directions = [90, 180, 270, 0]

timmy = Turtle()
timmy.colormode(255)
timmy.pensize(15)
timmy.speed("fastest")

def random_color():
    r = random.randint

for _ in range(200):
    timmy.forward(30)
    timmy.color(random.choice(colours))
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()