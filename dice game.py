import random

def dice_roll():
    diceroll=random.randint(1,6)
    return diceroll
def main():

    player1=0
    player2=0
    rounds=1
    player1wins=0
    player2wins=0
    while(rounds!=11):
        print("round ",rounds)
        player1=dice_roll()
        player2=dice_roll()
        print("the score of player 1 is ",player1)
        print("the score of player 2 is ",player2)
        rounds=rounds+1

        if player1==player2:
            print("Draw")
        elif player1>=player2:
            print("player 1 won")
            player1wins=player1wins+1
        else:
            print("player 2 won")
            player2wins=player2wins+1
        
        print("")

        if player2wins>player1wins:
            print("player 1 won the series")
        elif player1wins>player2wins:
            print("player 2 won the series")
        else:
            print("draw match both are winners")



main()
