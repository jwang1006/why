import turtle, math, time

# ------------------ CONSTANTS -------------------
width = 1000
height = 1000
incrementBetweenLines = 30
function_pensize=2
relationionship_pensize = 3
normalSpeed = 10
fastSpeed = 500

# ----------------- EQUATION CONSTANTS--------

westDistance = 4
distanceBetweenRoads = 2
distanceToFountain = 0.25
quadraticCoefficent = 1.0/4/distanceToFountain
superTickToTick = 1000
speed = 20 # units/superticks
speedInScreenUnitsPerTick = speed/superTickToTick*incrementBetweenLines
ticks = 0
superticks = ticks/superTickToTick


# ---------- CHANGING VARIABLES --------
normalSlope = 0
policeAndClientSlope = 0
global newtonsExpectedDistance
global binaryExpectedDistance

# ---------------- line drawers --------------

height_drawer = turtle.Turtle()
height_drawer.hideturtle()
height_drawer.color("blue")
height_drawer.pensize(relationionship_pensize)


west_distance_drawer = turtle.Turtle()
west_distance_drawer.hideturtle()
west_distance_drawer.color("blue")
west_distance_drawer.pensize(relationionship_pensize)

client_to_police_drawer = turtle.Turtle()
client_to_police_drawer.hideturtle()
client_to_police_drawer.color("green")
client_to_police_drawer.pensize(relationionship_pensize)

police_normal_drawer = turtle.Turtle()
police_normal_drawer.hideturtle()
police_normal_drawer.color("red")
police_normal_drawer.pensize(relationionship_pensize)

info_drawer = turtle.Turtle()
info_drawer.hideturtle()
info_drawer.penup()
info_drawer.color("black")
info_drawer.goto(50, 50)


# --------- set up -------------------
screen = turtle.Screen()
screen.setup(width, height)
screen.bgcolor("white")
screen.tracer(fastSpeed)
client = turtle.Turtle()
client.color("green")
client.shape("turtle")
client.penup()
client.goto(westDistance*incrementBetweenLines, -distanceBetweenRoads*incrementBetweenLines)
police = turtle.Turtle()
police.color("blue")
police.shape("turtle")
screen.tracer(normalSpeed)

def newtons_method(numIter) -> float:
    """Returns the distanceTraveled when light turns off"""
    return newtons_method_helper(0, numIter)

# 2a^2x^3+2ahx-d
def newtons_method_helper(lastX, numIter) -> float:
    if numIter==0:
        return lastX
    nextX = lastX - y_value(lastX)/newtons_method_derivative_helper(lastX)
    return newtons_method_helper(nextX, numIter-1)

def y_value(x):
    return 2*(quadraticCoefficent**2)*(x**3)+2*quadraticCoefficent*distanceBetweenRoads*x-westDistance

# 6a^2x^2+2ah
def newtons_method_derivative_helper(x) -> float:
    return 6*(quadraticCoefficent**2)*(x**2)+ 2*quadraticCoefficent*distanceBetweenRoads


def bruteForce():
    # 2a^2x^3+2ahx-d
    p1 = 0
    p2 = 20
    while True:
        x = (p2+p1)/2
        y = y_value(x)
        print(y)
        if abs(y)<0.001:
            return x
        elif y>0:
            p2 = x
        else:
            p1 = x


