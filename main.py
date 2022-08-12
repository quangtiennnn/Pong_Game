import turtle as t
from paddle import Paddle
from ball import Ball
import time
"""SCREEN"""
screen = t.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((350,0))
r_paddle = Paddle((-350,0))

screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"d")

ball = Ball()
ball.setheading(0)
screen.update()
game_is_on = True
while game_is_on:
    ball.move()
    if ball.wall_collision():
        ball.bounce_y()
    elif ball.paddle_collision(l_paddle) or ball.paddle_collision(r_paddle):
        ball.bounce_x()
    time.sleep(0.1)
    screen.update()




screen.exitonclick()