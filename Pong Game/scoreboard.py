from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.p1 = 0
        self.p2 = 0
        self.color("white")
        self.hideturtle()

        self.score()


    def score(self):
        self.goto(0, 250)
        self.write(f"{self.p1} | {self.p2} ", True, align="center", font=('Arial', 30, 'normal'))


    def left(self):
        self.p1 += 1
        self.clear()
        self.score()

    def right(self):
        self.p2 += 1
        self.clear()
        self.score()