from tkinter import *
import pandas
from random import choice
import time
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_to_learn = data.to_dict(orient="records")
    data.to_csv("data/words_to_learn.csv", index=False)
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_to_learn)
    canvas.itemconfig(card_title, text="French",fill='black')
    canvas.itemconfig(card_word, text=current_card['French'],fill='black')
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def right_word():
    data_to_learn.remove(current_card)
    data = pandas.DataFrame(data_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_image, image=card_back_image)

window = Tk()
window.title("My Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800,height=526)
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400,150,text="Title", font=(FONT_NAME, 40, "italic"),fill='black')
card_word = canvas.create_text(400,263,text="word", font=(FONT_NAME, 60, "bold"),fill='black')
canvas.config(highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=right_word)
right_button.grid(column=1,row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=next_card)
wrong_button.grid(column=0,row=1)

next_card()

window.mainloop()