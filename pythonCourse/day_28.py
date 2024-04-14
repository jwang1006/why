import tkinter
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    check.config(text = "✓" *(reps//2))
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    mode.config(text = "Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps+=1
    check.config(text = "✓" *(reps//2))
    if reps%2==1:
        countdown(WORK_MIN, 0)
        mode.config(text = "Timer", fg=GREEN)
    elif reps==8:
        countdown(SHORT_BREAK_MIN, 0)
        mode.config(text = "Break", fg=PINK)
    else:
        countdown(LONG_BREAK_MIN, 0)
        mode.config(text = "Break", fg=PINK)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(minutes, seconds):
    display = f"{minutes}:{seconds}"
    if seconds<10:
        display = f"{minutes}:0{seconds}" 
    canvas.itemconfig(timer_text, text = display)
    if minutes==0 and seconds==0:
        return
    if seconds==0:
        minutes-=1
        seconds=59
    else: 
        seconds-=1
    global timer
    timer = window.after(1000, countdown, minutes, seconds)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



mode = tkinter.Label(text="Timer", font = (FONT_NAME, 45, "normal"))
mode.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
mode.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="pythonCourse/day_28_tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = tkinter.Button(text="Start", background=YELLOW, borderwidth=0, highlightthickness=0, command=start, highlightcolor=YELLOW, border=0)
start.grid(row=2, column=0)

reset = tkinter.Button(text="Reset", background=YELLOW, borderwidth=0, highlightthickness=0, command=reset, highlightcolor=YELLOW, border=0)
reset.grid(row=2, column=2)

check = tkinter.Label(highlightthickness=0, bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)




window.mainloop()