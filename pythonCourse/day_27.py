import tkinter

screen = tkinter.Tk()
screen.title("Miles to Feet")
screen.minsize(300, 300)
screen.config(padx=20, pady=100)

def convert():
    miles = int(numOfMiles.get())
    feet = miles*5260
    converted.config(text=feet)

miles = tkinter.Label(text = "miles")
miles.grid(row=0, column=0)

numOfMiles = tkinter.Entry()
numOfMiles.config(text="Enter here")
numOfMiles.config(width=10)
numOfMiles.grid(row = 0, column = 1)

submit = tkinter.Button()
submit.config(text="Submit", command=convert)
submit.grid(row = 0, column = 2)

equal = tkinter.Label(text="is equal to")
equal.grid(row = 1, column = 0)
converted = tkinter.Label(text = 0)
converted.grid(row = 1, column = 1)
feet = tkinter.Label(text="feet")
feet.grid(row = 1, column = 2)





screen.mainloop()