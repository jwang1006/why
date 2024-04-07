import turtle, random, time

class Paddle:
    def __init__(self, x):
        self.x: int = x
        self.score: int = 0
        self.direction: str = "none"
        self.paddle = self.createPiece()

    def createPiece(self):
        toAdd = turtle.Turtle()
        toAdd.hideturtle()
        toAdd.penup()
        toAdd.color("white")
        toAdd.shape("square")
        toAdd.shapesize(stretch_wid=1, stretch_len=5)
        toAdd.speed(0)
        toAdd.left(90)
        toAdd.setposition(self.x, -50)
        toAdd.showturtle()
        return toAdd
    
    def getScore(self) -> int:
        return self.score
    
    def scorePoint(self):
        self.score+=1

    def directionUp(self):
        self.direction = "up"

    def directionDown(self):
        self.direction = "down"

    def directionNone(self):
        self.direction = "none"
    
    def movePaddle(self):
        if self.direction=="up":
            self.paddle.sety(self.paddle.ycor()+20)
        elif self.direction=="down":
            self.paddle.sety(self.paddle.ycor()-20)
    
    def hitPaddle(self, y):
        return self.paddle.ycor()+50>y and self.paddle.ycor()-50<y

ball = turtle.Turtle()
ball.penup()
ball.color("white")
ball.shape("circle")
ball.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800,  600)
paddle1 = Paddle(-390)
paddle2 = Paddle(380)

screen.listen()
screen.onkeypress(paddle1.directionUp, "w")
screen.onkeypress(paddle1.directionDown, "s")
screen.onkeypress(paddle2.directionUp, "Up")
screen.onkeypress(paddle2.directionDown, "Down")
screen.onkeyrelease(paddle1.directionNone, "w")
screen.onkeyrelease(paddle1.directionNone, "s")
screen.onkeyrelease(paddle2.directionNone, "Up")
screen.onkeyrelease(paddle2.directionNone, "Down")
turtle.penup()
turtle.hideturtle()
turtle.sety(260)
turtle.color("white")

def startRound():
    turtle.clear()
    turtle.write(f"{paddle1.getScore(), paddle2.getScore()}", align="center", font=("Arial", 25, "normal"))
    ball.hideturtle()
    ball.home()
    ball.showturtle()
    direction = random.randint(0, 3)
    if direction==0:
        ball.right(random.randint(0, 45))
    elif direction==1:
        ball.left(random.randint(0, 45))
    elif direction==2:
        ball.right(random.randint(135, 180))
    elif direction==3:
        ball.left(random.randint(135, 180))


def calculateDirection():
    if ball.ycor()>290:
        angle = (ball.heading()-180)*2
    elif ball.ycor()<-290:
        angle = ball.heading()*2
    elif ball.xcor()<-380:
        if paddle1.hitPaddle(ball.ycor()):
            angle = (ball.heading()-90)*2
        else:
            paddle2.scorePoint()
            startRound()
            return
    elif ball.xcor()>380:
        if paddle2.hitPaddle(ball.ycor()):
            angle = (ball.heading()-270)*2
        else:
            paddle1.scorePoint()
            startRound()
            return
    else:
        return
    if angle>0:
        ball.right(angle)
    else:
        angle*=-1
        ball.left(angle)

def gameloop():
    startRound()
    while True:
        ball.forward(10)
        paddle1.movePaddle()
        paddle2.movePaddle()
        calculateDirection()
        screen.update()
        time.sleep(0.02)

gameloop()