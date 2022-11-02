from turtle import Turtle,Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.parts = []
        for segments in self.starting_positions:
            self.add(segments)

        self.distance = 20
        self.head = self.parts[0]

    def add(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.parts.append(segment)
    def extend(self):
        self.add(self.parts[-1].position())

    def reset(self):
        for seg in self.parts:
            seg.goto(1000,1000)
        self.parts.clear()
        for segments in self.starting_positions:
            self.add(segments)
        self.head = self.parts[0]

    def move(self):
         for seg_num in range(len(self.parts) - 1, 0, -1):
             xcor = self.parts[seg_num - 1].xcor()
             ycor = self.parts[seg_num - 1].ycor()
             self.parts[seg_num].goto(xcor, ycor)
         self.parts[0].forward(self.distance)
    def up(self):
       if self.head.heading() != DOWN:
         self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)