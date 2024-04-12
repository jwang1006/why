import csv, pandas

def weatherData():
    with open("pythonCourse/day_25_weather_data.csv") as file:
        data = csv.reader(file)
        temperatures = []
        for row in data:
            if row[1]!="temp":
                temperatures.append(row[1])
        print(temperatures)

def squirrelData():
    print("running squirrel data")
    squirrelSheet = pandas.read_csv("pythonCourse/day_25_squirrels.csv")
    cinnamon = squirrelSheet[squirrelSheet["Primary Fur Color"].isin(["Cinnamon"])]
    black = squirrelSheet[squirrelSheet["Primary Fur Color"].isin(["Black"])]
    gray = squirrelSheet[squirrelSheet["Primary Fur Color"].isin(["Gray"])]
    
    colorSheet = pandas.DataFrame(
    {
        "Fur Color": ["cinnamon", "black", "gray"],
        "Count": [len(cinnamon), len(black), len(gray)],
    }
    )
    colorSheet.to_csv("pythonCourse/day_25_color_squirrels.csv")

        

if __name__=="__main__":
    squirrelData()