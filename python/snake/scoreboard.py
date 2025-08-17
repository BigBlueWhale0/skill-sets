from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.num_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def add_score(self):
        self.num_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.num_score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.num_score > self.high_score:
            with open("data.txt",mode="w") as file:
                file.write(str(self.num_score))
            self.high_score = self.num_score
        self.num_score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.hideturtle()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
