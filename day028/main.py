import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_working = ""
# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    window.after_cancel(timer_working)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        timer.config(text="Break" , font=(FONT_NAME, 35, "bold"), fg=RED , bg=YELLOW)
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer.config(text="Work", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_working
        timer_working = window.after(1000, count_down, count-1)

    else:
        start_timer()
        marks= ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks ="✔"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# ---------------------------- LABELS ------------------------------- #
timer = Label(text="Timer" , font=(FONT_NAME, 35, "bold"), fg=GREEN , bg=YELLOW)
timer.grid(column=1, row=0)
# ---------------------------- TOMATO ------------------------------- #
canvas = Canvas(width=200 ,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

# ---------------------------- BUTTON ------------------------------- #
start = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=time_reset)
reset.grid(column=2, row=2)

# ---------------------------- CHECKMARK ------------------------------- #
checkmark = Label(font=(FONT_NAME,25, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)
window.mainloop()