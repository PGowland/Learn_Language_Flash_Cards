from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
remaining_words = {}
try:
    word_bank = pandas.read_csv('data/words_left_to_learn.csv')
    remaining_words = word_bank.to_dict(orient='records')
except FileNotFoundError:
    original_bank = pandas.read_csv('data/italian_words.csv')
    remaining_words = original_bank.to_dict(orient='records')
current_card = {}


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def new_card():
    canvas.itemconfig(card_image, image=card_front_image)
    global current_card
    current_card = random.choice(remaining_words)
    canvas.itemconfig(word, text=current_card["Italian"], fill="black")
    canvas.itemconfig(title, text="Italian", fill="black")
    window.after(3000, flip_card)


def correct():
    remaining_words.remove(current_card)
    new_card()
    df = pandas.DataFrame.from_dict(remaining_words)
    df.to_csv("data/words_left_to_learn.csv", index=False)




window = Tk()
window.title("Lingua Flasha")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400, 100, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=correct, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=new_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)
window.mainloop()
