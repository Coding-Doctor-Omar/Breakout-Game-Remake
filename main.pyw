from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from bricks import BrickWall
from ball import Ball
from tkinter import PhotoImage
import time

FPS = 120

screen = Screen()
root = screen._root

icon = PhotoImage(file="images/Breakout.png")
root.iconphoto(False, icon)

root.resizable(False, False)
screen.title("Breakout")
screen.setup(900, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

paddle = Paddle()
score_board = ScoreBoard()
brick_wall = BrickWall()
ball = Ball()

def move_right():
    if not score_board.is_game_over and score_board.game_is_on:
        paddle.move_right()

def move_left():
        if not score_board.is_game_over and score_board.game_is_on:
            paddle.move_left()

def space_pressed():
    if score_board.is_game_over:
        paddle.reset_position()
        brick_wall.initialize_bricks()
        ball.reset_position()
        ball.playing = True
        score_board.reset_game()
    elif not score_board.game_is_on:
        score_board.game_is_on = True
        ball.playing = True
        score_board.reset_game()



screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="A", fun=move_left)
screen.onkeypress(key="Left", fun=move_left)

screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="D", fun=move_right)
screen.onkeypress(key="Right", fun=move_right)

screen.onkey(key="space", fun=space_pressed)


while True:
    time.sleep(1 / FPS)

    if ball.ycor() < paddle.ycor():
        score_board.deduct_life()

        if score_board.lives < 1:
            ball.playing = False

        ball.reset_position()

    if not brick_wall.bricks and score_board.is_game_over == False:
        score_board.is_game_over = True
        ball.playing = False
        score_board.display_game_over(status="win")


    if score_board.game_is_on and not score_board.is_game_over:
        ball.move()

    # Ball Side Wall Bounce Handling
    if ball.xcor() >= 430 or ball.xcor() <= -430:
        ball.bounce_from_wall()

    # Ball Ceiling Bounce Handling
    if ball.ycor() >= 280:
        ball.bounce_from_brick()

    # Ball Paddle Bounce Handling
    if paddle.ycor() <= ball.ycor() <= paddle.zone()["max_y"]:
        # Steep Left Bounce
        if paddle.zone()["min_x"] <= ball.xcor() < paddle.zone()["quartile_x_1"]:
            ball.bounce_steep_from_paddle_left()

        # Shallow Left Bounce
        if paddle.zone()["quartile_x_1"] <= ball.xcor() < paddle.xcor():
            ball.bounce_shallow_from_paddle_left()

        # Shallow Right Bounce
        if paddle.xcor() <= ball.xcor() < paddle.zone()["quartile_x_3"]:
            ball.bounce_shallow_from_paddle_right()

        # Steep Right Bounce
        if paddle.zone()["quartile_x_3"] <= ball.xcor() <= paddle.zone()["max_x"]:
            ball.bounce_steep_from_paddle_right()



    bricks_hit = []
    for brick in brick_wall.bricks:
        if brick.min_x <= ball.xcor() <= brick.max_x and brick.min_y <= ball.ycor() <= brick.max_y:
            score_board.increase_score(brick.value)
            bricks_hit.append(brick)

    if bricks_hit:
        for brick in bricks_hit:
            brick.hideturtle()
            brick_wall.bricks.remove(brick)

        ball.bounce_from_brick()

    screen.update()
