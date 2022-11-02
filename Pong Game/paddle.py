from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(pos, 0)
        self.shapesize(stretch_len=5)
    def up(self):
        self.forward(20)
    def down(self):
        self.back(20)