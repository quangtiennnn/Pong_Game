from turtle import Turtle
STEP_LEN = 10
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.left(90)
    def up(self):
        self.forward(STEP_LEN)
    def down(self):
        self.backward(STEP_LEN)
