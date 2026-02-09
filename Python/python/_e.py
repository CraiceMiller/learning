import random

def rock_paper_scissors():
    

    while True:

        game = ["rock", "paper", "scissors"]
        computer = random.choice(game)

        print("let's play it then :)")
        print()
        print("chosse one of this:")
        print(game)
        chosse = input().lstrip().lower()

        while not chosse in game: 
            print()
            print(" Write a valid input")
            print("chosse one of this:")
            print(game)
            chosse = input().lstrip().lower()

        print(f"player: " + chosse)
        print(f"computer: {computer} " )
        print()

        if chosse == computer:
            print("it's a tie ")
        elif chosse == "rock" and computer == "paper":
            print("You WIN!!")
        elif chosse == "paper" and computer == "rock":
            print("You WIN!!")
        elif chosse == "paper" and computer == "rock":
            print("You WIN!!")

        else: 
            print("you LOSE!!")
        print()
        print("do you want to play again ?: ")
        again = input().lstrip().lower()
        
        if again == "yes":
            pass
        else:
            break


#
want_play = True    
while want_play:
     
    games: list[str] = ["rock, paper, scissors", "guessing number"]
    print("what do you wnat to play today?: ")

    num = 1
    for i in games: 
        print(f"{num}. {i}")
        num += 1
        
        
        

    while True:
        print()
        play = input().lstrip()
        if play.isdigit():
            play = int(play)
            if play in range(len(games)):
                break
            
        print("please pick a or valid number ")

    if play == 1:
        rock_paper_scissors()

    print("do you want to play another game now?: ")
    print("yes, or not")
    again = input().lstrip().lower()
    if again == "yes":
        pass
    else:
        want_play = False


print("i hope you like my proyect")