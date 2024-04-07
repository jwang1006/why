from turtle import Turtle, Screen
import random, turtle

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "SlateGray", "SeaGreen"]

def drawSquare():
    for sides in range(0, 4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

def drawLine(length):
    for n in range(0, length):
        timmy_the_turtle.forward(5)
        timmy_the_turtle.teleport(timmy_the_turtle.xcor()+5, 0)

def drawShape(numOfSides):
    angleIncrement = 360/numOfSides
    while numOfSides>0:
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angleIncrement)
        numOfSides-=1

def drawShapesThrough10():
    for sideNum in range(3, 11):
        timmy_the_turtle.color(colors[random.randint(0, len(colors)-1)])
        drawShape(sideNum)
        
def randomColorTuple():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def spirograph(angleIncrement):
    timmy_the_turtle.speed(0)
    for angle in range(0, 360//angleIncrement):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.left(angleIncrement)
        timmy_the_turtle.color(randomColorTuple())

def randomWalk():
    timmy_the_turtle.speed(10)
    timmy_the_turtle.width(10)
    while True:
        num = random.randint(0, 3)
        timmy_the_turtle.forward(30)
        timmy_the_turtle.right(num*90)
        timmy_the_turtle.color(randomColorTuple())

timmy_the_turtle = Turtle()
turtle.colormode(255)
timmy_the_turtle.shape("turtle")
drawLine(100)





