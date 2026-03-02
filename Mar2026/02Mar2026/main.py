from turtle import *

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

def draw_shape(num_sides):

    angle = 360/ num_sides
    
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for _ in range(3, 11):
    draw_shape(_)

screen = Screen()
screen.exitonclick()