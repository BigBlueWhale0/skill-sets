from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_NAME = "Courier"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.canvas = Canvas(width=300, height=250, bg="white",highlightthickness=0, highlightbackground=THEME_COLOR)
        self.quote_text = self.canvas.create_text(150,125,text="Text", width=280, font=(FONT_NAME, 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(column=0, row=2)

        self.score_label = Label(text=f"Score: {self.score}", font=(FONT_NAME, 15), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)