import pandas
from turtle import Turtle
FONT = ("Courier", 15, "normal")

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.correct_answers = []
        self.total_number = len(self.data.state)

    def check_state(self, guess):
        return not self.data[self.data.state == guess].empty

    def point_on_the_map(self, guess):
        xcor = self.data[self.data.state == guess].x.item()
        ycor = self.data[self.data.state == guess].y.item()
        if guess not in self.correct_answers:
            self.correct_answers.append(guess)
            self.map_state(guess,xcor,ycor)

    def map_state(self,name,xcor,ycor):
        self.hideturtle()
        self.penup()
        self.goto(xcor, ycor)
        self.write(name, align="center", font=FONT)

    def save_the_progress(self):
        missed_states = [state for state in self.data.state.to_list() if state not in self.correct_answers]
        data = {"missed": missed_states}
        data = pandas.DataFrame(data)
        data.to_csv("missed_states.csv")




