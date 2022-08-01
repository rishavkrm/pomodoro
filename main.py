from tkinter import *
from constants_list import *


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    # timer_text["text"] = "25:00"
    start_timer()
    check_label["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        countdown(60 * 20)
        timer_label["text"] = "Long Break"
        timer_label["fg"] = RED
        check_label["text"] = "✓✓✓✓"
        print("reps60")
        check_label["text"] += "✓"

    elif reps % 2 == 0:
        countdown(60 * 5)
        timer_label["text"] = "Short break "
        timer_label["fg"] = PINK
        print("reps15")
        check_label["text"] += "✓"

    else:
        countdown(60 * 25)
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
        print("reps30")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = int(count / 60)
    count_sec = int(count) - int(count / 60) * 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


timer_label = Label(text="", font=("courier", 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)

check_label = Label(text="", font=("courier", 40, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=4, column=2)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(90, 130, text="25:00", fill="white", font=("courier", 35, "bold"))

# countdown(25)
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)
canvas.grid(row=2, column=2)

window.mainloop()
