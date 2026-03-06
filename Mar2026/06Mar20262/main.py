import turtle
from turtle import *
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

state_list = data.state.to_list()

guessed_states = []

while len(guessed_states) <= 50:

    user_guess = screen.textinput(title = f"{len(guessed_states)}/ 50 States Correct", 
                                  prompt = "Guess another state.").title()

    if user_guess in state_list:

        guessed_states.append(user_guess)

        pointer = Turtle()
        pointer.hideturtle()
        pointer.penup()

        getting_state_data = data[data.state == user_guess]

        pointer.goto(getting_state_data.x.item(), getting_state_data.y.item())

        pointer.write(user_guess)

screen.exitonclick()