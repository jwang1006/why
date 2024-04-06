import time, random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def play_a_game():
    from day_12_art.py import logo
    print(logo)
    print("Welcome to the Number Guessing Game!")
    mode = input("Choose a difficulty: 'easy' or 'hard'")
    if mode=="easy":
        guesses=10
    else:
        guesses=5
    time.sleep(1)
    print("I'm thinking of a number between 1 and 100.")
    targetNum = random.randint(1, 100)
    while guesses>0:
        guesses-=1
        if play_a_round(targetNum):
            print(f"You got it in {10-guesses}!")
            exit()
        print(f"You have {guesses} attempts left")
    print(f"The number was {targetNum}")

def play_a_round(targetNum):
    guessedNum = int(input("Make a guess: "))
    if guessedNum>targetNum:
        print("Too high")
    elif guessedNum<targetNum:
        print("Too low")
    else:
        print("You got it!")
        return True

