from turtle import Turtle
from random import randint

add_x = 10
add_y = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.penup()

    def move(self):
        new_xcor = self.xcor() + add_x
        new_ycor = self.ycor() + add_y
        self.goto(new_xcor,new_ycor)
    def wall_collision(self):
        if self.ycor() > 350 or self.ycor() < -350:
            return True
        return False
    def paddle_collision(self,paddle):
        if(self.distance(paddle) < 50):
            return True
        return False
    def bounce_y(self):
        global add_y
        add_y = -add_y
    def bounce_x(self):
        global add_x
        add_x = -add_x