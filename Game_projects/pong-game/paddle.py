from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        y_coordinate = self.ycor()
        y_coordinate += 20
        self.goto(self.xcor(), y_coordinate)

    def down(self):
        y_coordinate = self.ycor()
        y_coordinate -= 20
        self.goto(self.xcor(), y_coordinate)