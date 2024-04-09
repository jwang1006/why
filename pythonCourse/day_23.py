import turtle, random, time
from day_18_stealColors import colors
class CrossyTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__("classic", 1000, False)
        super().hideturtle()
        super().color("black")
        super().penup()
        super().shape("turtle")
        super().sety(-300)
        super().left(90)
        super().showturtle()

    def moveForward(self):
        super().forward(10)
    def resetTurtle(self):
        """Restart the race"""
        super().hideturtle()
        super().sety(-300)
        super().showturtle()
    
class Car(turtle.Turtle):
    def __init__(self, newSpeed):
        self.saveSpeed = newSpeed
        super().__init__("classic", 1000, False)
        super().hideturtle()
        super().penup()
        super().shape("square")
        turtle.colormode(255)
        super().shapesize(stretch_wid=1,stretch_len=5)
        super().color(colors[random.randint(0, len(colors)-1)])
        super().goto(random.randint(-280, 320), random.randint(-260, 280))
        super().right(180)
        super().showturtle()
        super().speed(newSpeed)
    
    def increaseSpeed(self):
        self.saveSpeed +=2
        super().speed(self.saveSpeed)

    def moveCar(self):
        super().forward(10)
        if super().xcor()<-280:
            super().hideturtle()
            super().speed(0)
            super().setx(320)
            super().speed(self.saveSpeed)
            super().showturtle()

    def detectCollision(self):
        return self.vertexCollided(me.xcor()+10, me.ycor()+10) or self.vertexCollided(me.xcor()-10, me.ycor()+10)or self.vertexCollided(me.xcor()-10, me.ycor()-10) or self.vertexCollided(me.xcor()+10, me.ycor()-10)
    
    def vertexCollided(self, x: int, y: int) -> bool:
        return x>super().xcor()-50 and x<super().xcor()+50 and y<super().ycor()+10 and y>super().ycor()-10
    
class Level():
    def __init__(self):
        self.allCars: list[Car] = []
        for n in range(0, 10):
            toAdd = Car(2)
            self.allCars.append(toAdd)
    
    
    def hitByCar(self):
        for car in self.allCars:
            car.moveCar()
            if car.detectCollision():
                return True
        return False

    def runLevel(self):
        while me.ycor()<280:
            if self.hitByCar():
                self.death()

    def death(self):
        turtle.home()
        turtle.tracer(1)
        turtle.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))
        time.sleep(5)
        exit()
           

    def nextLevel(self):
        me.resetTurtle()
        for car in self.allCars:
            car.increaseSpeed()
        self.allCars.append(Car(4))
        self.allCars.append(Car(4))
        
highScore = 0
def updateHighScore():
    with open("pythonCourse/day_24_high_score.txt", mode = "r") as file:
        content = file.read()
        print(content)
        for letter in content:
            if letter.isdigit():
                global highScore
                highScore = int(letter)

screen = turtle.Screen()
tracerSpeed = 2
turtle.colormode(255)
screen.tracer(2)
me = CrossyTurtle()
screen.setup(600, 600)
screen.listen()


def stopListening():
    screen.onkeypress(None, "Up")

def startListening():
    screen.onkeypress(me.moveForward, "Up")

def countdown(round: int):
    stopListening()
    if round-1>highScore:
        with open("pythonCourse/day_24_high_score.txt", mode = "w") as file:
                file.write(f"high score: {round-1}")
    updateHighScore()
    turtle.clear()
    turtle.home()
    turtle.tracer(1)
    writeAndClear("3")
    writeAndClear("2")
    writeAndClear("1")
    writeAndClear("GO!")
    turtle.tracer(tracerSpeed)
    turtle.goto(-250, 250)
    turtle.write(f"Round: {round}", align="left", font=("Courier", 24, "normal"))
    turtle.goto(-250, 230)
    turtle.write(f"High Score: {highScore}", align="left", font=("Courier", 24, "normal"))
    startListening()

def writeAndClear(toWrite: str):
    turtle.write(toWrite, align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    turtle.clear()


turtle.hideturtle()
turtle.penup()
turtle.speed(0)
def main():
    print("main")
    currentLevel = Level()
    round = 1
    while True:
        countdown(round)
        currentLevel.runLevel()
        currentLevel.nextLevel()
        global tracerSpeed
        tracerSpeed+=1
        round+=1

if __name__=="__main__":
    main()