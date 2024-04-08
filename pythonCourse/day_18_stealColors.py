import random, turtle
import colorgram
colors = colorgram.extract('pythonCourse/day_18_wwx.jpg', 10)
for index in range(0, len(colors)):
    colors[index]=(colors[index].rgb.r, colors[index].rgb.g, colors[index].rgb.b)
    print(colors[index])

def randomDots(bob):
    for rowNum in range(0, 9):
        drawRow(bob)
        bob.penup()
        bob.setx(-300)
        bob.sety(bob.ycor()+90)
        bob.pendown()
    

def drawRow(bob):
    for dotNum in range(0, 9):
        bob.color(colors[random.randint(0, len(colors)-1)])
        bob.begin_fill()
        bob.circle(20)
        bob.end_fill()
        bob.penup()
        bob.setx(bob.xcor()+90)
        bob.pendown()




if __name__=="__main__":
    bob = turtle.Turtle()
    bob.speed(0)
    bob.penup()
    bob.setposition(-300, -300)
    bob.pendown()
    turtle.colormode(255)
    turtle.screensize(600, 600)
    randomDots(bob)