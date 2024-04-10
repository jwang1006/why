import csv

with open("pythonCourse/day_25_weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1]!="temp":
            temperatures.append(row[1])
    print(temperatures)