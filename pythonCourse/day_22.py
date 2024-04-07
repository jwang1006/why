import turtle, random

class Paddle:
    def __init__(self, x):
        self.pieces = []
        self.addPiece(x, -20)
        self.addPiece(x, 0)
        self.addPiece(x, 20)

    def addPiece(self, x, y):
        toAdd = turtle.Turtle()
        toAdd.penup()
        toAdd.color("white")
        toAdd.shape("square")
        toAdd.speed(0)
        toAdd.left(90)
        toAdd.setposition(x, y)
        self.pieces.append(toAdd)
    
    def moveUp(self):
        for piece in self.pieces:
            piece.forward(10)
    
    def moveDown(self):
        for piece in self.pieces:
            piece.backward(10)

ball = turtle.Turtle()
ball.penup()
ball.color("white")
ball.shape("circle")

score1 = 0
score2 = 0
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600,  600)
paddle1 = Paddle(-280)
paddle2 = Paddle(280)

screen.delay(10)
screen.listen()
screen.onkeypress(paddle1.moveUp, "w")
screen.onkeypress(paddle1.moveDown, "s")
screen.onkeypress(paddle2.moveUp, "o")
screen.onkeypress(paddle2.moveDown, "k")

def calculateDirection():
    angle = ball.heading()
    print(angle)
    if ball.ycor()>290:
        angle = (ball.heading()-90)*2       
    elif ball.ycor()<-290:
        angle = (ball.heading()-270)*2
    elif ball.xcor()<-290:
        angle = (ball.heading()-180)*2
    elif ball.xcor()>290:
        angle = ball.heading()*2
    else:
        return
    if angle>0:
        ball.right(angle)
    else:
        angle*=-1
        ball.left(angle)
    print(angle)

ball.right(random.randint(0, 360))
while True:
    ball.forward(10)
    calculateDirection()

screen.exitonclick()