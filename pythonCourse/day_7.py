import random, os, time

from day_7_dictionary import word_list
targetWord = word_list[random.randint(0, len(word_list)-1)]
oldGuess = ""
for n in range (0, len(targetWord)):
    oldGuess += "_"

from day_7_art import logo
print(logo)

lives = 6
while oldGuess.count("_")>0:
    guess = input("Guess a letter!: ")
    newGuess = ""
    found = False
    for n in range (0, len(targetWord)):
        if targetWord[n]==guess:
            newGuess+=guess
            found = True
        else:
            newGuess+=oldGuess[n]
    if found==False:
        print("Letter not found.")
        lives-=1
        print("You now have", lives, "left.")
        if lives==0:
            print("You're dead. Bye bye.")
            exit()
    oldGuess = newGuess
    from day_7_art import stages
    os.system("clear")
    print(stages[lives])
    print("Your word is now:", oldGuess)
    time.sleep(2)
print("You win! Thank's for playing!")