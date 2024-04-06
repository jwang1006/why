import os

allBidders = {}
otherBidders = True
while otherBidders:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n")
    allBidders[name] = bid
    otherBidders = input("Are there more bidders? Y/N\n")
    if otherBidders == "N":
        otherBidders=False
    os.system("clear")
highestBidder = list(allBidders.keys())[0]
for name in allBidders:
    if allBidders[highestBidder]<allBidders[name]:
        highestBidder = name
print(f"The highest bidder was {highestBidder} with a bid of {allBidders[highestBidder]} dollars")