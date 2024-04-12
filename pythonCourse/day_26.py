import pandas

with open("pythonCourse/day_26_nato.csv", "r") as file:
    alphabet = pandas.read_csv(file)

nato_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

toNato = input("What would you like to spell out?\n")
natofied = [nato_dict[letter.upper()] for letter in toNato]
print(natofied)