def graphLines() -> None:
    bob = turtle.Turtle()
    bob.penup()
    bob.color("black")
    bob.speed(0)
    bob.pensize(2)
    bob.goto(0, -height//2)        
    bob.pendown()
    bob.goto(0, height//2)
    bob.penup()
    bob.goto(-width//2, 0)
    bob.pendown()
    bob.goto(width//2, 0)
    bob.penup()
    bob.pensize(1)

    for x in range(incrementBetweenLines, width//2, incrementBetweenLines):
        bob.goto(x, -height//2)        
        bob.pendown()
        bob.goto(x, 0)
        bob.write(f"{x//incrementBetweenLines}", align="center", font=("Courier", 20, "normal"))
        bob.goto(x, height//2)
        bob.penup()
        bob.goto(-x, -height//2)        
        bob.pendown()
        bob.goto(-x, 0)
        bob.write(f"{-x//incrementBetweenLines}", align="center", font=("Courier", 20, "normal"))
        bob.goto(-x, height//2)
        bob.penup()

    for y in range(incrementBetweenLines, height//2, incrementBetweenLines):
        bob.goto(-width//2, y)
        bob.pendown()
        bob.goto(0, y)
        bob.write(f"{y//incrementBetweenLines}", align="center", font=("Courier", 20, "normal"))
        bob.goto(width//2, y)
        bob.penup()
        bob.goto(-width//2, -y)
        bob.pendown()
        bob.goto(0, -y)
        bob.write(f"{-y//incrementBetweenLines}", align="center", font=("Courier", 20, "normal"))
        bob.goto(width//2, -y)
        bob.penup()

    
def graphSouthRoad() -> None:
    bob = turtle.Turtle()
    bob.penup()
    bob.color("red")
    bob.speed(0)
    bob.pensize(2)
    bob.goto(-width//2, -distanceBetweenRoads*incrementBetweenLines)
    bob.pendown()
    bob.goto(width//2, -distanceBetweenRoads*incrementBetweenLines)

def graphQuadratic(functionColor = "red") -> None:
    bob = turtle.Turtle()
    bob.penup()
    bob.speed(0)
    bob.pensize(2)
    bob.color(functionColor)
    for scaleX in range(-width//2, width//2):
        unitX = scaleX/incrementBetweenLines
        unitY = (unitX**2)*quadraticCoefficent
        if unitY*incrementBetweenLines<height//2:
            bob.goto(int(unitX*incrementBetweenLines), int(unitY*incrementBetweenLines))
            bob.pendown()

def chase():
    client.forward(speedInScreenUnitsPerTick)
    policeX = client.xcor()-westDistance*incrementBetweenLines
    police.goto(policeX, int(incrementBetweenLines*(policeX/incrementBetweenLines)**2*quadraticCoefficent))
    screen.tracer(fastSpeed)
    recalculateValues()
    if abs(policeAndClientSlope-normalSlope)<0.05 or ticks%2==0:
        drawWestDistance()
        drawHeight()
        drawLineClientToPolice()
        drawPoliceNormalLine()
        updateInformation()
    screen.tracer(normalSpeed)

def drawLineClientToPolice():
    client_to_police_drawer.penup()
    client_to_police_drawer.clear()
    client_to_police_drawer.goto(police.xcor(), police.ycor())
    client_to_police_drawer.pendown()
    client_to_police_drawer.goto(client.xcor(), client.ycor())
    

def recalculateValues():
    global policeAndClientSlope
    policeAndClientSlope = (police.ycor()-client.ycor())/(police.xcor()-client.xcor())
    policeUnitX = police.xcor()/incrementBetweenLines
    tangentSlope = 2*quadraticCoefficent*policeUnitX
    global normalSlope
    normalSlope = -1/max(tangentSlope, 0.000001)
    
def drawHeight():
    height_drawer.penup()
    height_drawer.clear()
    height_drawer.goto(police.xcor(), police.ycor())
    height_drawer.pendown()
    height_drawer.goto(police.xcor(), client.ycor())

def drawWestDistance():
    west_distance_drawer.penup()
    west_distance_drawer.clear()
    west_distance_drawer.goto(police.xcor(), client.ycor())
    west_distance_drawer.pendown()
    west_distance_drawer.goto(client.xcor(), client.ycor())


def updateInformation():
    info_drawer.clear()
    info_drawer.goto(-width//2+200, height//2-120)
    info_drawer.write(f"Normal Slope: {round(normalSlope, 4)}", align="center", font=("Arial", 25, "normal"))
    info_drawer.goto(-width//2+200, height//2-150)
    info_drawer.write(f"Police and Client Slope: {round(policeAndClientSlope, 4)}", align="center", font=("Arial", 25, "normal"))
    info_drawer.goto(-width//2+200, height//2-180)
    info_drawer.write(f"Superticks: {round(superticks, 4)}", align="center", font=("Arial", 25, "normal"))
    info_drawer.goto(-width//2+200, height//2-180)
    info_drawer.write(f"Superticks: {round(superticks, 4)}", align="center", font=("Arial", 25, "normal"))
    info_drawer.goto(-width//2+200, height//2-210)
    info_drawer.write(f"Newton distance: {round(newtonsExpectedDistance, 3)}", align="center", font=("Arial", 25, "normal"))
    info_drawer.goto(-width//2+200, height//2-240)
    info_drawer.write(f"Binary Distance: {round(binaryExpectedDistance, 3)}", align="center", font=("Arial", 25, "normal"))
    info_drawer.goto(-width//2+200, height//2-270)
    info_drawer.write(f"Distance travelled: {round((client.xcor()-westDistance*incrementBetweenLines)/incrementBetweenLines, 3)}", align="center", font=("Arial", 25, "normal"))
   
def drawPoliceNormalLine():
    police_normal_drawer.penup()
    police_normal_drawer.clear()
    police_normal_drawer.goto(police.xcor(), police.ycor())
    theta = math.atan(normalSlope)
    police_normal_drawer.setheading(theta*180/math.pi)
    police_normal_drawer.pendown()
    police_normal_drawer.forward(height)

def setup():
    graphLines()
    graphSouthRoad()
    graphQuadratic()

def runSimulation():
    while True:
        chase()
        global ticks
        ticks+=1
        global superticks
        superticks= ticks/superTickToTick

if __name__ == "__main__":
    setup()
    newtonsExpectedDistance = newtons_method(20)
    print(newtonsExpectedDistance)
    binaryExpectedDistance = bruteForce()

    runSimulation()
    screen.exitonclick()