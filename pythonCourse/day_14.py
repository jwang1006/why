import os, time, random

from day_14_data import data

def startGame():
    from day_14_art import logo, vs 
    print(logo)
    index1 = random.randint(0, len(data)-1)
    index2 = random.randint(0, len(data)-1)
    numRight = 0
    while True:
        while index1==index2:
            index2 = random.randint(0, len(data)-1)
        count1 = printInfo("Compare A:", index1)
        time.sleep(1)
        print(vs)
        time.sleep(1)
        count2 = printInfo("Against B:", index2)
        time.sleep(1)
        followers = input("Who has more followers? Type 'A' or 'B'.\n")
        if followers == "A" and count1>count2 or followers == "B" and count2<count1:
            print("Correct!")
            numRight+=1
            index1=index2
            print("Starting next round...")
            time.sleep(1)
            os.system("clear")
        else:
            print(f"Wrong answer. 'A' has {count1} followers while 'B' has {count2} followers.")
            again = input(f"You got {numRight} correct in total. Play again? Y/N: \n")
            if again == "Y":
                os.system("clear")
                startGame
            break

    
def printInfo(startWith, index):
    personInfo = data[index]
    print(f"{startWith} {personInfo["name"]}, {personInfo["description"]}, from {personInfo["country"]}")
    return personInfo["follower_count"]

startGame()