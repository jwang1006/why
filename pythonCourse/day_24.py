names = []

with open("pythonCourse/day_24_invited_names.txt", mode = "r") as file:
    names = file.readlines()


print(names)

with open("pythonCourse/day_24_starting_letter.txt", mode = "r") as file:
    letter = file.read()

for name in names:
    name = name.replace("\n", "")
    with open(f"pythonCourse/day_24_letters/{name}.txt", mode = "w") as file:
        letterCopy = letter
        letterCopy = letterCopy.replace("[name]", name)
        letterCopy = letterCopy.replace("Angela", "J9")
        file.write(letterCopy)