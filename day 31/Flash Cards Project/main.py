from tkinter import *
import pandas as pd
import random
#-----------------Setting up data---------------#
file = r"data\french_words.csv"
file2 = r"data\words_to_learn.csv"

try:
    data = pd.read_csv(file2)
except FileNotFoundError:
    data = pd.read_csv(file)
    
# list = {row['French'] : row['English'] for index, row in data.iterrows()}
to_learn = data.to_dict(orient="records")
current_card = {}
flip_timer = None
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    print(len(data))
    next_card()










#--------------------------UI--------------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images\card_front.png")
card_back_img = PhotoImage(file="images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img, )
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_img = PhotoImage(file=r"images\right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()







mainloop()