from tkinter import *
import pandas
import random

#data read
data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")
chosen_card = {}
def next_card():
    current_card = random.choice(data_dict)
    global chosen_card
    chosen_card = current_card
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_body,text=current_card["French"])
    print(current_card["French"])

def card_flip():

    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_body, text=chosen_card["English"])
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

# GUI
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800 ,  height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel",40,"italic"))
canvas_body = canvas.create_text(400,256,text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=card_flip)
known_button.grid(row=1,column=1)

window.mainloop()
