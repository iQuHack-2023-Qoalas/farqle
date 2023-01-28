import random

MAX_SCORE = 3000

# returns a sorted list of six randomly rolled dice values
def rollDice(diceList):
    # simulate the rolling of dice using random numbers
    for i in range(len(diceList)):
        diceList[i] = random.randrange(1,7)

    # return sorted list of dice values
    diceList.sort()
    return diceList

def removeItem(list, num):
    for i in range(len(list)):
        if(num in list):
            list.remove(num)

    return list

# returns the score of a roll
def getScore(diceList):
    score = 0
    tripletCount = 0
    pairCount = 0
    fourCount = 0

    #Find the count of each number 1..6 in the rolled dice and score appropriately
    for i in range(1,6):        
        if (diceList.count(i) == 6):
            diceList = removeItem(diceList, i)
            score = 3000
        if (diceList.count(i) == 5):
            diceList = removeItem(diceList, i)
            score = 2000
        if (diceList.count(i) == 4):
            diceList = removeItem(diceList, i)
            fourCount += 1
            score = 1000
        if (diceList.count(i) == 3):
            diceList = removeItem(diceList, i)
            tripletCount += 1
            score = i * 100
        if (diceList.count(i) == 2):
            pairCount += 1

    # Check for special cases and override score if present
    if(tripletCount == 2):
        score = 2500
    elif(pairCount == 3):
        score = 1500 
    elif(fourCount == 1 and pairCount == 1):
        score = 1500 
    elif(diceList == [1,2,3,4,5,6]):
        diceList = []
        score = 1500

    #Score the 5s and the 1s
    score += 50 * diceList.count(5)
    score += 100 * diceList.count(1)

    if(1 in diceList):
        diceList = removeItem(diceList, 1)
    
    if(5 in diceList):
        diceList = removeItem(diceList, 5)

    return score, diceList

# Walk the user through their turn
def playerTurn():
    roll = True
    input("It is Your Turn. Press Enter to Roll Dice\n")
    diceList = [0] * 6
    turnScore = 0

    while(roll):

        diceList = rollDice(diceList)
        print(f"You Rolled {diceList}")

        rollScore, diceList = getScore(diceList)
        print(f"This is Worth {rollScore} Points")

        turnScore += rollScore
        # Check for farkle
        if(rollScore == 0):
            print("You rolled a FARQLE and will gain no points for this turn :(")
            turnScore = 0
            break

        # Give users back all six dice if they run out and haven't farkled
        if(len(diceList) == 0):
            diceList = [0]*6

        print(f"The remaining Dice are {diceList}")

        # Ask if User Wants to Roll the Dice
        action = ""
        while(action != "yes" or action != "no"):
            action = input("Would you like to continue rolling? (yes/no)\n")

            # End Turn if Player Says No
            if(action == "yes"):
                print('-' * 41)
                break
            elif(action == "no"):
                roll = False
                break
            else:
                print("Please enter 'yes' or 'no'")

    print("Your Turn Has Ended")
    return turnScore

# simulate the computer opponent
def computerTurn():
    roll = True
    diceList = [0] * 6
    turnScore = 0

    while(roll):
        diceList = rollDice(diceList)
        print(f"Computer Rolled {diceList}")

        rollScore, diceList = getScore(diceList)
        print(f"This is Worth {rollScore} Points")

        turnScore += rollScore
        # Check for farkle
        if(rollScore == 0):
            print("Computer rolled a FARQLE and will gain no points for this turn :)")
            turnScore = 0
            break
        
        # Computer will never roll if only one dice remains
        if(len(diceList) == 1):
            break
        
        # Computer randomly decided to keep rolling
        roll = True if random.randrange(0,2) else False

        # Computer will keep rolling if there are at least 4 dice
        if(len(diceList) >= 4):
            roll = True

        if(roll == True):
            print("Computer will continue to roll")
        else:
            print("Computer will stop rolling")
    return turnScore


def main():
    
    playerScore = 0
    computerScore = 0

    title = ''' 
 ______              _      
|  ____|            | |     
| |__ __ _ _ __ __ _| | ___ 
|  __/ _` | '__/ _` | |/ _ \\
| | | (_| | | | (_| | |  __/
|_|  \__,_|_|  \__, |_|\___|
                  | |       
                  |_|     '''
    
    
    instructions = '''
    
You start each turn with 6 dice
Roll the dice to get points.
The following combination details how many points you will receive

1 = 100 points
5 = 50 points
Three of a kind = That number times 100
Four of any number = 1000 points
Five of any number = 2000 points
Six of any number = 3000 points
Two sets of three = 2500
Three sets of two = 1500
Set of four and set of two = 1500
A run of six = 1500

After each roll you set aside the dice that contribute points.
You can choose whether or not roll the remaining.
If you roll zero points in a roll though then you lose all points for that turn
and have to stop.

First player to 3000 points wins.
    
    '''

    print(title)
    print(instructions)
    while(playerScore <= MAX_SCORE and computerScore <= MAX_SCORE):
        print("-" * 41)
        playerScore += playerTurn()
        print(f"PLAYER SCORE: {playerScore} \t COMPUTER SCORE: {computerScore}")
        
        print("-" * 41 + "\nCOMPUTER TURN")
        computerScore += computerTurn()

        print(f"PLAYER SCORE: {playerScore} \t COMPUTER SCORE: {computerScore}")

    if(playerScore > computerScore):
        print("YOU WON!!!")
    else:
        print("the computer won")

if(__name__ == "__main__"):
    main()