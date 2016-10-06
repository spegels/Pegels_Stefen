import random

playerNum=random.randint(1,6)
compNum=random.randint(1,6)

def rollDice():
    player="you!"
    comp="the computer!"
    null="nobody!"
    if playerNum > compNum:
        winner=player
    if compNum > playerNum:
        winner=comp
    if compNum==playerNum:
        winner=null
    return (winner)

print("You rolled a",playerNum)
print("The computer rolled a", compNum)

print("The winner is",rollDice())
    
