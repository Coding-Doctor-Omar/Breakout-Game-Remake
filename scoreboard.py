from turtle import Turtle
import sound


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_is_on = False
        self.reset_game()

    def deduct_life(self):
        if self.lives > 1:
            self.lives -= 1
            self.refresh_stats()
            sound.play_life_deduction_sound()
        else:
            self.lives -= 1
            self.refresh_stats()
            self.is_game_over = True
            self.display_game_over(status="lose")

    def increase_score(self, brick_value: int):
        self.score += brick_value
        self.refresh_stats()

        if self.score > self.highscore:
            self.highscore = self.score
            self.refresh_stats()

            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))


    def refresh_stats(self):
        self.clear()
        self.color("white")
        self.teleport(-340, 270)
        self.write(
            arg=f"Score: {self.score}",
            align="center",
            font=("Courier", 16, "normal")
        )

        self.teleport(0, 270)
        self.write(
            arg=f"High Score: {self.highscore}",
            align="center",
            font=("Courier", 16, "normal")
        )

        self.teleport(330, 270)
        self.write(
            arg=f"Lives: {self.lives}",
            align="center",
            font=("Courier", 16, "normal")
        )

    def display_game_over(self, status):
        self.teleport(0, -50)
        self.color("red")
        if status == "lose":
            self.write(
                arg=f"GAME OVER\nPress SPACE to play again.",
                align="center",
                font=("Courier", 16, "bold")
            )

            sound.play_lose_game_sound()

        elif status == "win":
            self.win = True
            self.color("green")
            self.write(
                arg=f"You WIN!\nPress SPACE to play again.",
                align="center",
                font=("Courier", 16, "bold")
            )

            sound.play_win_game_sound()

    def reset_game(self):
        self.clear()
        self.win = False
        self.is_game_over = False
        self.score = 0

        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read().strip())

        self.lives = 3
        self.hideturtle()
        self.color("white")

        self.refresh_stats()

        if not self.game_is_on:
            self.teleport(0, -50)
            self.write(
                arg=f"Press SPACE to begin.",
                align="center",
                font=("Courier", 16, "normal")
            )


