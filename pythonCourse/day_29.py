import tkinter, pandas

FONT_NAME = "Courier"
bg_color = "white"
fg_color = "black"
def generate():
    pass

def addEntry():
    pass


window = tkinter.Tk()
window.config(padx = 50, pady=50, bg = bg_color)

canvas = tkinter.Canvas(width=150, height=204, bg = bg_color, highlightthickness=0)

icon = tkinter.PhotoImage(file="pythonCourse/day_29_icon.png")
canvas.create_image(100, 112, image = icon)
canvas.grid(row=0, column=1)

website = tkinter.Label(text="Website:", width=12, fg=fg_color, bg=bg_color)
website.grid(row=1, column=0)
username = tkinter.Label(text="Email/Username:", width=12, fg=fg_color, bg=bg_color)
username.grid(row=2, column=0)
password = tkinter.Label(text="Password:", width=12, fg=fg_color, bg=bg_color)
password.grid(row=3, column=0)

websiteInput = tkinter.Entry(width=30, fg=fg_color, bg=bg_color, borderwidth=0)
websiteInput.grid(row=1, column=1, columnspan=2)
usernameInput = tkinter.Entry(width=30, fg=fg_color, bg=bg_color, borderwidth=0)
usernameInput.grid(row = 2, column=1, columnspan=2)
passwordInput = tkinter.Entry(width=15, fg=fg_color, bg=bg_color, borderwidth=0)
passwordInput.grid(row=3, column=1)
generatePassword = tkinter.Button(text = "Generate Password", command = generate, width=11, fg=fg_color, bg=bg_color, highlightthickness=0, borderwidth=0)
generatePassword.grid(row=3, column=2)
addButton = tkinter.Button(text="Add", command=addEntry, highlightthickness=0, borderwidth=0, width=27)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()