from turtle import *
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    user_guess = screen.textinput(title = f"{len(guessed_state)}/50", prompt = "Input the next state name.").title()

    if user_guess in all_states:
        # to re-loop while loop
        guessed_state.append(user_guess)
        t = Turtle()
        t.penup()
        t.hideturtle()

        put_in_state = data[data.state == user_guess]

        t.goto(put_in_state.x.item(), put_in_state.y.item())
        t.write(user_guess)

screen.exitonclick()