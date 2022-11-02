from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import  Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

pad1 = Paddle(350)
pad2 = Paddle(-350)
ball = Ball()
score = Scoreboard()





screen.listen()
screen.onkeypress(pad1.up,"Up")
screen.onkeypress(pad1.down, "Down")
screen.onkeypress(pad2.up,"w")
screen.onkeypress(pad2.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.movespeed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(pad1) < 50 and ball.xcor() >320 or ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        score.left()
    if ball.xcor() < -380:
        ball.reset()
        score.right()

















screen.exitonclick()