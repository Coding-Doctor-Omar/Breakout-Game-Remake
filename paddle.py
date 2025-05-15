from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.reset_position()

    def move_right(self):
        if self.xcor() <= 385:
            self.fd(MOVE_DISTANCE)

    def move_left(self):
        if -385 <= self.xcor():
            self.bk(MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(0, -275)

    def zone(self):
        min_x = self.xcor() - 72
        max_x = self.xcor() + 72
        quartile_x_1 = (min_x + self.xcor()) / 2
        quartile_x_3 = (self.xcor() + max_x) / 2

        max_y = self.ycor() + 22

        return {
            "min_x": min_x,
            "max_x": max_x,
            "quartile_x_1": quartile_x_1,
            "quartile_x_3": quartile_x_3,
            "max_y": max_y,
        }

