from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#FFFFFF"
windowbg_color = "#89CFF3"
canvasbg_color = "#89CFF3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("My Promo App")
window.config(padx=100, pady=50,bg=windowbg_color)
bg_image = PhotoImage(file="tomato.png")

title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,28,"bold"),bg=canvasbg_color)
title_label.grid(column=1 , row=0)

canvas = Canvas(width=200, height=224,bg=canvasbg_color,highlightthickness=0)
canvas.create_image(103,112,image=bg_image)
timer_text = canvas.create_text(103,112,text="00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start",bg=canvasbg_color,font=(FONT_NAME,12,"bold"),highlightthickness=0,command=start_timer)

start_button.grid(column=0,row=3)
reset_button = Button(text="reset",bg=canvasbg_color,font=(FONT_NAME,12 ,"bold"),highlightthickness=0,command=timer_reset)
reset_button.grid(column=2, row=3)

 
check_marks =Label(text="✔️",fg=GREEN,font=(FONT_NAME,12,"bold"),bg=canvasbg_color)
check_marks.grid(column=1, row=3)
window.mainloop()