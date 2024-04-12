import turtle, pandas, csv, datetime

turtle.penup()
screen = turtle.Screen()
screen.title("US Fifty States")
screen.bgpic("pythonCourse/day_25_background.gif")
screen.setup(750, 500)


with open("pythonCourse/day_25_statesXY.csv") as file:
    data = csv.reader(file)
    states = {}
    for row in data:
        if row[0]!="state":
            states.update({row[0]: (int(row[1]), int(row[2]))})

def addState(state: str):
    turtle.hideturtle()
    turtle.goto(states[state][0], states[state][1])
    turtle.write(state)
    turtle.showturtle()

def saveData():
    with open(f"pythonCourse/day_25_state_data/{datetime.datetime.now().date()}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["states missed:"])
        for state in states:
            writer.writerow([state])
    with open(f"pythonCourse/day_25_state_data/all_data.csv", "a") as file:
        writer = csv.writer(file)
        row = [f"{datetime.datetime.now().date()}", 50 - len(states)]
        print("Appending row to all_data.csv:", row)  # Add this line for debugging
        writer.writerow(row)
    exit()

def askForState():
    state = turtle.textinput(f"{len(states)}/50 states left", "Enter a state!")
    if states.get(state, False)!=False:
        addState(state)
        states.pop(state)
    elif state == "Exit":
        saveData()
    else:
        print(f"{state} is not a state.")

def startGame():
    while len(states)>0:
        askForState()


if __name__ =="__main__":
    startGame()