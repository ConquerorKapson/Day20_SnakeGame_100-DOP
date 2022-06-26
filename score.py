from turtle import Turtle

FONT = "Courier"
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write_score()
        self.hideturtle()

    def update(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        with open("data.txt") as file:
            val = file.read()
            self.write(f"Score: {self.score}     Highscore: {val}", align=ALIGNMENT, font=(FONT, 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        # self.write(f"Game Over", align=ALIGNMENT, font=(FONT, 24, "normal"))

    def reset(self):
        with open("data.txt") as file:
            val = file.read()
            if self.score > int(val):
                self.highscore = self.score
                with open("data.txt", "w") as file:
                    file.write(str(self.highscore))
        self.score = -1
        self.update()
