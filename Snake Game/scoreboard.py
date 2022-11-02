from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.showscore()
    def showscore(self):
        self.clear()
        self.write(f"Score = {self.score}  High-score = {self.high_score}", False, align="center", font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as f:
            f.write(f"{self.high_score}")
        self.score = 0
        self.showscore()

    def update(self):
         self.score += 1
         self.showscore()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER !", False, align="center", font=('Arial', 15, 'normal'))