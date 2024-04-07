# turtle race
from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.bgcolor("black")
allTurtles = {
    "red": Turtle(),
    "orange": Turtle(),
    "yellow": Turtle(),
    "green": Turtle(),
    "blue": Turtle(),
    "purple": Turtle()
}
num = 0
for colors in allTurtles:
    allTurtles[colors].penup()
    allTurtles[colors].shape("turtle")
    allTurtles[colors].color(colors)
    allTurtles[colors].sety(num)
    num+=20


finishLine = 550

def takeStep(turty):
    step = random.randint(0, 1)
    if step==1:
        turty.forward(15)

fighter = turtle.textinput("CHOOSE YOUR FIGHTER!", "Enter a color: ")

noVictor = True
while noVictor:
    for color in allTurtles:
        takeStep(allTurtles[color])
        if allTurtles[color].xcor()>finishLine:
            if color == fighter:
                print("Congratulations! You bet on the winning turtle!")
            else:
                print(f"Sorry, the winner was {color}")
            noVictor = False
            break
screen.exitonclick()
