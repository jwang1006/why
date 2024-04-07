import turtle, random

direction = "right"

score = -1
apple = turtle.Turtle()
apple.hideturtle()
apple.color("red")
apple.penup()
apple.speed(0)
apple.shape("circle")


screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()



def newApple():
    global score
    score+=1
    turtle.clear()
    turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    apple.hideturtle()
    apple.goto(random.randint(-280, 280)//20*20, random.randint(-280, 280)//20*20)
    apple.showturtle()
    

def up():
    global direction
    if direction!="down":
        direction = "up"
    
def down():
    global direction
    if direction!="up":
        direction = "down"

def right():
    global direction
    if direction!="left":
        direction = "right"

def left():
    global direction
    if direction!="right":
        direction = "left"

def deathCheck():
    if snakeBody[0].xcor()>280 or snakeBody[0].xcor()<-280 or snakeBody[0].ycor()>280 or snakeBody[0].ycor()<-280:
        turtle.goto(0, 0)
        turtle.write(f"Game over!", align="center", font=("Courier", 24, "normal"))
        return True
    closestDistance = 1000
    for index in range(1, len(snakeBody)):
        if abs(snakeBody[0].xcor()-snakeBody[index].xcor())<1 and abs(snakeBody[0].ycor()-snakeBody[index].ycor())<1:
            print("self destruction!")
            turtle.write(f"Game over!", align="center", font=("Courier", 24, "normal"))
            return True

def addHead():
    newX = snakeBody[0].xcor()
    newY = snakeBody[0].ycor()
    if direction=="up":
        newY+=20
    elif direction == "down":
        newY-=20
    elif direction == "left":
        newX+=20
    else:
        newX-=20
    newTurtle = turtle.Turtle()
    newTurtle.shape("square")
    newTurtle.hideturtle()
    newTurtle.penup()
    newTurtle.color("green")
    newTurtle.speed(0)
    
    newTurtle.goto(newX, newY)
    newTurtle.showturtle()
    snakeBody.insert(0, newTurtle)
    if not isEatingApple(newX, newY):
        lastTurtle = snakeBody.pop()
        lastTurtle.hideturtle()
    

def isEatingApple(x, y):
    if abs(apple.xcor()-x)<1 and abs(apple.ycor()-y)<1:
        newApple()
        print("apple eaten")
        return True
    return False


snakeBody = []
for i in range(0, 3):
    toAdd = turtle.Turtle()
    toAdd.penup()
    toAdd.color("green")
    toAdd.setx(i*20)
    toAdd.shape("square")
    snakeBody.append(toAdd)

screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(right, "a")
screen.onkey(left, "d")

newApple()
screen.delay(10)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 250)
turtle.color("white")
turtle.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
while True:
    addHead()
    if deathCheck():
        break


screen.exitonclick()