import random, time, os
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def interpretNumber(chosenNum):
    if chosenNum==1:
        print(rock)
    elif chosenNum ==2:
        print(scissors)
    else:
        print(paper)

def playAGame():
    print("Let's play rock paper scissors!")
    playerNum = int(input("Play 1 for Rock, 2 for Scissors, and 3 for Paper!: "))
    print("You played:")
    interpretNumber(playerNum)
    print("Alrighty, now the computer shall choose...")
    time.sleep(1)
    computerNum = random.randint(1, 3)
    interpretNumber(computerNum)
    if computerNum==playerNum:
        print("A tie.")
    elif computerNum == 1 and playerNum==2 or computerNum==2 and playerNum==3 or computerNum==3 and playerNum==1:
        print("Computer wins! Mwhahahaha")
    else:
        print("You win... this time.")


while True:
    playAGame()
    time.sleep(1)
    again = input("Would you like to play again? Y/N: ")
    if again=="N":
        print("Tired of losing, eh?")
        print("No worries. I'm always here, if you want to play again.")
        exit()
    print("Prepare to be beaten!")
    os.system("clear")