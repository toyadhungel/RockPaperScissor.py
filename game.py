import random



def rps():    
    opt= int(input('''
    please select one of the following options
    1. To play the game
    2. Quit: \n'''))

    if opt == 1:
        player1 = input("Select Rock, Paper, or Scissor :").lower()
        player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
        print("Player 2 selected: ", player2)

        if player1 == "rock" and player2 == "paper":
            print("Player 2 Won")
        elif player1 == "paper" and player2 == "scissor":
            print("Player 2 Won")
        elif player1 == "scissor" and player2 == "rock":
            print("Player 2 Won")
        elif player1 == player2:
            print("Tie")
        else:
            print("Player 1 Won")
    elif opt == 2 :
        print("Good bye")
     

    else:
        print("Wrong operator, please try again")

    playAgain()


def playAgain():
    print("Do you wanna play the game again? \n")
    answer=input("Enter Y/s for yes or N/n for no: \n" )

    if answer=='n':
        print("good bye, see you again")
    else:
        rps()



rps()