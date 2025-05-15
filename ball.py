from turtle import Turtle
import sound

MOVE_SPEED = 4

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.playing = False
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.reset_position()

    def move(self):
        self.forward(MOVE_SPEED)

    def bounce_from_brick(self):
        self.setheading(-1 * self.heading() + 360)
        if self.playing:
            sound.play_bounce_sound()

    def bounce_from_wall(self):
        self.setheading(180 - self.heading())
        if self.playing:
            sound.play_bounce_sound()

    def bounce_steep_from_paddle_right(self):
        self.setheading(30)
        if self.playing:
            sound.play_bounce_sound()

    def bounce_steep_from_paddle_left(self):
        self.setheading(150)
        if self.playing:
            sound.play_bounce_sound()

    def bounce_shallow_from_paddle_right(self):
        self.setheading(60)
        if self.playing:
            sound.play_bounce_sound()

    def bounce_shallow_from_paddle_left(self):
        self.setheading(120)
        if self.playing:
            sound.play_bounce_sound()

    def reset_position(self):
        self.teleport(0, -253)
        self.setheading(60)
