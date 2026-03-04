from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Welcome to Pong")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330 or ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    # detect if right side missed
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    
    # detect if left side missed
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()