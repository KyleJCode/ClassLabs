from random import randint

def humanTurn(humanTotalScore):
    char = None
    roundScr = 0
    while char != 'r':
        char = input("It's your turn! Enter 'r' to roll.\n")
    while char != 'h':
        diceRoll = randint(1, 6)
        if diceRoll == 1:
            char = None
            while char != 'c':
                char = input("You rolled 1\nYou lose your turn. Enter 'c' to continue.\n")
            return 0
        roundScr += diceRoll
        print(f"You rolled {diceRoll}\nYour score this round is: {roundScr}\n"
              f"If you hold, your total score would be: {humanTotalScore+roundScr}")
        char = input("Press 'h' to hold or 'r' to roll again. ")
    return roundScr, 1

def computerTurn(compTotalScore):
    return 0, 1

def main():
    playerTotal = 0
    computerTotal = 0
    turnCalc = 0
    winner = None
    while winner == None:
        if turnCalc == 0:
            roundScore, turnCalc = humanTurn(playerTotal)
            playerTotal += roundScore
        elif turnCalc == 1:
            roundScore, turnCalc = computerTurn(computerTotal)
            computerTotal += roundScore

        roundScore = 0


main()


