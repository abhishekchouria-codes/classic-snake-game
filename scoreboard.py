from turtle import Turtle

FONT = ("Arial", 13, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font=FONT, align=ALIGN)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as highest_score:
                highest_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=FONT, align=ALIGN)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
