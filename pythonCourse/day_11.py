import random, os, time
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

yourCards = []
dealerCards = []
dealerPoints = 0
yourPoints = 0

def dealCard(personCards):
    personCards.append(cards[random.randint(0, len(cards)-1)])

def countPoints(personHand):
    hand = 0
    containsAce = False
    for card in personHand:
        if card == "A":
            hand+=1
            containsAce = True
        elif card == "J" or card == "Q" or card == "K":
            hand+=10
        else:
            hand+=int(card)
    if (containsAce): 
        return [hand, hand+10]
    else:
        return [hand]
        

def clearTable():
    yourCards.clear()
    dealerCards.clear()

def startGame():
    from day_11_art import logo
    print(logo)
    print("Welcome to BlackJack!")
    time.sleep(1)
    playAnotherRound = "Y"
    while playAnotherRound == "Y":
        playRound()
        print(f"Scores: You have {yourPoints}; Computer has {dealerPoints}")
        playAnotherRound = input("Play another round? Y/N: \n")
        os.system("clear")
    
def startRound(): 
    print("Shuffling cards...")
    time.sleep(1)
    dealCard(yourCards)
    print(f"You have been dealt {yourCards[len(yourCards)-1]}.")
    print("For the dealer...")
    time.sleep(1)
    dealCard(dealerCards)
    print(f"The dealer has been dealt {dealerCards[len(dealerCards)-1]}.")
    print("Dealing the next two cards...")
    time.sleep(2)
    dealCard(yourCards)
    dealCard(dealerCards)
    print(f"You have been dealt {yourCards[len(yourCards)-1]}, while the dealer... well, you'll just have to find out!")
    time.sleep(2)
    print("Now, let the game begin!")

def stay():
    return True

def hit():
    dealCard(yourCards)
    return getBestValidHand(yourCards)

inputToMethod = {"stay": stay, "hit": hit}

def playRound():
    startRound()
    validHand = True
    while validHand:
        os.system("clear")
        print(f"Your current cards are: {yourCards}, and they sum up to {countPoints(yourCards)}")
        print(f"The dealer's cards are: {dealerCards[0]}, and a hidden card.")
        time.sleep(1)
        decision = input("Would you like to 'hit' or 'stay'?\n")
        if inputToMethod[decision]() == True:
            print(f"The dealer's current hand (revealed) is: {dealerCards}")
            dealerPlays()
            break
        elif inputToMethod[decision]() == False:
            print("Dealer wins.")
            global dealerPoints
            dealerPoints +=1
            break
            


def getBestValidHand(personHand):
    bestHand = 0
    for possibleHand in countPoints(personHand):
        if possibleHand<=21 and possibleHand>bestHand:
            bestHand = possibleHand
    if bestHand<=21:
        return bestHand
    return False
    
            
def dealerPlays():
    playerBestHand = getBestValidHand(yourCards)
    dealerBestHand = getBestValidHand(dealerCards)
    while dealerBestHand<=playerBestHand:
        dealCard(dealerCards)
        print(f"The Dealer had been dealt {dealerCards[len(dealerCards)-1]}")
        dealerBestHand=getBestValidHand(dealerCards)
        if dealerBestHand==False:
            print("You win.")
            global yourPoints
            yourPoints+=1
            return
        time.sleep(1)

    print(f"The dealer wins: {dealerBestHand} to {playerBestHand}")
    global dealerPoints
    dealerPoints+=1

startGame()