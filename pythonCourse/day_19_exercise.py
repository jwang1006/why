from turtle import Turtle, Screen



bob = Turtle()
screen = Screen()

def forward():
    bob.forward(15)

def back():
    bob.backward(15)

def turnleft():
    bob.left(15)

def turnright():
    bob.right(15)
    
def clear():
    bob.home()
    bob.clear()
screen.listen()
screen.onkey(forward, key="w")
screen.onkey(back, key="s")
screen.onkey(turnleft, key="a")
screen.onkey(turnright, key="d")
screen.onkey(clear, "c")
screen.exitonclick()