from turtle import Turtle

positions = {
    "red": [
        (-385, 230), (-275, 230), (-165, 230), (-55, 230), (55, 230), (165, 230), (275, 230), (385, 230),
        (-385, 200), (-275, 200), (-165, 200), (-55, 200), (55, 200), (165, 200), (275, 200), (385, 200)
    ],
    "orange": [
        (-385, 170), (-275, 170), (-165, 170), (-55, 170), (55, 170), (165, 170), (275, 170), (385, 170),
        (-385, 140), (-275, 140), (-165, 140), (-55, 140), (55, 140), (165, 140), (275, 140), (385, 140)
    ],
    "green": [
        (-385, 110), (-275, 110), (-165, 110), (-55, 110), (55, 110), (165, 110), (275, 110), (385, 110),
        (-385, 80), (-275, 80), (-165, 80), (-55, 80), (55, 80), (165, 80), (275, 80), (385, 80)
    ],
    "yellow": [
        (-385, 50), (-275, 50), (-165, 50), (-55, 50), (55, 50), (165, 50), (275, 50), (385, 50),
        (-385, 20), (-275, 20), (-165, 20), (-55, 20), (55, 20), (165, 20), (275, 20), (385, 20)
    ]
}

class BrickWall:
    def __init__(self):
        self.bricks = []
        self.initialize_bricks()

    def initialize_bricks(self):
        colors = ["red", "orange", "green", "yellow"]
        scores = {
            "red": 7,
            "orange": 5,
            "green": 3,
            "yellow": 1,
        }

        for color in colors:
            for position in positions[color]:
                brick = Turtle()
                brick.shape("square")
                brick.color(color)
                brick.turtlesize(stretch_len=5, stretch_wid=1)
                brick.penup()
                brick.goto(position)
                brick.min_x = position[0] - 70
                brick.max_x = position[0] + 70
                brick.min_y = position[1] - 20
                brick.max_y = position[1] + 20
                brick.value = scores[color]
                self.bricks.append(brick)

