import turtle
from states import States

screen = turtle.Screen()
screen.title("My U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = States()

while len(states.correct_answers) < states.total_number:
    answer_state = screen.textinput(title=f"{len(states.correct_answers)}/{states.total_number} Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states.save_the_progress()
        break

    if states.check_state(answer_state):
        states.point_on_the_map(answer_state)

